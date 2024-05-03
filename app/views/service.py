from django.shortcuts import render, get_object_or_404
from app.models import Service


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    services = Service.objects.all()
    benefits = service.benefits.split(',')

    context = {
        'service': service,
        'services': services,
        'benefits': benefits
    }
    return render(request, 'service/service-detail.html', context=context)