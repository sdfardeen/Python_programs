from src.DataTypes.fetch_uid import data


res = {}

for items in data:
    print(items.get('json_data'))
    if items.get('st2') == 'AD_IMPRESSION':
        resu = (items['json_data'].get('publisher_revenue') * 100) == (items.get('v'))
        print('TRUE')


    else:
        print("false")
