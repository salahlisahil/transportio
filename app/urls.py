from django.urls import path

import app.views as view

urlpatterns = [
    path('', view.index, name='index'),
    path('contact/', view.ContactView.as_view(), name='contact'),
    path('subscribe/', view.subscribe, name='subscribe'),
    path('about/', view.about, name='about'),
    path('service/<int:service_id>/', view.service_detail, name='service_detail'),
    path('project/<int:project_id>/', view.project_detail, name='project_detail'),
    path('terms/', view.terms, name='terms'),
    path('solutions/', view.solutions, name='solutions'),
    path('privacy-policy/', view.privacy_policy, name='privacy_policy'),
    path('faq/', view.faq, name='faq'),
    path('warehouse/', view.warehouse, name='warehouse'),
    path('tracking/', view.TrackingView.as_view(), name='tracking'),
    path('post/<int:post_id>/', view.PostDetailView.as_view(), name='post_detail'),
]