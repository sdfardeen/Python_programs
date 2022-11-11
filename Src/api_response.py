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
    "https://sbox1.gluid.internal.revtech.glulive.com/gluid/v1/links/search",
                      {"playerId": "test_rev_sdk_rv"}
)

print(ed)

