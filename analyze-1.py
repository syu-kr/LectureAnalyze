import requests
import xmltodict
import json
import time
import os

for year in range(1999, 2024):
  for semester in [10, 20]:
    url = "https://suwings.syu.ac.kr/websquare/engine/proworks/callServletService.jsp"
    
    xml = ""
    
    with open("request1.xml", "r", encoding="UTF-8") as file:
      xml = file.read().replace(f"{{year}}", str(year)).replace(f"{{semester}}", str(semester))

    headers = {"Content-Type": "application/xml"}

    request = requests.post(url, data=xml, headers=headers)

    xpars = xmltodict.parse(request.text)
    
    data = {}
    
    # if not os.path.exists("./전체/"):
    #   os.makedirs("./전체/")
    
    # with open(f'./전체/{year}년 {"1" if semester == 10 else "2"}학기.json', "w", encoding="UTF-8") as f:
    #   json.dump(xpars, f, ensure_ascii=False, indent=2)
    
    for classInfo in xpars["vector"]["data"]:
      data[classInfo["ROW"]["ORGN4_NM"]["@value"]] = True
    
    if not os.path.exists("./학부(과)/"):
      os.makedirs("./학부(과)/")

    with open(f'./학부(과)/{year}년 {"1" if semester == 10 else "2"}학기.json', "w", encoding="UTF-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=2)
    
    time.sleep(1)