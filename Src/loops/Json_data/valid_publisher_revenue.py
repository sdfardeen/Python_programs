from src.loops.Json_data.fetching_uids import data

# taking empty result as list
res = []

# iterating every item in data using for loop
for item in data:
    # checking that st2 = ad_impression in data
    if item.get('st2') == 'AD_IMPRESSION':
        # giving a condition that, if st2 = ad_impression in data
        # then add that item's data in res using list.append()
        res.append(item.get('st2'))
    # checking json_data is in data or not
    # and checking that if json_data is in given data,
    # then check publisher_revenue is in json_data or not
    if item.get('json_data') and item['json_data'].get('publisher_revenue'):
        # if json_data in data, then we are printing that json_data
        print(item.get('json_data'))
        # checking after if publisher_revenue in json_data,
        # then multiply publisher_revenue's value with 100,
        # after multiplying with 100, we are assuming that result should match with,
        # the item 'v' in given data
        if item['json_data'].get('publisher_revenue',0) * 100 == item.get('v'):
            # if result matches with item 'v', then we are printing true
            print("true")
        else:
            # or else printing false
            print("false")

print(res)
