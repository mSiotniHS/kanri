from django.db import models
from django.utils.translation import gettext_lazy as _


# class AppSettings(models.Model):
#     pass


class Inbox(models.Model):
    """
    Inbox is a bin where everything from the outer world
    first goes. That is something that is captured and
    should be processed in order to become a task or a project.
    Or any other thing: note, calendar event, etc. 
    """

    text = models.TextField(verbose_name=_("Text content"))

    def __str__(self) -> str:
        return self.text[:20]

    class Meta:
        verbose_name = _("Inbox entry")
        verbose_name_plural = _("Inbox entries")


class InboxFile(models.Model):
    """
    This model stores files for an inbox entry. There
    may be multiple files.
    """

    inbox_entry = models.ForeignKey(Inbox, on_delete=models.CASCADE, verbose_name=_("Inbox entry"))
    file = models.FileField(upload_to="inbox_files", verbose_name=_("File"))

    class Meta:
        verbose_name = _("Inbox entry file")
        verbose_name_plural = _("Inbox entry files")


class Space(models.Model):
    """
    Describes a set of projects grouped logically. For example,
    you can have "Personal" space with personal-related projects and
    tasks. Same for "Work" space or "Uni" space.
    """

    name = models.CharField(max_length=50, verbose_name=_("Name"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Space")
        verbose_name_plural = _("Spaces")


class Project(models.Model):
    """
    Project is a collection of tasks. Project has a goal towards
    which all tasks are oriented.
    """

    name = models.CharField(max_length=150, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    archived = models.BooleanField(default=False, verbose_name=_("Is archived"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


class ProjectLog(models.Model):
    """
    Project log is a note that has a timestamp and reflects
    any updates on a project. That may be a result of a task,
    some problem log to note in the future --- virtually
    anything that might be important.
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("Log's project"))
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_("Timestamp"))
    text = models.TextField(verbose_name=_("Log text"))

    def __str__(self) -> str:
        return f'{self.project} | {self.timestamp} | {self.text[:20]}'

    class Meta:
        verbose_name = _("Project log")
        verbose_name_plural = _("Project changelog")


class TaskStatus(models.IntegerChoices):
    """
    Represents various states that a task can be in.
    """

    TODO = 0, _("To do")
    INWORK = 1, _("In work")
    CANCELED = 2, _("Canceled")
    WAITING = 3, _("Waiting")
    DONE = 4, _("Done")


class Task(models.Model):
    """
    Describes a task --- some understandable, relatively easily
    action.
    """

    name = models.CharField(max_length=150, verbose_name=_("Name"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("Parent project"))
    status = models.SmallIntegerField(choices=TaskStatus.choices, default=TaskStatus.TODO, verbose_name=_("Status"))
    deadline = models.DateTimeField(null=True, blank=True, verbose_name=_("Deadline"))
    archived = models.BooleanField(default=False, verbose_name=_("Is archived"))

    def __str__(self) -> str:
        return f'({self.project}) {self.name} | {TaskStatus(self.status).label}'

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
