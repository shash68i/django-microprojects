from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', SignUpView.as_view(), name='signup'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
