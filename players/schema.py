import graphene
from graphene_django import DjangoObjectType

from .models import Player, Club, Position


class ClubType(DjangoObjectType):
    class Meta:
        model = Club
        fields = ("id", "name", "players")


class PositionType(DjangoObjectType):
    class Meta:
        model = Position
        fields = ("id", "name")


class PlayerType(DjangoObjectType):
    full_name = graphene.String()

    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'base_salary',
                  'guaranteed_compensation', 'club', 'positions')

    def resolve_full_name(self, info):
        return f"{self.first_name} {self.last_name}"


class Query(graphene.ObjectType):
    player = graphene.Field(PlayerType, id=graphene.Int())
    club = graphene.Field(ClubType, id=graphene.Int())
    position = graphene.Field(PositionType, id=graphene.Int())
    players = graphene.List(PlayerType)
    clubs = graphene.List(ClubType)
    positions = graphene.List(PositionType)

    def resolve_player(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Player.objects.get(pk=id)

        return None

    def resolve_club(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Club.objects.get(pk=id)

        return None

    def resolve_position(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Position.objects.get(pk=id)

        return None

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()

    def resolve_clubs(self, info, **kwargs):
        return Club.objects.all()

    def resolve_positions(self, info, **kwargs):
        return Position.objects.all()


schema = graphene.Schema(query=Query)
