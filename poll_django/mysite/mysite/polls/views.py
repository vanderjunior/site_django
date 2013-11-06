# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from mysite.polls.models import Poll
from django.http import HttpResponse


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    return HttpResponse("You are look at poll %s." % poll_id)
