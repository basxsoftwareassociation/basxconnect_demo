from basxconnect.core import models, settings
from bread import layout


def customcontext(request):
    return {
        "headerlayout": layout.shell_header.ShellHeader(
            "basx Connect",
            models.Person.objects.filter(pk=settings.OWNER_PERSON_ID).first(),
        )
    }
