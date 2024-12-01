from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static 


urlpatterns = [
    path('', views.home,  name='home'),

    path('product/<int:id>/', views.product, name='product'),

    path('about/', views.about, name='about'),
    
    path('new/', views.new, name='new'),

    path('google03bd2b58a927019e.html/', views.googleVerify, name='googleVerify'),

]  
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)