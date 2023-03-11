from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, ProductDemo, Book
from .forms import ContactForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def Homepage(request):
    # variable = Table.objects.method()
    # Query All Posts
    all_posts = Post.objects.all()
    return render(request, 'company/home.html', {'all_posts': all_posts})

def about(request):
    data = ProductDemo.objects.all()
    context = {'data': data} # attachment
    return render(request, 'company/about.html', context)

def product(request):
    data = ProductDemo.objects.all()
    context = {'data': data} # attachment
    return render(request, 'company/product.html', context)
# EP6 Week5
def post_detail(request, id):
    single_post = Post.objects.get(id=id)
    return render(request, 'company/post-detail.html', {'single_post': single_post})
#EP7
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB
            form.save()
            return redirect("/")
    else:
        form = ContactForm()
    return render(request, 'company/contact.html', {'form': form})

def search(request):
    # get the query from the search form (get the incoming query params)
    search_post = request.GET.get('q')  # q is the name of the input field in the search form, First GET is a method, second is the name 
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post))
    else:
        pass
    return render(request, 'company/search.html', {'posts': posts})

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            # Log user in
            login(request, user)
            return redirect('/admin')
        messages.error(request, 'Invalid login')

    return render(request, 'company/sign-in.html')

def sign_out(request):
    # Sign user out
    logout(request)
    return redirect('/sign-in')

@login_required
def addbook(request):
    if request.method == 'POST':
        data = request.POST.copy()
        book_title = data.get('book_title') # get the book title from the form HTML name="book_title"   
        book_description = data.get('book_description')
        book_price = data.get('book_price')

        newbook = Book()
        newbook.title = book_title
        newbook.description = book_description
        newbook.price = float(book_price)
        newbook.save()

    return render(request, 'company/addbook.html')

