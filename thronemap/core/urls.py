from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LocationDetailsView, LocationsView
from .views import LocationRatingsView, LocationRatingDetailsView
from .views import UserViewSet

urlpatterns = {
    url(r'^locations$',
        LocationsView.as_view(), name="create"),
    url(r'^locations/(?P<pk>[0-9]+)$',
        LocationDetailsView.as_view(), name="details"),
    url(r'^locations/(?P<pk>[0-9]+)/ratings$',
        LocationRatingsView.as_view(), name="create"),
    url(r'^locationratings/(?P<pk>[0-9]+)$',
        LocationRatingDetailsView.as_view(), name="details"),
    url(r'^users$', UserViewSet.as_view({'post': 'create'}), name="users"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
