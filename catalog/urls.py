from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactView, IndexView, ProductsListView, ProductsCreateView, ProductsDetailView, \
    ProductsUpdateView, ProductDeleteView, BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/create/', ProductsCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='view_product'),
    path('update/<int:pk>/', ProductsUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='read_blog'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog')
    ]