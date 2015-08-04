from django.conf.urls import patterns, include, url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'index^$', views.index, name='index'),
    url(r'^test1$', views.test1, name='test1'),
    url(r'post_list$', views.post_list, name = 'post_list'),
    #url(r'^search/', include('haystack.urls')),
    url(r'^search_form/$', views.search_form, name = 'search_form'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^clean_data/$', views.clean_data, name = 'clean_data'),
    url(r'^blog-single/$', views.blog_single, name = 'blog_single'),
    url(r'^clean_data2/$', views.clean_data2, name = 'clean_data2'),
    url(r'^estimation/$', views.estimation, name = 'estimation'),
    url(r'^quality/$', views.quality, name = 'quality'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
]

### add media urls ###

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))

