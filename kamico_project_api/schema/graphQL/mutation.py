import graphene
from schema.graphQL.schema import CreateCardType, AllCardType
from api.models import CreateCardModel



class AllCard(graphene.InputObjectType):
    class Arguments:
        first = graphene.Int()
        after = graphene.String()
        last = graphene.String()
        before = graphene.String()
        pipeId = graphene.String()
        filter = graphene.String()


    @classmethod
    def mutate(self, title, description, image):
        card = AllCard(title=title, description=description, image=image)
        card.save()
        return AllCard(all_card=card)


class Mutation(graphene.ObjectType):
    create_card = AllCard.Field()






    