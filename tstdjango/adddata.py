import json
from dictionary.models import *


f = open('../endata.json', encoding='utf-8')
list_d = json.loads(f.read())

for d in list_d:
    dobj = Dictionary.objects.create(
        name = d['word'],
        readas = d['readas'],
        meaning = d['meaning'],
        url = d['url'],
    )
    dobj.save()
