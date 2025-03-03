from django.shortcuts import redirect, render

from .forms import SignupForm

# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SignupForm()

    return render(request, "signup_form.html", {"form": form})



def success_view(request):
    return render(request, "success.html")