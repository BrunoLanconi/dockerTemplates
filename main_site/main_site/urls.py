from django.contrib import admin
from django.urls import path, include
import os

# SECURITY WARNING: don't enable admin in production!
ADMIN = os.environ.get("ADMIN", "True")

urlpatterns = [
    # allauth url
    path('accounts/', include('allauth.urls')),
    # Including all content of pages folder on our 'requisition dispatcher'
    path("", include("pages.urls", namespace="pages")),
]

if ADMIN:
    urlpatterns.append(
        path('admin/', admin.site.urls),
    )
