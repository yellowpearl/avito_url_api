from django.test import TestCase
import requests


client = requests.session()
r = requests.post('http://127.0.0.1:8000/s/short', data={'url':'google.com'})
print(r.text)
r = requests.post('http://127.0.0.1:8000/s/short', data={'url':'vk.com'})
print(r.text)
r = requests.post('http://127.0.0.1:8000/s/short', data={'url':'youtube.com'})
print(r.text)
r = requests.post('http://127.0.0.1:8000/s/short', data={'url':'avito.com'})
print(r.text)
print('Just try http://127.0.0.1:8000/s/"hash" to redirect on full link')

