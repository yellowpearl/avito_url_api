from django.test import TestCase
import requests
import unittest


class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()

headers = {'User-Agent': 'My User Agent 1.0',}

client = requests.session()
r = requests.post('http://127.0.0.1:8000/s/short', data={'url':'piepi.com'}, headers=headers)
print(r.text)
#print(r.text[r.text.index('=')+1:])
#print(requests.post('http://127.0.0.1:8000/s/short', data={'key':'vk.com'}, headers=headers).text)
print(requests.get('http://127.0.0.1:8000/s/wewe').text)
print(requests.get('http://127.0.0.1:8000/s/google'))
print(requests.get('http://127.0.0.1:8000/s/vkcom'))
