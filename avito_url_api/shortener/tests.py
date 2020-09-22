from django.test import TestCase
import requests
headers = {'User-Agent': 'My User Agent 1.0',}

client = requests.session()
r = requests.post('http://127.0.0.1:8000/s/short', data={'url':'piepi.com'}, headers=headers)
print(r.text)
#print(r.text[r.text.index('=')+1:])
#print(requests.post('http://127.0.0.1:8000/s/short', data={'key':'vk.com'}, headers=headers).text)
print(requests.get('http://127.0.0.1:8000/s/wewe'))
print(requests.get('http://127.0.0.1:8000/s/google'))
print(requests.get('http://127.0.0.1:8000/s/vkcom'))
