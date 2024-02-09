import requests
import xmltodict
import json
import os

url = "https://suwings.syu.ac.kr/websquare/engine/proworks/callServletService.jsp"

xml = ""

with open("request2.xml", "r", encoding="UTF-8") as file:
  xml = file.read()

headers = {"Content-Type": "application/xml"}

request = requests.post(url, data=xml, headers=headers)

xpars = xmltodict.parse(request.text)

data = {}

for classInfo in xpars["vector"]["data"]:
  data[classInfo["RESULT"]["ORGN_NM"]["@value"].replace("(폐지)", "")] = True

if not os.path.exists("./폐지 학부(과)/"):
  os.makedirs("./폐지 학부(과)/")

with open("./폐지 학부(과)/data.json", "w", encoding="UTF-8") as f:
  json.dump(data, f, ensure_ascii=False, indent=2)
