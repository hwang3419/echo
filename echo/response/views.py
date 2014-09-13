# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from os.path import join
import yaml
import aiml
B = join(settings.ROOT_DIR,'brain')
C = join(settings.ROOT_DIR,'config.yaml')
config = yaml.safe_load(open(C))
k = aiml.Kernel()
k.loadBrain(B)
for key, value in config.items():
    k.setPredicate(key, value)
def answer(request):
    msg = request.GET.get('message')
    print msg
    r = k.respond(msg)
    return HttpResponse(r)

def home(request):
    return render_to_response('home.html')