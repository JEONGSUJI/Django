import os
from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    # Template를 찾을 경로에서 post_list.html을 찾아서
    # 그 파일을 text로 만들어서 HttpResponse 형태로 돌려준다.
    # 위 기능을 하는 shortcut 함수
    return render(request, 'post_list.html')