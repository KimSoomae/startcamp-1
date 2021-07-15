import requests


name = 'eric'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()

print(response)


"""
실습
"""
name = response['name']
age = response['age']
print(f'{name}의 나이는 {age}입니다.')