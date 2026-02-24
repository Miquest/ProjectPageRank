from django.http import HttpRequest, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from crawler.models import PageKeyword, Keyword, WebPage


class TestView(APIView):

    def get(self, request: HttpRequest):
        return HttpResponse("Hello world from searchy!")


class KeywordSearch(APIView):

    # Small helper function
    @staticmethod
    def db_to_json(page: WebPage):
        return {
            "url": page.url,
            "title": page.title,
            "content": page.content[:200] if page.content is not None else "",
            "last_crawl": page.last_crawled,
            "score": page.pagerank_score
        }

    def get(self, request: HttpRequest):
        keyword = request.GET.get("search", "")
        keyword_entity = Keyword.objects.filter(word=keyword).first()
        pages = PageKeyword.objects.filter(keyword=keyword_entity).all()

        response_list = []

        for page in pages:
            print(page.page.pk)
            response_list.append(self.db_to_json(WebPage.objects.get(pk=page.page.pk)))

        response_list = sorted(response_list, key=lambda x: 5 if keyword in x["url"] else 0, reverse=True)

        return HttpResponse(JSONRenderer().render(response_list), content_type="application/json")
