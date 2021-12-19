import time

from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()

        RequestResponseLog.objects.create(
            path=request.path,
            request_method=request.method,
            response_time=(end - start),
        )

        return response
