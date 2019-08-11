from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='HOME'),
    url(r'^neighborhood/(?P<neighborhood_id>[0-9])$',views.neighborhood,name='NEIGHBORHOOD DETAILS '),
    url(r'^profile/',views.user_profile,name='USER PROFILE'),
    url(r'^search/',views.search_business,name='SEARCH'),
    url(r'^new/neighborhood$',views.new_neighborhood,name='NEW REGION'),
    url(r'^edit_profile$',views.edit_profile,name='EDIT PROFILE'),
    url(r'^new/business$',views.new_business,name='NEW BUSINESS'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
