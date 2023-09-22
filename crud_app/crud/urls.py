from django.urls import path
from . import views



app_name = "crud"
urlpatterns = [

    # 一覧
    path("", views.ProductListView.as_view(), name="list"),
    path('new/', views.ProductCreateView.as_view(), name='new'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
]
