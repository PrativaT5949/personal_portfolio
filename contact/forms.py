from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Check if all fields are filled
        if not name or not email or not message:
            return HttpResponse("Please fill all fields.", status=400)

        try:
            send_mail(
                subject=f"New Message from {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,  
                recipient_list=['prativarender@gmail.com'],  
                fail_silently=False,
                reply_to=[email],  
            )
            return HttpResponse("Email sent successfully!")
        except Exception as e:
           
            return HttpResponse(f"An error occurred: {e}", status=500)

    return render(request, "contact.html")
