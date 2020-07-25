from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Django REST framework standard libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Authentification
from django.contrib.auth.decorators import login_required

# Django REST framework my stuff
from .serializers import TaskSerializer, EventSerializer, ActivitySerializer, \
    TimeSerializer

# My classes
from mysite.models import Activity, Event, Task, Project, Time


def this_user_only(get_queryset):
    """
    :param get_queryset function:
    :return: get_queryset function with query objects limited to this user only
             if user is registered. Otherwise – nothing
    """

    def function_wrapper(self):
        # Get the current user
        current_user = self.request.user

        # If user is not registered
        if current_user.id is None:
            # Return empty query set and get out
            return []

        # If user is OK make the basic fetch
        queryset = get_queryset(self)
        # Apply user filter to the fetched data
        result = queryset.filter(user_id=current_user)

        return result

    return function_wrapper


@login_required
def index(request):
    return HttpResponse('It is api index page')


class EventTasksList(APIView):
    """
    List all tasks for a particular
    """

    def get(self, request, pk):
        tasks = Event.objects.get(pk=pk).task_set.all().order_by('order')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    """
    The view set to provide CRUD operation on Task
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @this_user_only
    def get_queryset(self):
        return self.queryset


class TimeViewSet(viewsets.ModelViewSet):
    """
    The view set to provide CRUD operation on Task
    """
    serializer_class = TimeSerializer
    queryset = Time.objects.all()

    def get_queryset(self):
        user = self.request.user
        user_events = Event.objects.filter(user_id=user)
        tasks = Task.objects.filter(event_id__in=user_events)
        return self.queryset.filter(task_id__in=tasks)


class EventViewSet(viewsets.ModelViewSet):
    """
    The view set to provide CRUD operation on Task
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @this_user_only
    def get_queryset(self):
        return self.queryset.filter(active=True).order_by('start')

    # TODO: Add permission classes (later on)

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    The view set to provide CRUD operation on Task
    """

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    # TODO: Add permission classes (later on)

    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)