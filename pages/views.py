from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    # validate post
    if request.method == 'POST':
        # passing data to regForm var
        regForm = UserCreationForm(request.POST)
        # if data is valid, save and show message
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User has been registered')
            redirect('home')
        # if not then show error message
        else:
            messages.success(request, 'Something went wrong. Try Again !')
    return render(request, 'registration/register.html', {'form':UserCreationForm})