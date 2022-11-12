import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")
# res レスポンスの省略形

# print(res.text["status"])
print(res.json()["status"])
# json形式で
json = res.json()
print(res.json()["results"][0]["address1"])
print(res.json()["results"][0]["address2"])
print(res.json()["results"][0]["address3"])
print(res.json()["results"][0]["prefcode"])
