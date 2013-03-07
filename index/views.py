# -*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
import conf.constants

def index(request):
    print 'asd:'+conf.constants.RIGHT
    return render_to_response('default.html', {'latest_poll_list': 12})