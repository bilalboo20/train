from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('index/', views.home_page,name='index'),
    path('AIdetales/', views.AIdetales, name='AIdetales'),
    path('AIbad/', views.AIbad, name='AIbad'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about_us, name='about_us'),

]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
