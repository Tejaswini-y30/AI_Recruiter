from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('', views.index, name='index.html'),
    path('adminlogin', views.adminlogin),
    path('studentform', views.studentform),
    path('form_submitted', views.form_submitted, name='form_submitted'),
    path('msg', views.msg, name='msg'),
    path('msg1', views.msg1, name='msg1'),
    path('msg2', views.msg2, name='msg2'),
    path('success', views.index, name='index.html'),
    path('logout', views.adminlogin),
    path('admin', views.admin, name='admin')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)