from earningscalls.models import EarningsCall
from django.forms import widgets
from rest_framework import serializers
from earningscalls.models import EarningsCall
from django.contrib.auth.models import User

class EarningsCallSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = EarningsCall
        fields = ('ticker', 'quarter', 'calldate', 'calltime', 'url', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    earningscalls = serializers.HyperlinkedRelatedField(many=True, view_name='earningscall-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'earningscalls')
