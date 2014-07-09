from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
