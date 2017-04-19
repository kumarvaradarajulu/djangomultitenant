import threading


thread_local_data = threading.local()


class MultiTenant(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_code = request.META.get('HTTP_TENANT_CODE', 'default')
        setattr(thread_local_data, 'tenant_code', tenant_code)
        response = self.get_response(request)
        return response
