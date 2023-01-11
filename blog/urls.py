from django.contrib import admin
from django.urls import path
from blog.views import CategoryListView, PostByCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
]