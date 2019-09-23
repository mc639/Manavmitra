from django.shortcuts import render
from django.http import Http404
from .models import Blog, Category, Epaper, Trailer
# -*- coding: utf-8 -*-
# Create your views here.


def index(request):
    categories = Category.objects.all()
    gujarat_news = Blog.objects.filter(category__slug='gujarat').order_by('-pk')[:4]
    national_news = Blog.objects.filter(category__slug='national').order_by('-pk')[:4]
    international_news = Blog.objects.filter(category__slug='international').order_by('-pk')[:4]
    sports_news = Blog.objects.filter(category__slug='sports').order_by('-pk')[:4]
    bollywood_news = Blog.objects.filter(category__slug='bollywood').last()
    breaking_news = Blog.objects.filter().order_by('-pk')[:10]
    latest_news = Blog.objects.filter().order_by('-pk')[:2]
    trailer = Trailer.objects.filter(trailer_name__startswith="Bollywood").order_by("-pk")[:2]
    trailerSports = Trailer.objects.filter(trailer_name__startswith="Sports").order_by("-pk")[:2]
    context = {'breaking_news': breaking_news, 'latest_news': latest_news, 'categories': categories, 'trailer': trailer,
               'trailerSports': trailerSports,'gujarat': gujarat_news, 'national': national_news,
               'international': international_news, 'sports': sports_news, 'bollywood': bollywood_news}
    return render(request, 'hindi/html/index.html', context)


def post(request, slug):
    try:
        categories = Category.objects.all()
        npost = Blog.objects.get(slug=slug)
        breaking_news = Blog.objects.filter().order_by('-pk')[:10]
        latest_news = Blog.objects.filter().order_by('-pk')[:2]
        context = {'x': npost, 'breaking_news': breaking_news, 'latest_news': latest_news, 'categories': categories,}
    except Blog.DoesNotExist:
        raise Http404("Oops! Post Not Found..!!")
    return render(request, 'hindi/html/post.html', context)


def allpost(request):
    try:
        categories = Category.objects.all()
        npost = Blog.objects.all()
        breaking_news = Blog.objects.filter().order_by('-pk')[:10]
        latest_news = Blog.objects.filter().order_by('-pk')[:2]
        context = {'posts': npost, 'breaking_news': breaking_news, 'latest_news': latest_news, 'categories': categories,}
    except Blog.DoesNotExist:
        raise Http404("Oops! Post Not Found..!!")
    return render(request, 'hindi/html/allpost.html', context)


def category(request, slug):
    try:
        categories = Category.objects.all()
        get_category_name = Category.objects.get(slug=slug)
        get_category = Blog.objects.filter(category=Category.objects.get(slug=slug))
        breaking_news = Blog.objects.filter().order_by('-pk')[:10]
        latest_news = Blog.objects.filter().order_by('-pk')[:2]
        context = {'posts': get_category, "category_name": get_category_name,
                   'latest_news': latest_news, 'breaking_news': breaking_news, 'categories': categories,}
    except Category.DoesNotExist:
        raise Http404("Oops! Category Not Found..!!")
    return render(request, 'hindi/html/category.html', context)


def epaper_main(request):
    categories = Category.objects.all()
    pdf = Epaper.objects.filter().order_by('-date')
    latest_news = Blog.objects.filter().order_by('-pk')[:2]
    context = {
        'pdf': pdf,
        'latest_news': latest_news,
        'categories': categories,
    }
    return render(request, 'hindi/html/epaper_main.html', context)


def epaper(request, name):
    try:
        categories = Category.objects.all()
        pdf = Epaper.objects.get(e_paper_name=name)
        latest_news = Blog.objects.filter().order_by('-pk')[:2]
        context = {
            'paper': pdf,
            'latest_news': latest_news,
            'categories': categories
        }
    except Epaper.DoesNotExist:
        raise Http404
    return render(request, 'hindi/html/epaper.html', context)


def aboutus(request):
    categories = Category.objects.all()
    latest_news = Blog.objects.filter().order_by('-pk')[:2]
    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    return render(request, 'hindi/html/aboutus.html', context)


def my_custom_bad_request_view(request):
    categories = Category.objects.all()
    latest_news = Blog.objects.filter().order_by('-pk')[:2]
    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    return render(request, 'hindi/html/400.html', context)


def my_custom_permission_denied_view(request):
    categories = Category.objects.all()
    latest_news = Blog.objects.filter().order_by('-pk')[:2]
    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    render(request, 'hindi/html/403.html', context)


def my_custom_page_not_found_view(request):
    categories = Category.objects.all()
    latest_news = Blog.objects.filter().order_by('-pk')[:2]
    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    return render(request, 'hindi/html/404.html', context)


def my_custom_error_view(request):
    categories = Category.objects.all()
    latest_news = Blog.objects.filter().order_by('-pk')[:2]
    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    return render(request, 'hindi/html/500.html', context)
