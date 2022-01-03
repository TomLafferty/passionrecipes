"""
Render html web pages
"""

from django.http import HttpResponse



def home_view(request):

    HTML_STRING = """
    <h1>Cook Book Home</h1>
    """
    return HttpResponse(HTML_STRING)