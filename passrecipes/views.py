"""
Render html web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string


def home_view(request, *args, **kwargs):

    # HTML_STRING = """
    # <h1>Cook Book Home</h1>
    # """
    HTML_STRING = render_to_string("home-view.html")
    return HttpResponse(HTML_STRING)