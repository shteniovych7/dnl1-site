from django.shortcuts import render
from news.models import Article
from django.core.paginator import Paginator


def allnews(request):

    articles = Article.objects.all().order_by('-date')
    paginator = Paginator(articles,6)
    page = request.GET.get('page')

    articles = paginator.get_page(page)

    return render(request, 'news/allnews.html', {'articles' : articles})