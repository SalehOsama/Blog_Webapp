from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        fm = UserRegisterForm(request.POST)       # creates a form with data
        if fm.is_valid():
            fm.save()        # Saves the data in a database
            
            username = fm.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in')

            return redirect('login')
    
    else:
        fm = UserRegisterForm()                      # creates an empty form

    return render(request,'users/register.html', {'form': fm})



# profile view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your Profile has been Updated!') 
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request,'users/profile.html', context)
    