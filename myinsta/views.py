from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import login_required
from myinsta.forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all().order_by('-id')
    users = Profile.objects.all()
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = CommentForm()
    return render(request, 'index.html',{'posts':posts, 'users':users, 'form':form})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile, })


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'update_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def add_post(request): 
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            posts = post_form.save(commit=False)
            posts.user = current_user 
            posts.save()
        return HttpResponseRedirect('/')
    else:
        post_form = PostForm()  
    return render(request,'add_post.html', {'post_form':post_form})    

@login_required
def comments(request,post_id):
  form = CommentForm()
  post = Post.objects.filter(pk = post_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.post = post
      comment.save() 
  return redirect('index')
     
