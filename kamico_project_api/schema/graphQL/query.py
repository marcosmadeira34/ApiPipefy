import graphene
from api.models import Card as CardModel
from schema.graphQL.schema import SnippetType

class Query(graphene.ObjectType):
    all_snippet = graphene.List(SnippetType)    

    def resolve_all_snippets(self, info, **kwargs):
        return CardModel.objects.all()

    def all_results(self, info, **kwargs):
        return CardModel.objects.all()

schema = graphene.Schema(query=Query)