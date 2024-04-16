from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .mail import send_email
from django.contrib.auth import get_user_model, login


# import django auth views to add context menu
from django.contrib.auth.views import LoginView

# Create your views here.

# Login view not technically needed but need it for the context menu
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('')
                else:
                    # Invalid password
                    form.add_error(None, "Invalid email or password")
            except User.DoesNotExist:
                # Invalid email
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()

    extra_context = {
        'title': 'Hamco IS',
        'company': 'Hamco Internet Solutions',
        'form': form,
    }
    return render(request, 'registration/login.html', extra_context)

# Custom registration view
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Send a welcome email
            from_email = "art@hamcois.com"
            from_name = "Art Mills"
            to_email = user.email
            subject = "Welcome to Hamco Internet Solutions"
            text_content = "Thank you for registering."
            html_content = "<h3>Thank you for registering.</h3>"
            send_email(from_email, from_name, to_email, subject, text_content, html_content)
            
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
