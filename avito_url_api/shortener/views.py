
import urllib.parse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Link
import hashlib
import logging
logger = logging.getLogger(__name__)

def redirect(request, **kwargs):
    short_hash = kwargs['hash']
    logger.error(f'Trying to get {short_hash}')
    try:
        link = Link.objects.get(short_link_hash=short_hash)
        logger.error(f'Redirect to {link.full_link}')
        return HttpResponseRedirect(link.full_link)
    except:
        return HttpResponse(f"Cant GET {short_hash}.")


def shortener(request):
    if request.method == 'POST':
        # write request body in url var
        url = request.body.decode()
        logger.error(url)
        url = urllib.parse.unquote(url)
        logger.error(url)
        url = url[url.index('=')+1:]
        logger.error(url)
        # check url
        if url[:8] != 'https://':
            url = 'https://' + url
        logger.error(url)
        # check url string in db
        try:
            link = Link.objects.get(full_link=url)
        except:
            while True:
                # create hash
                sha_obj = hashlib.sha1(url.encode('utf-8'))
                sha = sha_obj.hexdigest()
                logger.error(sha)
                sha = sha[-8:]
                logger.error(sha)
                # check hash string in db
                try:
                    link = Link.objects.get(short_link_hash=sha)
                    logger.error('trying get with sha')
                except:


                    # create new Link
                    Link.objects.create(full_link=url, short_link_hash=sha)
                    logger.error('Short url is create')
                    return HttpResponse(sha)


    return HttpResponse("ERR GET")


