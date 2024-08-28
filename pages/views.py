from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_vaild():
            name = form.cleaned_data["name"]
            email_form = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                "Email from " + name, message, email_form, ["daisha05311994@gmail.com"]
            )
        else:
            print("Invalid Form")

        print("Post....")
    else:
        print("GET....")
        form = ContactForm()

    return render (request, "pages/contact.html", {"form": form})