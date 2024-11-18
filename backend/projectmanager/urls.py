"""
URL configuration for projectmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myauth.views import UserViewSet
from projects.views import ProjectViewSet, TaskViewSet, ProjectMemberViewSet, TaskAssigneeViewSet, CommentViewSet, NotificationViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('projects/<project_id>/members/', ProjectMemberViewSet.as_view({'get': 'list'}), name='project-member-list'),
    path('projects/<project_id>/members/', ProjectMemberViewSet.as_view({'post': 'create'})),
    path('projects/<project_id>/members/<user_id>/', ProjectMemberViewSet.as_view({'get': 'retrieve'})),
    path('projects/<project_id>/members/<user_id>/', ProjectMemberViewSet.as_view({'delete': 'destroy'})),
    path('projects/<project_id>/members/<user_id>/', ProjectMemberViewSet.as_view({'patch': 'partial_update'})),
    path('tasks/<task_id>/assignees/', TaskAssigneeViewSet.as_view({'get': 'list'})),
    path('tasks/<task_id>/assignees/', TaskAssigneeViewSet.as_view({'post': 'create'})),
    path('tasks/<task_id>/assignees/<user_id>/', TaskAssigneeViewSet.as_view({'get': 'retrieve'})),
    path('tasks/<task_id>/assignees/<user_id>/', TaskAssigneeViewSet.as_view({'delete': 'destroy'})),
    path('tasks/<task_id>/assignees/<user_id>/', TaskAssigneeViewSet.as_view({'patch': 'partial_update'})),
    path('tasks/<task_id>/comments/', CommentViewSet.as_view({'get': 'list'})),
    path('tasks/<task_id>/comments/', CommentViewSet.as_view({'post': 'create'})),
    path('tasks/<task_id>/comments/<comment_id>/', CommentViewSet.as_view({'get': 'retrieve'})),
    path('tasks/<task_id>/comments/<comment_id>/', CommentViewSet.as_view({'delete': 'destroy'})),
    path('tasks/<task_id>/comments/<comment_id>/', CommentViewSet.as_view({'patch': 'partial_update'})),
]
