import requests

url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev"
serviceKey = 'h3DCxIcAkIXuXZtegIqGtNRej9XJVZ%2FBXiAbYtnU%2BNYH1RXY7RNh2WunydDz1Tr9OMB0EtQn9HLhT4aUB%2Bo9Xg%3D%3D'
url += f"?serviceKey={serviceKey}"
# url += f"&pageNo={pageNo}"
# url += f"&numOfRows={numOfRows}"
LAWD_CD = '11260'  # 중랑구
DEAL_YMD = '202201'
url += f"&LAWD_CD={LAWD_CD}"
url += f"&DEAL_YMD={DEAL_YMD}"
print(url)
response = requests.get(url)
#
print(response)
