from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse(
        '<html>'
        '<body>'
        
        '<div>'
        '<p>published: 12.11.2019, 14:38</p>'
        '<h2><a href="">My First post</h2>'
        '<p>asdasd</p>'
        '</div>'
        
        '<div>'
        '<p>published: 12.11.2019, 14:39</p>'
        '<h2><a href="">My Second post</h2>'
        '<p>asdasdasd</p>'
        '</div>'
        
        '</body>'
        '</html>'
    )

