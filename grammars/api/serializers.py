from rest_framework import serializers
from grammars.models import RuleCategory, RuleSubCategory


class RuleSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = RuleSubCategory
        fields = (
            'category_id',
            'id',
            'title',
            'content',
        )

class RuleCategorySerializer(serializers.ModelSerializer):
    subcategories = RuleSubCategorySerializer(many = True, read_only = True)
    class Meta:
        model = RuleCategory
        fields = (
            'id',
            'title',
            'subcategories'
        )


# class RuleSerializer(serializers.ModelSerializer):

#     category = RuleCategorySerializer()

#     class Meta:
#         model = Rule
#         fields = (
#             'id',
#             'title',
#             'category',
#             'description',
#         )


