from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from django.contrib import messages
from django.contrib.staticfiles import finders

# Define the contact form class
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                # Send the email
                send_mail(
                    subject,
                    f"Message from {name} <{email}>\n\n{message}",
                    email,  # Sender email (from the form input)
                    ['dalubatanhans@gmail.com'],  # Recipient email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('home')  # Redirect to home after sending
            except Exception as e:
                # Log the error if needed and show a failure message
                messages.error(request, 'An error occurred while sending your message. Please try again later.')
        else:
            messages.error(request, 'There was an error in your form. Please check the inputs and try again.')
    else:
        form = ContactForm()

    return render(request, 'myapp/home.html', {'form': form})

def download_cv(request):
    # Use Django's static file finder to locate the file in the static directory
    file_path = finders.find('myapp/documents/Hans Archer Dalubatan.pdf')

    # Check if file exists
    if file_path:
        with open(file_path, 'rb') as cv_file:
            response = HttpResponse(cv_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Hans Archer Dalubatan.pdf"'
            return response
    else:
        raise Http404("CV file not found.")

