import requests
import json

#url="https://api.imagga.com/v2/tags"
url="https://api.imagga.com/v2/categorizers"
querystr={"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2dJ8FhuEHJzFAWsmqTAc1izd91dc03gLuqA&usqp=CAU "}
headers={
    'accept':"application/json",
    'authorization': "Basic=="
}


response=requests.request("GET",url,headers=headers,params=querystr)
data=json.loads(response.text.encode("ascii"))
print(data)

for i in range(5):
    #tag = data["result"]["tags"][i]["tag"]["en"] for tags
    tag = data["result"]["categorizers"][i]["labels"]
    for k in tag:
        print(k)
