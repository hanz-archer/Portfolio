from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

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
    else:
        form = ContactForm()

    return render(request, 'myapp/home.html', {'form': form})
