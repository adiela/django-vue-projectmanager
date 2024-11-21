import django_filters
from .models import Project, Task, ProjectMember, Comment, TaskAssignee, Invitation

class ProjectFilter(django_filters.FilterSet):
    member_id = django_filters.NumberFilter(
        method='filter_by_member', label='Filter by member ID'
    )

    class Meta:
        model = Project
        fields = ['member_id']  # This field is derived via the custom method

    def filter_by_member(self, queryset, name, value):
        return queryset.filter(team__members__id=value)
    

class TaskFilter(django_filters.FilterSet):
    project_id = django_filters.NumberFilter(
        method='filter_by_project', label='Filter by project ID'
    )
    user_id = django_filters.NumberFilter(
        method='filter_by_user', label='Filter by user ID'
    )

    class Meta:
        model = Task
        fields = ['project_id', 'user_id']

    def filter_by_project(self, queryset, name, value):
        return queryset.filter(project__id=value)
    
    def filter_by_user(self, queryset, name, value):
        return queryset.filter(taskasignee__user__id=value)
    
class ProjectMemberFilter(django_filters.FilterSet):
    project_id = django_filters.NumberFilter(
        method='filter_by_project', label='Filter by project ID'
    )

    class Meta:
        model = ProjectMember
        fields = ['project_id']

    def filter_by_project(self, queryset, name, value):
        return queryset.filter(project__id=value)
    
class CommentFilter(django_filters.FilterSet):
    task_id = django_filters.NumberFilter(
        method='filter_by_task', label='Filter by task ID'
    )

    class Meta:
        model = Comment
        fields = ['task_id']

    def filter_by_task(self, queryset, name, value):
        return queryset.filter(task__id=value)

class TaskAssigneeFilter(django_filters.FilterSet):
    task_id = django_filters.NumberFilter(
        method='filter_by_task', label='Filter by task ID'
    )

    class Meta:
        model = TaskAssignee
        fields = ['task_id', 'user_id']

    def filter_by_task(self, queryset, name, value):
        return queryset.filter(task__id=value)

class InvitationFilter(django_filters.FilterSet):
    project_id = django_filters.NumberFilter(
        method='filter_by_project', label='Filter by project ID'
    )
    created_by = django_filters.NumberFilter(
        method='filter_by_user', label='Filter by user ID'
    )

    class Meta:
        model = Invitation
        fields = ['project_id', 'created_by']

    def filter_by_project(self, queryset, name, value):
        return queryset.filter(project__id=value)
    
    def filter_by_user(self, queryset, name, value):
        return queryset.filter(created_by__id=value)