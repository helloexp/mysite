"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from vulnerability import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^indexS/$', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^vulnerability/$', views.vulnerability),
    url(r'^vulnerability/search/$', views.search),
    url(r'^vulnerability/importBatch/$', views.importBatch),
    url(r'^vulnerability/add/$',views.addVulnerability),
    url(r'^vulnerability/edit/\??$',views.editVulnerability),
    url(r'^vulnerability/add/result/$',views.add_Save),
    url(r'^login/$', views.login),
    url(r'^registration/$', views.registration),
    url(r'^forum/$', views.forum),
    url(r'^detail/$', views.detail_vul),
    url(r'^search/\??$',views.search_vul),
    url(r'^test2/$',views.display_meta),
]
