from django.urls import path
from . import views  # . 表示当前文件夹

urlpatterns = [
    path('',views.index),#表示app的根目录
    path('new/',views.new_product)
]