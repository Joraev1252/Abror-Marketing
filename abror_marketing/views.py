from django.shortcuts import render
from abror_marketing.models import BusinessSmmModel, TargetingModel, LogoRoleModel, OurProjectsModel, ContactModel, CarouselModel, CategoriesModels, ServicesModel, MainLogoModel


def abror_view(request):
    context = {}
    business = BusinessSmmModel.objects.all()
    target = TargetingModel.objects.all()
    logo = LogoRoleModel.objects.all()
    main_logo = MainLogoModel.objects.all()
    projects = OurProjectsModel.objects.all()
    contact = ContactModel.objects.all()
    carousel = CarouselModel.objects.all()
    categories = CategoriesModels.objects.all()
    services = ServicesModel.objects.all()
    context['business'] = business
    context['target'] = target
    context['logo'] = logo
    context['projects'] = projects
    context['contact'] = contact
    context['carousel'] = carousel
    context['categories'] = categories
    context['services'] = services
    context['main_logo'] = main_logo
    print(context['carousel'])
    a = (len(context['carousel']))
    context['carousel_count'] = a

    return render(request, 'index.html', context)
#
#
# def target_view(request):
#     context = {}
#     target = TargetingModel.objects.all()
#     context['target'] = target
#
#     return render(request, 'index.html', context)
#
#
# def logo_view(request):
#     context = {}
#     logo = LogoRoleModel.objects.all()
#     context['logo'] = logo
#
#     return render(request, 'index.html', context)
#
#
# def projects_view(request):
#     context = {}
#     projects = OurProjectsModel.objects.all()
#     context['projects'] = projects
#
#     return render(request, 'index.html', context)
#
#
# def contact_view(request):
#     context = {}
#     contact = ContactModel.objects.all()
#     context['contact'] = contact
#
#     return render(request, 'index.html', context)
#
