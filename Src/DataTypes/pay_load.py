import json

from src.DataTypes.fetch_uid import data

res = set()
for item in data:
    if item.get('json_data',{}).get('resources',{}):
        res.add(json.loads(item.get('json_data',{}).get('resources',{})).get('payloads_hash'))
print(res)
