from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),

    path('', admin.site.urls),
]
