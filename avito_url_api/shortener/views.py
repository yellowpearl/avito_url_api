from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from .models import *


def redirect(request, **kwargs):
    """if hash in db redirect to full link"""
    short_hash = kwargs['hash']
    try:
        link = get_full_url_from_hash(short_hash)
        return HttpResponseRedirect(link.full_link)
    except:
        return HttpResponseNotFound(f"Cant GET {short_hash}.")


def shortener(request):
    """url in request body hashing in 8 chars and return with response in json"""
    if request.method == 'POST':
        url = decode_request_body(request)
        url = check_http_or_https(url)
        json = {'url': check_url_in_bd_or_hash(url)}
        return JsonResponse(json)
    return HttpResponseNotFound('Error, GET method')
