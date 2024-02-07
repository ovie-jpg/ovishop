from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name= "home"),
    path('<str:ref_by>', views.home, name= "home"),
    path('search/', views.search, name= "search"),
    path('search/<str:ref_by>', views.search, name= "search"),
    path('info/<int:pk>', views.info, name= "info"),
    path('add-product/', views.AddProduct.as_view(), name= "add-product"),
    path('edit-product/<int:pk>', views.EditProduct.as_view(), name= "edit-product"),
    path('delete-product/<int:pk>', views.DelProduct.as_view(), name= "delete-product"),
    path('info/<int:pk>/offer-info/<str:perc>', views.offer_info, name= "offer-info"),
    path('add-offer/', views.AddOffer.as_view(), name= "add-offer"),
    path('edit-offer/<int:pk>', views.EditOffer.as_view(), name= "edit-offer"),
    path('delete-offer/<int:pk>', views.DelOffer.as_view(), name= "delete-offer"),
    path('profile/', views.profile, name= "profile"),
    path('profile-edit/<int:pk>', views.ProfileEdit.as_view(), name= "profile-edit"),
    path('add-cat/', views.AddCat.as_view(), name= "add-cat"),
    path('edit-cat/', views.EditCat.as_view(), name= "edit-cat"),
    path('delete-cat/', views.DelCat.as_view(), name= "delete-cat"),
    path('trans-hist/', views.transaction_history, name="trans-hist"),
    path('make-payment/', views.make_payment, name= "make-payment"),
    path('init-payment/<int:pk>', views.initialize_payment, name= "init-payment"),
    path('verify-payment/<str:ref>', views.verify_payment, name= "verify-payment"),
    path('blog-page/', views.blog_page, name= "blog-page"),
    path('add-blog/', views.AddBlog.as_view(), name= "add-blog"),
    path('edit-blog/<int:pk>', views.EditBlog.as_view(), name= "edit-blog"),
    path('del-blog/<int:pk>', views.DelBlog.as_view(), name= "del-blog"),
    path('post-detail/<int:pk>', views.post_details, name= "post-detail"),
    path('add-blogcat/', views.AddBlogCat.as_view(), name= "add-blogcat"),
    path('del-blogcat/<int:pk>', views.DelBlogCat.as_view(), name= "del-blogcat")
]