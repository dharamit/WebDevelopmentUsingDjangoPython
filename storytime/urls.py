from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from story import app

##for rest api
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'story.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^home2/', 'story.views.home1', name='home2'),

    url(r'^home3/', 'story.views.home3', name='home3'),

    url(r'^postPost/', 'story.views.postPost', name='postPost'),

    url(r'^admin/', include(admin.site.urls)),

    ###############for rest api##############
    url(r'^api/posts/$', app.PostList.as_view()),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
