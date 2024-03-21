from django.contrib.auth.models import User
from django.shortcuts import render
from django_filters.rest_framework import filters
from rest_framework import generics
from . import models
from . import serializers
from rest_framework import permissions
from .permissions import IsTest


# Create your views here.
class ProjectList(generics.ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class OrganizationList(generics.ListAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class OrganizationDetail(generics.RetrieveAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class ViolationTypeList(generics.ListAPIView):
    queryset = models.ViolationType.objects.all()
    serializer_class = serializers.ViolationTypeSerializer


class ViolationList(generics.ListCreateAPIView):
    # queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationSerializer
    filterset_fields = ['project', 'status']
    # permission_classes = [IsTest]

    def get_queryset(self):
        user = self.request.user
        queryset = models.Violation.objects.filter(creator=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TaskList(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        task_id = self.kwargs['task']
        return models.Comment.objects.filter(task=task_id)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class AttachmentList(generics.ListCreateAPIView):
    queryset = models.Attachment.objects.all()
    serializer_class = serializers.AttachmentSerializer


class AttachmentDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Attachment.objects.all()
    serializer_class = serializers.AttachmentSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
