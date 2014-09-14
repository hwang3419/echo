# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from os.path import join
import yaml
import aiml
from models import Entry
B = join(settings.ROOT_DIR,'brain')
C = join(settings.ROOT_DIR,'config.yaml')
config = yaml.safe_load(open(C))
k = aiml.Kernel()
k.loadBrain(B)
for key, value in config.items():
    k.setPredicate(key, value)
    k.setBotPredicate(key, value)
def answer(request):
    msg = request.GET.get('message')
    ip = get_client_ip(request)
    if is_chinese(msg):
        return HttpResponse('I am still learning Chinese, let\'s chat in English! :)')
    r = k.respond(msg)
    msg = msg.encode('ascii','ignore')
    e = Entry(ask = msg, ip = ip, response = r)
    try:
        e.save()
    except Exception,e:
        print e

    return HttpResponse(r)

def home(request):
    return render_to_response('home.html')

def is_chinese(uchar):
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip