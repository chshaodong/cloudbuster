from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ansible.runner as runner
import os
import json

@csrf_exempt
def adhoc_runner(request):
    if request.method == "POST" and request.is_ajax():
        body = json.loads(request.body)
        results = runner.Runner(
            private_key_file=settings.PRIVATE_KEY_FILE,
            remote_user=body.get("remote_user", settings.REMOTE_USER),
            module_name=body.get("module_name", None),
            module_args=body.get("module_args", {}),
            extra_vars=body.get("extra_vars", None),
            host_list=body.get("host_list", []),
            is_playbook=True,
            sudo=True
            ).run()
        return JsonResponse(results)
    else:
        return HttpResponseBadRequest("Not a valid ajax request!")

    
