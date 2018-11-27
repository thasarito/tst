from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class WordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Word
		fields = ('spelling',)

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('name',)

class DescriptionSerializer(serializers.ModelSerializer):
	word = WordSerializer()
	tag = TagSerializer(many=True)

	class Meta:
		model = Description
		fields = ('id', 'word', 'meaning', 'example', 'tag', 'author')	

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'id',)