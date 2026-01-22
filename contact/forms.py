from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact   # make sure model exists

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            return HttpResponse("Please fill all fields.", status=400)

        # save to database only
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return HttpResponse("Message sent successfully!")

    return render(request, "contact/contact.html")
