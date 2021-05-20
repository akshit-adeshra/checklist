from rest_framework import serializers
from core.models import CheckList, CheckListItem


class CheckListItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CheckListItem
        fields = '__all__'


class CheckListSerializer(serializers.ModelSerializer):
    # here we are specifying a new field named items so as to we can see all the items of a checklist in its nested form
    items = CheckListItemSerializer(source='checklistitem_set', many=True, read_only=True)
    # above we have passed the foreign_key (that we've already defined along with the CheckListItem model) in the source
    # parameter, many=True is specified as there can be multiple CheckList items for a single checklist, and
    # read_only=True is specified so user can not create new item while reading all the checklists.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CheckList
        fields = '__all__'
