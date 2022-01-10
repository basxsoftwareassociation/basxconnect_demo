from bread.utils.urls import protectedMedia
from bread.views.error import view400, view403, view404, view500
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView

# set default django error views to bread views
handler400 = view400
handler403 = view403
handler404 = view404
handler500 = view500

urlpatterns = [
    # redirect to home page
    path("", RedirectView.as_view(pattern_name="core.person.browse")),
    path("admin/", admin.site.urls),
    #  all basx-bread urls
    path("", include("demoapp.urls")),
    path("bread/", include("bread.urls")),
    path("basxconnect/", include("basxconnect.core.urls")),
    path("basxconnect/", include("basxconnect.contributions.urls")),
    path("reports/", include("bread.contrib.reports.urls")),
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
