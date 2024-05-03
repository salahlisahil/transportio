from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static

from app.models import Project


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_images = {
        'main_image': project.images.all()[0] if project.images and len(project.images.all()) > 0 else static(
            'assets/imgs/project-details-img1.jpg'),
        'right_images': project.images.all()[1] if project.images and len(project.images.all()) > 1 else static(
            'assets/imgs/project-details-img2.jpg'),
        'right_images_2': project.images.all()[2] if project.images and len(project.images.all()) > 2 else static(
            'assets/imgs/about-v3-img1.jpg'),
    }
    benefits = project.benefits.split(',')
    context = {
        'project': project,
        'project_images': project_images,
        'project_info': project.info,
        'benefits': benefits
    }
    return render(request, 'project/project-detail.html', context=context)