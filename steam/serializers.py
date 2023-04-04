from steam.models import Mail, Game, Account
from rest_framework import routers, serializers, viewsets


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'coast')


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ('id', 'login', 'password')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer(many=True)
    mail = MailSerializer()
    class Meta:
        model = Account
        fields = [
            'id', 'login', 'password', 'coast', 'game', 'mail', 'description'
        ]
