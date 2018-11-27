from django.db import models
import math
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.name

class Word(models.Model):
	spelling = models.CharField(max_length=128, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.spelling

class Description(models.Model):
	word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="meaning")
	meaning = models.TextField()
	example = models.TextField()
	tag = models.ManyToManyField(Tag)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'ความหมายของคำว่า {self.word}'

class Description_Vote(models.Model):
	post = models.ForeignKey(Word, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	VOTE_CHOICES = (
		('UP', 'UPVOTE'),
		('DOWN', 'DOWNVOTE'),
		)
	action = models.CharField(max_length=4, choices=VOTE_CHOICES, default=None)
	saved = models.BooleanField()

	def __str__(self):
		return f"{user} {action} {post} post saved: {saved}"