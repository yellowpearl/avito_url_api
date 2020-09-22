
import urllib.parse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
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
        url = decode_request_body(request)
        url = check_http_or_https(url)
        return HttpResponse(check_url_in_bd_or_hash(url))
    return HttpResponse("ERR GET")
