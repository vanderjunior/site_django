# -*- coding: utf-8 -*-
# from mysite.polls.models import Polls
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You are look at poll %s." % poll_id)
