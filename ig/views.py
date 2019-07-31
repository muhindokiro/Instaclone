from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Post
from .forms import NewArticleForm,NewsLetterForm,RegisterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def ig_today(request):
    ig = Post.todays_ig()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            send_welcome_email(name,email)
            HttpResponseRedirect('ig_today')
    else:
        form = NewsLetterForm()
    return render(request, 'all-posts/today-ig.html', {"ig":ig,"letterForm":form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Post.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'all-posts/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})




@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('igToday')

    else:
        form = NewArticleForm()
    return render(request, 'new_post.html', {"form": form})

def register(request):
   if request.method == "POST":
       form = UserRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           email = form.cleaned_data['email']
           send_welcome_email(username,email)
           return redirect('all_posts/today_ig.html')
   else:
       form =RegisterForm()
   return render(request,'registration/registration_form.html',{'form':form})
  

