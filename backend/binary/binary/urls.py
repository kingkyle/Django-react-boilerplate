
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
