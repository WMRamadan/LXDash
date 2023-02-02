from django.http import HttpResponse
from django.template import loader
from lxdash.helpers import LXDash


def index(request):
    lxdash = LXDash()
    lxdash_resources = lxdash.get_client_resources()
    template = loader.get_template('lxdash/index.html')
    context = {
        'lxdash_version': 1.0,
        'lxdash_resources': lxdash_resources,
    }
    return HttpResponse(template.render(context, request))