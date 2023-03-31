import graphene

class QueryType(graphene.ObjectType):
    name = "Query"
    description = "The query root of this schema"

    hello = graphene.String(default_value="Hi!")

schema = graphene.Schema(query=QueryType)