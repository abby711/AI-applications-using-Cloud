import requests
import json

#url="https://api.imagga.com/v2/tags"
url="https://api.imagga.com/v2/faces/detections"
querystr={"image_url":"https://www.recruitmentplus.ie/wp-content/uploads/2017/10/group-photo.jpg"}
headers={
    'accept':"application/json",
    'authorization': "Basic YWNjX2QzZmI3ZjU0OTI2OTFmYTphODlhMmM3NGY4ZTllYWJhOTE3NTNiMjVmOGQ4ZDYxMg=="
}


response=requests.request("GET",url,headers=headers,params=querystr)
data=json.loads(response.text.encode("ascii"))
print(data)

tag = data["result"]["faces"][0]["attributes"]
n=len(tag)
print("number of faces present in this picture are: ",n)
