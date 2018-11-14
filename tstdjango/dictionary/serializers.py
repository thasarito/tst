from rest_framework import serializers
from .models import Dictionary

class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'url', 'name', 'readas', 'meaning', 'up', 'down')
