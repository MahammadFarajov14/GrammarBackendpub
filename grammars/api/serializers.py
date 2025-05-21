from rest_framework import serializers
from grammars.models import Rule

class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rule
        fields = (
            'id',
            'title',
            'description',
        )

