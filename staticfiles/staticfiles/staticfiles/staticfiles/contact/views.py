from django.shortcuts import render, redirect
from .models import Contact


def contact_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email_address')
        phone = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Optional: You can add basic validation here
        if fullname and email and message:
            # Save data to the database
            Contact.objects.create(
                fullname=fullname,
                email_address=email,
                phone_number=phone if phone else 'N/A',
                message=message
            )
            # Redirect to a success page or render a success message
            # You should define this URL/view
            return redirect('contact:success')
        else:
            # Return error message if needed
            return render(request, "contact.html", {"error": "Please fill all required fields."})
    else:
        return render(request, "contact.html")


def success_view(request):
    return render(request, "contact/success.html")
def index(request):
    return render(request, 'contact/index.html')