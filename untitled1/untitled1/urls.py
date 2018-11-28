"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('register', views.register, name="register"),

    path('view_property', views.view_property, name="view_property"),

    path('admin_portal/', views.list_user, name='admin_portal'),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('admin_portal/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('admin_portal/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',
    auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('admin_portal/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    path('admin_portal/add_user/', views.add_user, name='add_user'),
    path('admin_portal/list_userrole/', views.list_userrole, name='list_userrole'),
    path('admin_portal/manage_role/', views.manage_role, name='manage_role'),
    path('admin_portal/edit_user/<int:pk>', views.edit_user, name='edit_user'),
    path('admin_portal/delete_user/<int:pk>', views.delete_user, name='delete_user'),
    path('admin_portal/delete_userrole/<int:pk>', views.delete_userrole, name='delete_userrole'),
    path('admin_portal/list_user/', views.list_user, name='list_user'),

    path('admin_portal/add_role/', views.add_role, name='add_role'),
    path('admin_portal/edit_role/<int:pk>', views.edit_role, name='edit_role'),
    path('admin_portal/delete_role/<int:pk>', views.delete_role, name='delete_role'),
    path('admin_portal/list_role/', views.list_role, name='list_role'),

    path('admin_portal/add_feature/', views.add_feature, name='add_feature'),
    path('admin_portal/assign_feature/', views.assign_feature, name='assign_feature'),
    path('admin_portal/import_feature/', views.import_feature, name='import_feature'),
    path('admin_portal/edit_feature/<int:pk>', views.edit_feature, name='edit_feature'),
    path('admin_portal/delete_feature/<int:pk>', views.delete_feature, name='delete_feature'),
    path('admin_portal/delete_assignfeatures/<int:pk>', views.delete_assignfeatures, name='delete_assignfeatures'),
    path('admin_portal/list_feature/', views.list_feature, name='list_feature'),
    path('admin_portal/list_assignfeatures/', views.list_assignfeatures, name='list_assignfeatures'),

]
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


