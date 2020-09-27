from django.test import TestCase
import requests


client = requests.session()
r = requests.post('http://127.0.0.1:8000/s/short', data={'url':'piepi.com'})
print(r.text)
#print(r.text[r.text.index('=')+1:])
#print(requests.post('http://127.0.0.1:8000/s/short', data={'key':'vk.com'}, headers=headers).text)
print(requests.get('http://127.0.0.1:8000/s/wewe').text)
print(requests.get('http://127.0.0.1:8000/s/google'))
print(requests.get('http://127.0.0.1:8000/s/'))
