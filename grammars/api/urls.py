from django.urls import path
from grammars.api.views import RulesApiView, RuleUpdateApiView

urlpatterns = [
    path('rules/', RulesApiView.as_view(), name = 'rules'),
    path('rule/<int:pk>/', RuleUpdateApiView.as_view(), name = 'rule_update'),

]