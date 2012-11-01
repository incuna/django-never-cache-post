from django.utils.cache import add_never_cache_headers, patch_cache_control


class NeverCachePostMiddleware(object):
    def process_response(self, request, response):
        if request.POST:
            add_never_cache_headers(response)
            patch_cache_control(response, no_cache=True)
        return response
