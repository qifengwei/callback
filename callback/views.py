import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def callback(request):
    print(request.method)
    print(request.body)
    response = HttpResponse()
    res = json.dumps({"code": 0}, ensure_ascii=False)
    response.content = res
    return response
