from rest_framework import viewsets
from .serializers import *

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Project Member ViewSet
class ProjectMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMemberSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        queryset = Project.objects.get(id=project_id).members.all()

        if self.kwargs.get('member_id'):
            return queryset.members.filter(id=self.kwargs['member_id'])

        return queryset

# Task Assignee ViewSet
class TaskAssigneeViewSet(viewsets.ModelViewSet):
    serializer_class = TaskAssigneeSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        queryset = Task.objects.get(id=task_id).assignees.all()

        if self.kwargs.get('assignee_id'):
            return queryset.assignees.filter(id=self.kwargs['assignee_id'])

        return queryset

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        queryset = Task.objects.get(id=task_id).comments.all()

        if self.kwargs.get('comment_id'):
            return queryset.comments.filter(id=self.kwargs['comment_id'])

        return queryset

# Notification ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)
