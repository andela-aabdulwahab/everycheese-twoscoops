from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<slug>[\w\-]+)/$',
        view=views.CheeseDetailView.as_view(),
        name='details'
    ),
]
