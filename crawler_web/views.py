from django.shortcuts import render
from django.shortcuts import render_to_response

def index(req):
    return render_to_response('index.html',{})
def register(req):
    return render_to_response('register.html',{})