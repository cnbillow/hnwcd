"""hnwcd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from women import views as women_views



urlpatterns = [
    url(r'^$',women_views.index,name='index'),
    url(r'^NewsList/(?P<column_list>[^/]+)/',women_views.NewsList,name='NewsList'),
    url(r'^CityNews/',women_views.CityNew,name='CityNews'),
    url(r'^Prolist/',women_views.Project,name='Projects'),
    url(r'^Viewlist/',women_views.Video,name='Video'),
    url(r'^Comment/',women_views.Comment,name='Comment'),
    url(r'^check_code',women_views.check_code,name="Check"),
    url(r'^Aboutus/',women_views.About,name='About'),
    url(r'^Show/(?P<id>[^/]+)\.html',women_views.Show,name='Show'),
    url(r'^Zsshow/(?P<id>[^/]+)\.html',women_views.ZSShow,name='Zsshow'),
    url(r'^VideoShow/(?P<id>[^/]+)\.html',women_views.VideoShow,name='VideoShow'),
    url(r'^Bycity/(?P<cid>[^/]+)',women_views.ByCity,name='Bycity'),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
