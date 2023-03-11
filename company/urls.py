from django.urls import path
from .views import Homepage, about, product, post_detail, contact, search, addbook, sign_in, sign_out #import path from views.py

urlpatterns = [
    # path ('URL name', function_name)
    path('', Homepage), #localhost:8000
    path('about', about),
    path('product', product),
    path('blog/<int:id>', post_detail),
    path('contact', contact),
    path('search', search),
    path('addbook', addbook),
    path('sign-in', sign_in),
    path('sign-out', sign_out)
]