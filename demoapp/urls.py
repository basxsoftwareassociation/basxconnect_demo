from basxbread.views.auth import LoginView
from django.urls import path


class DemoLoginView(LoginView):
    def get_form(self, *args, **kwargs):
        ret = super().get_form(*args, **kwargs)
        ret.fields["username"].widget.attrs["value"] = "demo"
        ret.fields["password"].help_text = "Use password 'connectdemo' to login"
        return ret


urlpatterns = [path("basxbread/accounts/login/", DemoLoginView.as_view(), name="login")]
