from grammars.models import Rule
from django.http import JsonResponse
from grammars.api.serializers import RuleSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
def rules(request):
    rules = Rule.objects.all()
    serializer = RuleSerializer(rules, many = True)
    # rule_dict = []
    # for rule in rules:
    #     rule_dict.append({
    #         'id': rule.id,
    #         'title': rule.title
    #     })

    return JsonResponse(data=serializer.data, safe=False)

class RulesApiView(ListCreateAPIView):
    serializer_class = RuleSerializer
    queryset = Rule.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]

class RuleUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = RuleSerializer
    queryset = Rule.objects.all()