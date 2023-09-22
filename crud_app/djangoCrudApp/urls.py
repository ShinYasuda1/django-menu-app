from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # CRUD追加
    path('crud/', include('crud.urls')),
]
