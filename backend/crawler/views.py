from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .crawler import Crawler


class TestView(APIView):

    def get(self, request: HttpRequest):

        return HttpResponse("Hello world from crawly!")


class Crawl(APIView):

    def get(self, request: HttpRequest):

        crawler = Crawler("https://azure.microsoft.com/de-de/resources/cloud-computing-dictionary/what-is-java-programming-language")
        crawler.crawl(50)

        return HttpResponse(JSONRenderer().render({}), content_type="application/json")