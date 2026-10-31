
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello(request):
    return Response({
        "message": "Hello from CSC 325!"
    })

@api_view(["GET"])
def status(request):
    return Response({
        "status": "running"
    })
# Create your views here.
