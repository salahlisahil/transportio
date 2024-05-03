from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from app.forms import ContactForm


class ContactView(View):
    template_name = 'contact/contact.html'

    def get(self, request):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']

            subject = f"Message from {fullname}, Comes from ContactForm"
            message = f""""Fullname: {fullname}, Email: {email}, Mobile: {mobile}, Company: {company}
            Message: {message}"""

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)
            except Exception as e:
                messages.error(request, 'Your message has not been sent!')
                return redirect('contact')

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')

        return render(request, self.template_name)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            send_mail('Subscription', f'You have successfully subscribed!', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)
        except Exception as e:
            messages.error(request, 'An error occurred, try again!')
            return redirect('index')

        messages.success(request, 'You have successfully subscribed!')
        return redirect('index')

    return redirect('index')

