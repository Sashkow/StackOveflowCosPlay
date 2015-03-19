from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.main.views import main
# from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StackOveflowCosPlay1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main, name='index'),
    # url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts_social/', include('social_auth.urls')),

    
)
