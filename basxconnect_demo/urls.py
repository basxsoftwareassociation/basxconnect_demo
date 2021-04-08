from bread.utils.urls import protectedMedia
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # redirect to home page
    path("", RedirectView.as_view(pattern_name="core.person.browse")),
    #  all basx-bread urls
    path("", include("demoapp.urls")),
    path("bread/", include("bread.urls")),
    path("basxconnect/", include("basxconnect.core.urls")),
    path("reports/", include("bread.contrib.reports.urls")),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # in production we want to serve files with nginx, the protectedMedia function is used to check access permission with django and then make an internal redirect to nginx
    urlpatterns += [
        path(f"{settings.MEDIA_URL[1:]}<path:path>", protectedMedia, name="media")
    ]
