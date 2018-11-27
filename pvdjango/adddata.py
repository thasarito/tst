from dictionary.models import *
from django.contrib.auth.models import User

ter = User.objects.create_superuser('ter', 'admin@example.com', 'terterter', first_name="ธสฤษฏ์", last_name="บุญศิริ")
ter.save()

tags = ['เหนือ', 'กลาง', 'อีสาน', 'ใต้', 'ตะวันออก', 'ตะวันตก']
for t in tags:
	tag = Tag.objects.create(name=t)
	tag.save()

# Add social login
from django.contrib.sites.models import Site
s = Site.objects.get()
s.domain = 'localhost:8000'
s.save()

import csv
import datetime
from allauth.socialaccount.models import *
with open('../providerinfo.csv', encoding='utf-8', newline='') as provider:
	reader = csv.DictReader(provider)
	for row in reader:
		print(row)
		provider = row['\ufeffProvider']
		name = row['Name']
		client_id = row['Cliend id']
		secret = row['Secret key']
		social_app = SocialApp.objects.create(provider=provider, name=name, client_id=client_id,secret=secret)
		social_app.sites.add(s)
		social_app.save()


import json
f = open('../endata.json', encoding='utf-8')
list_d = json.loads(f.read())

import random
all_tag = Tag.objects.all()
for d in list_d:
	word = d['word']
	meaning = d['meaning']

	W = Word.objects.create(spelling=word)
	W.save()

	Desc = Description.objects.create(word=W, meaning=meaning, example=meaning)
	word_tags = random.choices(all_tag, k=random.randint(1, 3))
	for t in word_tags:
		Desc.tag.add(t)
	Desc.save()

