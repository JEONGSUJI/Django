import os
from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    # 상위 폴더(blog)의 상위폴더(djangogirls)의 하위폴더(templates)의 하위파일(post_list.html) 내용을
    # read()한 결과를 HttpResponse에 인자로 전달

    # 경로 이동
    # os.path.abspath(__file__) <- 현재 파일의 절대 경로 리턴
    # os.path.dirname
        # 한단계 위로 가는 것
    # os.path.join
        # os.path.join(r'c:\temp', 'hello.exe')
        # ('c:\\temp\\python', 'data.txt')

    # 파일 열기
    # open

    cur_file_path = os.path.abspath(__file__)
    blog_dir_path = os.path.dirname(cur_file_path)
    root_dir_path = os.path.dirname(blog_dir_path)
    templates_dir_path = os.path.join(root_dir_path, 'templates')
    post_list_html_path = os.path.join(templates_dir_path,'post_list.html')
    print('result: ', post_list_html_path)

    f = open(post_list_html_path, 'rt')
    html = f.read()
    f.close()

    # with open(result, 'r') as html:
    #     return HttpResponse(html)

    return HttpResponse(html)