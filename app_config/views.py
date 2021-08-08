from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse, JsonResponse
from .models import App, Parameter, ConfigRequest
import json
from json import JSONEncoder
import logging

log = logging.getLogger(__name__)
class MyEncoder(JSONEncoder):
    def default(self, o):
        def default(self, obj):
            try:
                return json.JSONEncoder.default(self, obj)
            except:
                try:
                    return dict(obj)
                except:
                    return str(obj)


def params(request, app_name):
    try:
        cfg_req = ConfigRequest(
            app = App.objects.get(name=app_name),
            remote_addr=request.META["REMOTE_ADDR"],
            user_agent=request.META["HTTP_USER_AGENT"],
            data=str(request.META),
        )
        cfg_req.save()
    except:
        log.error("Failed to save request details", exc_info=True)
        pass

    param_list = Parameter.objects.filter(app__name=app_name)
    params = {p.name: p.value for p in param_list}
    return JsonResponse(params)
