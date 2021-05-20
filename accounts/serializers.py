from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
        # extra_kwargs dict is made to give extra property to the fields under it, here we've made both passwords fields
        # as write_only=True, so that no one can read it.
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    # Note: both create and update methods always returns the instance of the model it uses (here: User).
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = User(username=username, email=email)
            user.set_password(password)
            user.is_staff = True
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match',
            })
