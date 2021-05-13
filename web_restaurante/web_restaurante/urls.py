"""web_restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from recipe.urls import recipe_patterns
from blog.urls import blog_patterns
from core.urls import core_patterns
from services.urls import services_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # Paths del core
    path('', include(core_patterns)),
    # Paths de servicios
    path('servicios/', include(services_patterns)),
    # Paths de blog
    path('blog/', include(blog_patterns)),
    # Paths del pages
    path('page/', include('pages.urls')),
    # Paths del contact
    path('contact/', include('contact.urls')),
    # Paths del recipe
    #path('recipe/', include('recipe.urls')),
    path('recipe/', include(recipe_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                            document_root = settings.MEDIA_ROOT)
