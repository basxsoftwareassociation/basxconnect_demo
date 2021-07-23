from bread.views.auth import BreadLoginView
from django.urls import path


class DemoLoginView(BreadLoginView):
    def get_form(self, *args, **kwargs):
        ret = super().get_form(*args, **kwargs)
        ret.fields["username"].widget.attrs["value"] = "demo"
        ret.fields["password"].help_text = "Use password 'connectdemo' to login"
        return ret


urlpatterns = [path("bread/accounts/login/", DemoLoginView.as_view(), name="login")]
