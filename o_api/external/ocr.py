# https://ocr.space/OCRAPI
# K81787531788957
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true

import requests


url = 'https://api.ocr.space/parse/imageurl?apikey=K81787531788957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
response = requests.get(url) # request로 url을 받아오게됨
response.raise_for_status()
result = response.json()
print(result) # 리턴값임.(결과값), dictionary 타입으로 받아옴
print(result['ParsedResults'][0]['ParsedText'])