from itertools import groupby
from django.shortcuts import render
from app.models import Service, Project, Faq, WareHouse, BlogPost, Statistic


def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    posts = BlogPost.objects.all()
    main_statistic = Statistic.objects.filter(main_page=True).first()
    context = {
        'services': services,
        'projects': projects,
        'posts': posts,
        'statistic': main_statistic
    }
    return render(request, 'index/index.html', context)


def terms(request):
    return render(request, 'index/terms.html')


def solutions(request):
    return render(request, 'index/solutions.html')


def privacy_policy(request):
    return render(request, 'index/privacy-policy.html')


def warehouse(request):
    warehouses = WareHouse.objects.all()
    context = {
        'warehouses': warehouses
    }
    return render(request, 'index/warehouse.html', context=context)


def about(request):
    services = Service.objects.all()
    statistics = Statistic.objects.all()
    projects = Project.objects.all()
    context = {
        'services': services,
        'statistics': statistics,
        'projects': projects
    }
    return render(request, 'index/about.html', context)


def faq(request):
    faqs = Faq.objects.exclude(category="global").order_by('category').all()
    grouped_faqs = {category: list(faq_list) for category, faq_list in groupby(faqs, key=lambda x: x.category)}

    result_dict = {"faq": grouped_faqs}
    global_faq = Faq.objects.filter(category="global").all()

    context = {
        'result_dict': result_dict,
        'global_faq': global_faq
    }

    return render(request, 'index/faq.html', context=context)

