"""To render html web page"""

from django.http import HttpResponse

HTML_STRING = """<h1>Hello World</h1>"""


def home_view(request):
    """Take request and return HTML response"""
    return HttpResponse(HTML_STRING)
