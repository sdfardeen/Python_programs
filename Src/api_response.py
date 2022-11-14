import requests


def get_api_response(url, params, api_type="GET", headers={}):
    response = ""
    if api_type.upper() == "GET":
        response = requests.get(url, params).json()
    elif api_type.upper() == "POST":
        response = requests.post(url, params).json()
    else:
        print("Please enter the valid request type")
    return response


ed = get_api_response(
    "https://www.amazon.com",
                      {"playerId": "test_rev_sdk_rv"}
)

print(ed)

