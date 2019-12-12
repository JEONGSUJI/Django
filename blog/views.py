import os
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

def post_list(request):
    # Template를 찾을 경로에서 post_list.html을 찾아서
    # 그 파일을 text로 만들어서 HttpResponse 형태로 돌려준다.
    # 위 기능을 하는 shortcut 함수

    # 1. posts라는 변수에 전체 Post를 가지는 QuerySet 객체를 할당
    #   hint) Post.objects.무언가... 를 실행한 결과는 QuerySet 객체가 된다.
    # 2. context라는 dict를 생성하며, 'post'키에 위에 posts변수를 value로 사용하도록 한다.
    # 3. render의 3번째 위치인자로 위 context 변수를 전달한다.

    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'post_list.html', context)

def post_detail(request):
    # URL: /post-detail/
    # View: post_detail
    # Template: post_detail.html
    # 내용으로 <h1>Post Detail!</h1>을 갖도록 함

    # 1. 전체 Post목록(Post 전체 QuerySet) 중 [0]번 index에 해당하는 Post객체 하나를 post 변수에 할당
    # 2. 'context'라는 이름의 dict 만들기, 'post' key에 위 post변수를 value로 사용한다.
    # 3. 이 context 변수를 render의 3번째 인자로 전달
    # 4. post_detail.html에서는 전달받은 'post' 변수의 title, author, text, created_date, published_date를 적절히 출력한다.

    post = Post.objects.all()[3]
    context = {'post': post}

    return render(request, 'post_detail.html', context)