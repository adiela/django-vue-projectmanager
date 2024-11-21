from rest_framework import viewsets, mixins
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProjectFilter, TaskFilter, ProjectMemberFilter, TaskAssigneeFilter, CommentFilter, InvitationFilter

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

# Project Member ViewSet
class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectMemberFilter

# Task Assignee ViewSet
class TaskAssigneeViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignee.objects.all()
    serializer_class = TaskAssigneeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskAssigneeFilter

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter

# Notification ViewSet
class NotificationViewSet( mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)

# Invitation ViewSet
class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer