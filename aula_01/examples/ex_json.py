#coding:utf-8
import json
from pprint import pprint

data = {'nome': 'Alice', 'idade': 24}

json_data = json.dumps(data)
print u"Conteúdo JSON: '%s'" % json_data

dict_data = json.loads(json_data)
print u'\nConteúdo em dict de novo: '
pprint(dict_data)
