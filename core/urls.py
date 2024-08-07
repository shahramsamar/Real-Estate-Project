"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap, PropertySitemap
from blog.sitemaps import BlogSitemap

import debug_toolbar
from core.veiws import coming_soon

sitemaps={'static':StaticViewSitemap,'blog':BlogSitemap, 'properties': PropertySitemap}

  

urlpatterns = [
    # added path user
    # re_path(r'^.*$', coming_soon),
    path("admin/", include("honeypot.urls")),
    path("secret", admin.site.urls),

    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),

    # added path user
    path('captcha/', include('captcha.urls')),
    
    path('sitemap.xml', sitemap, 
         {'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    
    path('robots.txt', include('robots.urls')),
    
    path('tinymce/', include('tinymce.urls')),
    # this setting for dev
    path("__debug__/", include("debug_toolbar.urls")),

]


# static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Custom error handler
handler400 = 'website.views.custom_400'# bad_request
handler403 = 'website.views.custom_403'# permission_denied
handler404 = 'website.views.custom_404'# page_not_found
handler500 = 'website.views.custom_500' # server_error

