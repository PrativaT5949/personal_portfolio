from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
import os

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"New Message from {name}",
            message=message,
            from_email=DEFAULT_FROM_EMAIL,          # SendGrid verified email
            recipient_list=['prativat5949@gmail.com'],  # where you want to receive emails
            fail_silently=False,
            reply_to=[email],  # visitor can be replied directly
        )
        return HttpResponse("Email sent successfully!")
    return render(request, "contact.html")
