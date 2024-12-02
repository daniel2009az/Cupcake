from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static 


urlpatterns = [
    path('', views.home,  name='home'),

    path('product/<int:id>/', views.product, name='product'),

    path('about/', views.about, name='about'),
    
    path('new/', views.new, name='new'),

    path('login/', views.login_user, name='login'),
   
    path('logout/', views.logout_user, name='logout'),

    path('register/', views.register_user, name='register'),

    path('category/<str:foo>', views.category, name='category'),
    
    path('google03bd2b58a927019e.html/', views.googleVerify, name='googleVerify'),
    
]  
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)