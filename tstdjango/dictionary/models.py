from django.db import models
import math
from django.contrib.auth.models import User

# class Dictionary(models.Model):
#     name = models.CharField(max_length=128)
#     readas = models.CharField(max_length=128)
#     meaning = models.TextField()
#     src = models.URLField()
#     up = models.PositiveIntegerField(default=0)
#     down = models.PositiveIntegerField(default=0)

#     def percentUp(self):
#     	return math.log(self.up+self.down+1) + self.up/(self.up+self.down+1)


class Tag(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Word(models.Model):
	spelling = models.CharField(max_length=128)
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
		return f'ความหมายของคำว่า {word}'

class Description_Vote(models.Model):
	post = models.ForeignKey(Word, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	VOTE_CHOICE = (
		('UP', 'UPVOTE'),
		('DOWN', 'DOWNVOTE'),
		)
	action = models.CharField(max_length=4, choices=VOTE_CHOICE, default=None)
	saved = models.BooleanField()

	def __str__(self):
		return f"{user} {action} {post} post saved: {saved}"