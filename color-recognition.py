import requests
import json


url="https://api.imagga.com/v2/colors"
querystr={"image_url":"https://thumbs.dreamstime.com/z/people-group-selfie-friendly-guy-makes-photo-smiling-friends-smartphone-camera-hands-taking-self-portrait-photos-131283306.jpg "}
headers={
    'accept':"application/json",
    'authorization': "Basic YWNjX2QzZmI3ZjU0OTI2OTFmYTphODlhMmM3NGY4ZTllYWJhOTE3NTNiMjVmOGQ4ZDYxMg=="
}


response=requests.request("GET",url,headers=headers,params=querystr)
data=json.loads(response.text.encode("ascii"))
print(data)
tag = data["result"]["colors"]["background_colors"]
n=len(tag)
print(n)
for i in range(n):

    tag = data["result"]["colors"]["background_colors"][i]["closest_palette_color"]
    print(tag)
