from decouple import config
from django.http import HttpResponseForbidden


class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        at = request.headers.get('API-TOKEN')
        if not at or at != config('CONST_TOKEN'):
            return HttpResponseForbidden("You are not allowed to use this profile.")
        response = self.get_response(request)
        return response
