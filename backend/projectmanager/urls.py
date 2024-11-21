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
from django.urls import path, include, re_path
from myauth.views import UserViewSet, GitHubLogin
from projects.views import ProjectViewSet, TaskViewSet, ProjectMemberViewSet, TaskAssigneeViewSet, CommentViewSet, NotificationViewSet, InvitationViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'projectmembers', ProjectMemberViewSet)
router.register(r'taskassignees', TaskAssigneeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'invitations', InvitationViewSet)

notification_views_list = NotificationViewSet.as_view({
    'get': 'list',
})
notification_views_detail = NotificationViewSet.as_view({
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls'), name='rest_auth_register'),
    path('api/auth/github/', GitHubLogin.as_view(), name='github_login'),
    path('/accounts/', include('allauth.urls')),
    path('notifications/', notification_views_list, name='notification-list'),
    path('notifications/<int:pk>/', notification_views_detail, name='notification-detail'),
]
