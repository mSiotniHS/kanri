from django.contrib import admin
from .models import Inbox, InboxFile, Project, ProjectLog, Space, Task


class InboxFileInlineAdmin(admin.StackedInline):
    model = InboxFile


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    inlines = [InboxFileInlineAdmin]


class ProjectLogInlineAdmin(admin.StackedInline):
    model = ProjectLog


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectLogInlineAdmin]


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
