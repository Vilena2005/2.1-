from django.urls import path

from .views import index_page, register, dashboard, logout_view, login_view, admin_dashboard

urlpatterns = [
    path('', index_page, name='index_page'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
path('admin/', admin_dashboard, name='admin_dashboard'),
]
