from django.shortcuts import render, redirect
from .models import Post
from .forms import ContactForm
from .forms import RegisterFrom
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    all_posts = Post.objects.all()    
    
    context = {
        'posts': all_posts
    }
    return render(request, 'blog/home.html', context)

@login_required(login_url='sign_in')
def post_detail(request,post_id):
    sigle_post = Post.objects.get(id=1)
    return render(request,'blog/post_detail.html', {'post': sigle_post})

def contact(request):
    form = ContactForm(request.POST)
    if form. is_valid():
        form.save()
        return redirect('/')
    else:
        form = ContactForm()
        print("ฟอร์มถูกส่งเรียบร้อย")
        print(form)
        
    return render(request, 'blog/contact.html', {'form': form})

def register(request):
    form = RegisterFrom
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            print("สมัครสมาชิกเรียบร้อย")
            return redirect("home")
    else:
        form = RegisterFrom()
        print("แสดงฟอร์มเรียบร้อย")
 
    return render(request, 'blog/register.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print('Login complete')
            return redirect("home")
        else:
        # Return an
            print('ยังไม่ได้')
    return render(request, 'blog/login.html')

def sign_out(request):
    logout(request)# Redirect to a success page.
    return redirect("home")
    