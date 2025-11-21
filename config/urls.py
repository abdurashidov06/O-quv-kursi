
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('education.urls')),
    path('about', include('about.urls')),
    path('account', include('account.urls')),

]
