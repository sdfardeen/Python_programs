from src.DataTypes.fetch_uid import data

# modification
res = []

for item in data:
    if item.get('st2') == 'AD_IMPRESSION':
        res.append(item.get('st2'))
    if item.get('json_data') and item['json_data'].get('publisher_revenue'):
        print(item.get('json_data'))
        if item['json_data'].get('publisher_revenue',0) * 100 == item.get('v'):
            print("true")

        else:
            print("false")

print(res)


