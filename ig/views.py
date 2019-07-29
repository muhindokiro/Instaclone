from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .models import Pic
from .forms import NewPicForm
# from django.contrib.auth import authenticate,get_user_model,login,logout
# from .forms import UserLoginForm,UserSignUpForm 


# Create your views. 
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def timeline(request):
    return render(request, 'timeline.html')

def profile(request):
    return render(request, 'profile.html')

# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request,user)
#         if next:
#             return redirect(next)
#         return redirect('/')

#     context = {
#         'form': form,
#     }

#     return render(request, 'timeline.html',context)

@login_required(login_url='/accounts/login/')
def new_pic(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPicForm(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.save()
        return redirect('')

    else:
        form = NewPicForm()
    return render(request, 'timeline.html', {"form": form})