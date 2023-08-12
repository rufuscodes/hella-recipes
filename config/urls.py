from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from users import views as user_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes_app.urls')),
    path('register', user_views.register, name="user-register"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)