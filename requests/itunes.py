""" Api connection
cmd line value will ba used as search criteria. 
such as providing "weezer" will make GET call to fetch songs related to weezer
"""
import requests

# if len(sys.argv) != 2:
#     sys.exit()
# try:
#     response = requests.get(
#         "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
#     )
# except requests.exceptions.RequestException as e:  # This is the correct syntax
#     raise SystemExit(e)

# o = response.json()
# for i in o["results"]:
#     print(i["trackName"])

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
o = response
print(o.json())
print(o.status_code)
