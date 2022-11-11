import json
from src.loops.Json_data.fetching_uids import data

# taking empty result as set(), in set() there'll no duplicates
res = set()

# iterating every item in given data
for item in data:
    # checking that key:'resources' in json_data
    if item.get('json_data', {}).get('resources', {}):
        # if that key:'resources' is in json_data,
        # then checking key:'payloads_hash' in key:'resources'
        # if there's a key named by that,then add the value in res, using set.add()
        # here json.loads is for converting string to dict
        res.add(json.loads(item.get('json_data', {}).get('resources', {})).get('payloads_hash'))
print(res)
