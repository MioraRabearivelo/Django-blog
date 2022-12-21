from  django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # on associe nos chemins d' urls à des fichiers, ici par une image
