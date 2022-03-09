# from django.contrib import admin
from django.urls import path
from . import views

app_name='fbv_app1'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.retrive_view, name='retrive_view'),
    path('create/',views.create_view, name='create_view'),
    path('delete/<id>',views.delete_view, name='delete_view'),
    path('update/<id>',views.update_view, name='update_view'),
]