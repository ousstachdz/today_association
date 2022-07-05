from django.urls import path
from . import views


urlpatterns = [

    # public urls
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    
    #auth urls
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('second_page_register',views.second_page_register,name='second_page_register'),
    path('complet_page_register',views.complet_page_register,name='complet_page_register'),
    path('logout',views.logout,name='logout'),

    #admin urls
    path('dashbord',views.dashbord,name='dashbord'),
    path('add_post',views.add_post,name='add_post'),

    # numbers urls
    path('profil',views.profil,name='profil'),
    path('postes',views.postes,name='postes'),
    path('post_details/<str:pk>',views.post_details,name='post_details'),
]
