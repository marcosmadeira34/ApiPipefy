import graphene
from graphene_django.types import DjangoObjectType
from api.models import Card as CardModel, AllCard


class CreateCardType(DjangoObjectType):
    class Meta: 
        model = CardModel
        fields = "__all__"


class CreatePhaseType(DjangoObjectType):
    class Meta: 
        model = ""
        fields = "__all__"

class AllCardType(DjangoObjectType):
    class Meta: 
        model = AllCard
        fields = "__all__"