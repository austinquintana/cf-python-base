# recipe_project/urls.py

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, logout_view
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("recipes.urls")),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "success/",
        TemplateView.as_view(template_name="recipes/success.html"),
        name="success",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)