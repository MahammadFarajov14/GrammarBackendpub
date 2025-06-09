from rest_framework.filters import BaseFilterBackend
from grammars.models import RuleCategory

class RuleCatFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return super().filter_queryset(request, queryset, view)
        print(queryset)