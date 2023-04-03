from basxbread.utils.urls import protectedMedia
from basxbread.views.error import handler400, handler403, handler404, handler500  # noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView

# set default django error views to basxbread views

urlpatterns = [
    # redirect to home page
    path("", RedirectView.as_view(pattern_name="core.person.browse")),
    path("admin/", admin.site.urls),
    #  all basxbread urls
    path("", include("demoapp.urls")),
    path("basxbread/", include("basxbread.urls")),
    path("basxconnect/", include("basxconnect.core.urls")),
    path("basxconnect/", include("basxconnect.projects.urls")),
    path("basxconnect/", include("basxconnect.invoicing.urls")),
    path("reports/", include("basxbread.contrib.reports.urls")),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # in production we want to serve files with nginx, the protectedMedia function
    # is used to check access permission with django and then make an internal
    # redirect to nginx
    urlpatterns += [
        path(f"{settings.MEDIA_URL[1:]}<path:path>", protectedMedia, name="media")
    ]
