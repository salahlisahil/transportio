from app.models import Service


def global_variables(request):
    services = Service.objects.all()

    context = {
        'footer_services': services
    }

    return context
