from django.db import models
import urllib.parse
import hashlib

def decode_request_body(request):
    """
    decode post request body and unquote him to urlencode our url
    :return:
    """
    url = urllib.parse.unquote(request.body.decode())
    url = url[url.index('=') + 1:]
    return url


def check_http_or_https(url):
    """return url only with https prefix"""
    if url[:8] != 'https://':
        if url[:7] != 'http://':
            url = 'https://' + url[7:]
        else:
            url = 'https://' + url
    return url


def check_url_in_bd_or_hash(url):
    """if the link exists, it will return its hash or call hash_url"""
    try:
        link = Link.objects.get(full_link=url)
        return link.short_link_hash
    except:
        return hash_url()


def hash_url(url):
    """Create sha hash for our url and return last 8 symbols it if hash does not exist in db"""
    while True:
        sha_obj = hashlib.sha1(url.encode('utf-8'))
        sha = sha_obj.hexdigest()[-8:]
        try:
            link = Link.objects.get(short_link_hash=sha)
        except:
            Link.objects.create(full_link=url, short_link_hash=sha)
            return sha


class Link(models.Model):
    full_link = models.CharField(max_length=2048)
    short_link_hash = models.CharField(max_length=200)
