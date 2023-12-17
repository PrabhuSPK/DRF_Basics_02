from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#API policy decorators
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

# Create your views here.

#index page
@api_view()
def index(request):
    return Response({"message": "Hello World!"})

#GET & POST
@api_view(['GET','POST'])
def index2(request):
    if request.method == 'POST':
        return Response({"message": "This is post method","data": request.data})
    return Response({"message":"Hello World!"})

#throttle times
class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

#throttle function
@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def throttle(request):
    return Response({"message" : "Hello for today! See you tomorrow!"})

from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        pass
        # override view introspection here...

@api_view(['GET'])
@schema(CustomAutoSchema())
def schema(request):
    return Response({"message": "Hello for today! See you tomorrow!"})