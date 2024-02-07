from django import forms 
from .models import Product, Category, Profile, Offer, Payment, Bank, Banks, Blog_cat, Blog

choices= Category.objects.values_list('name', 'name')
choice_list= []

for item in choices:
    choice_list.append(item)

blog_cats= Blog_cat.objects.values_list('name', 'name')
cat_list= []

for cat in blog_cats:
    cat_list.append(cat)

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= ('image', 'name', 'description', 'price', 'category', 'commission')

        widgets= {
            'category': forms.Select(choices= choice_list)
        }

        def get_absolute_url(self):
            return reverse('home')

class ProductEdit(forms.ModelForm):
    class Meta:
        model= Product
        fields= ('image','name', 'description', 'price', 'category', 'commission')

        widgets= {
            'category': forms.Select(choices= choice_list)
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields= ('image', 'title', 'description', 'category')

        widgets= {
            'category': forms.Select(choices= cat_list)
        }

        def get_absolute_url(self):
            return reverse('home')

class BlogEdit(forms.ModelForm):
    class Meta:
        model= Blog
        fields= ('image', 'title', 'description', 'category')

        widgets= {
            'category': forms.Select(choices= cat_list)
        }
