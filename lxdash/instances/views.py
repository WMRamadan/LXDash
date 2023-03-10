from django.http import HttpResponse
from django.template import loader
from lxdash.helpers import LXDash


def index(request):
    # latest_instance_list = [{"id": 123, "instance_text": "abc"}]
    lxdash = LXDash()
    latest_instance_list = lxdash.get_all_instances()
    template = loader.get_template('instances/index.html')
    context = {
        'latest_instance_list': latest_instance_list,
    }
    return HttpResponse(template.render(context, request))

def get_instance(request, name):
    lxdash = LXDash()
    detail_data = lxdash.get_instance_by_name(name=name)
    template = loader.get_template('instances/detail.html')
    context = {
        'detail_data': detail_data,
    }
    return HttpResponse(template.render(context, request))