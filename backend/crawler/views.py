from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView


class TestView(APIView):

    def get(self, request: HttpRequest):

        return HttpResponse("Hello world from crawly!")