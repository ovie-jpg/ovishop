from django.shortcuts import render, redirect
from .models import Product, Category, Profile, Offer, Payment, Bank, Banks, Blog_cat, Blog
import uuid
from datetime import date
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm, ProductEdit, BlogForm, BlogEdit
from django.urls import reverse
import requests
from decimal import Decimal
from django.contrib import messages

# Create your views here.

def home(request, **kwargs):
    ref_by= str(kwargs.get("ref_by"))
    products= Product.objects.all()
    
    context= {
        'products': products,
        'ref_by': ref_by
    }
    return render(request, 'home.html', context)

def info(request, pk):
    product= Product.objects.get(pk=pk)
    ref= str(uuid.uuid4()).replace("-", "")[:7]
    offers= Offer.objects.all()
    offer= ''
    today= date.today()

    if Offer.objects.filter(product=product).exists():
        offer= Offer.objects.get(product=product)
        product.discount= product.price - (offer.discount_percentage/100 * product.price)
        product.save()
    elif Offer.objects.filter(product=product).exists() == False:
        product.discount= None
        product.save()

    if offer != '' and offer.valid_till == today:
        offer.delete()

    if request.method == 'POST':
        quantity= int(request.POST['quantity'])
        if product.discount:
            amount= product.discount*quantity
            payment= Payment.objects.create(user= request.user, product= product.name, amount= amount, ref= ref)
            return redirect('trans-hist')
        else:
            amount = product.price*quantity
            payment= Payment.objects.create(user= request.user, product= product.name, amount= amount, ref= ref)
            return redirect('trans-hist')

    context= {
        'product': product,
        'offers': offers,
        'offer': offer
    }
    return render(request, "info.html", context)

def search(request, **kwargs):
    ref_by= str(kwargs.get("ref_by"))
    search= request.GET['search']
    products= Product.objects.filter(name__icontains=search)

    context= {
        'ref_by': ref_by,
        'search': search,
        'products': products
    }
    return render(request, 'search.html', context)


def offer_info(request, pk, **kwargs):
    perc= str(kwargs.get('perc'))
    product= Product.objects.get(pk=pk)
    offer= Offer.objects.get(discount_percentage= perc)

    if request.method == 'POST':
        try:
            if product.discount:
                amount= product.discount*quantity
                payment= Payment.objects.create(user= request.user, product= product.name, amount= amount, ref= ref)
                return redirect('init-payment', payment.pk)
            else:
                amount = product.price*quantity
                payment= Payment.objects.create(user= request.user, product= product.name, amount= amount, ref= ref)
                return redirect('init-payment', payment.pk)
        except:
            messages.info(request, 'register on the website or login to purchase')
    context= {
        'product': product,
        'offer': offer
    }
    return render(request, 'offer-info.html', context)



class AddProduct(CreateView):
    model= Product
    template_name= "add-product.html"
    form_class= ProductForm

class EditProduct(UpdateView):
    model= Product
    template_name= "edit-product.html"
    form_class= ProductEdit

class DelProduct(DeleteView):
    model= Product
    template_name= "delete-product.html"
    success_url= reverse_lazy('home')

class AddOffer(CreateView):
    model= Offer
    template_name= "add-offer.html"
    fields= ('discount_percentage', 'valid_till')

class EditOffer(UpdateView):
    model= Offer
    template_name= "edit-offer.html"
    fields= ('discount_percentage', 'valid_till')

class DelOffer(DeleteView):
    model= Offer
    template_name= "delete-offer.html"
    success_url= reverse_lazy('home')

def profile(request):
    
    profile= Profile.objects.filter(user= request.user)

    context= {
        'profiles': profile
    }
    return render(request, 'profile.html', context)

class ProfileEdit(UpdateView):
    model= Profile
    template_name= "edit-profile.html"
    fields= ('image', 'telephone')

class AddCat(CreateView):
    model= Category
    template_name= "add-cat.html"
    fields= ('name',)

    def get_absolute_url(self):
        return reverse('home')

class EditCat(UpdateView):
    model= Category
    template_name= "edit-cat.html"
    fields= ('name',)

class DelCat(DeleteView):
    model= Category
    template_name= "delete-cat.html"
    success_url= reverse_lazy('home')

def make_payment(request):
    today= date.today()
    payment= Payment.objects.filter(date=today)

    context= {
        'payments': payment
    }
    return render(request, 'make_payment.html', context)

def transaction_history(request):
    payments= Payment.objects.all().order_by('-date')
    
    context= {
        'payments': payments
    }
    return render(request, 'trans-hist.html', context) 

def initialize_payment(request, pk):
    payment= Payment.objects.get(pk=pk)
    paystack_publickey= 'pk_test_0d607ce9950cf59c2862bad631607f4ac1f28a7a'

    context= {
        'payment': payment,
        'public_key': paystack_publickey
    }
    return render (request, 'init-payment.html', context)

def verify_payment(request, ref):
    payment= Payment.objects.get(ref=ref)
    paystack_secretkey= 'sk_test_abb941d36e3e441e11a16f615028ef499028f5ff'
    headers= {
        "Authorization": 'Bearer ' + paystack_secretkey,
        "Content-Type": 'application/json'
    }
    url= 'https://api.paystack.co/transaction/verify/'
    response= requests.get(url + payment.ref, headers= headers)
    res_json= response.json()
    if res_json['status'] == True:
        payment.transaction= "successful"
        payment.save()
    else:
        payment.transaction= "unsuccessful"
        payment.save()

    profile= Profile.objects.get(user= request.user)
    product= Product.objects.get(name= payment.product)
    
    if payment.transaction == "successful":
        if Profile.objects.filter(recommendations= request.user).exists() and product.commission is not None:
            ref_profile= Profile.objects.get(recommendations= request.user)
            ref_profile.earnings += product.commission/100 * payment.amount
            ref_profile.save()
         
    context= {
        'response': response.json,
        'payment': payment
    }
    return render(request, 'verify.html', context)

def blog_page(request):
    blogs= Blog.objects.all().order_by('-pub_date')
    cats= Blog_cat.objects.all()
    context= {
        'blogs': blogs,
        'cats': cats
    }
    return render(request, 'blog-page.html', context)

class AddBlog(CreateView):
    model= Blog
    template_name= "add-blog.html"
    form_class= BlogForm

class EditBlog(UpdateView):
    model= Blog
    template_name= "edit-blog.html"
    form_class= BlogEdit

class DelBlog(DeleteView):
    model= Blog
    template_name= "del-blog.html"
    success_url= reverse_lazy('home')

class AddBlogCat(CreateView):
    model= Blog_cat
    template_name= "add-blogcat.html"
    fields= '__all__'

class DelBlogCat(DeleteView):
    model= Blog_cat
    template_name= "del-blogcat.html"
    success_url= reverse_lazy('home')

def post_details(request, pk):
    blog= Blog.objects.get(pk=pk)
    cats= Blog_cat.objects.all()
    context= {
        'blog': blog,
        'cats': cats
    }
    return render(request, 'post-details.html', context)