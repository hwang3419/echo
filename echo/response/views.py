# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from os.path import join
import yaml
import aiml
from models import Entry, KeyErr


def getBotPredicate(self,name):
    try: return self._botPredicates[name]
    except KeyError, e:
        try:
            KeyErr.objects.create(keyname = e, fucname = 'getBotPredicate')
        except Exception, e:
            print e
        return ""


def getPredicate(self, name, sessionID = "_global"):
    try: return self._sessions[sessionID][name]
    except KeyError, e:
        try:
            KeyErr.objects.create(keyname = e, fucname = 'getPredicate')
        except Exception,e:
            print e
        return ""


aiml.Kernel.getBotPredicate = getBotPredicate
aiml.Kernel.getPredicate = getPredicate


# bot setup
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
    try:
        ismath = do_math(msg)
        if ismath:
            return HttpResponse(ismath)
    except:
        pass
    ip = get_client_ip(request)
    for s in msg:
        if is_chinese(s):
            return HttpResponse('I am still learning Chinese, let\'s chat in English! :)')
    r = k.respond(msg)
    msg = msg.encode('ascii','ignore')
    
    try:
        Entry.objects.create(ask = msg, ip = ip, response = r)
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


def do_math(msg):
    if '+' in msg or '*' in msg or '-' in msg or '/' in msg:
        slist = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 46, 43, 45, 42, 47, 40, 41]
        strip_msg = "".join([i for i in msg if ord(i) in slist ])
        try:
            result = eval(strip_msg)
            if result<50:
                return '='+ 'bark '* result
            else:
                return '='+ 'bark *'+str(result)
        except:
            return False
    return False