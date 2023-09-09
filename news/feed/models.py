from django.utils import timezone

from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.query import QuerySet


class CustomManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    
class TypeManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter


class Organizations(models.Model):
    name = models.CharField(max_length=40)
    shortname = models.CharField(max_length=10)
    number = models.CharField(max_length=11)
    adress = models.CharField()
    email = models.EmailField()
    link = models.TextField()


class Dvision(models.Model):
    name = models.CharField(max_length=40)
    organizations = models.ForeignKey(Organizations, on_delete=models.CASCADE, blank=True)


class Post(models.Model):
    class TypeNews(models.TextChoices):
        news = 'NE', 'News'
        announcement = 'AN', 'Announcement'
        message = 'ME', 'Message'

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    type = models.CharField(
        max_length=2,
        choices=TypeNews.choices,
        default=TypeNews.news
    )
    divizion = models.ForeignKey(Dvision, on_delete=models.CASCADE)
    title = models.CharField()
    created = models.DateField(auto_now_add=True)
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    published = CustomManager()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __sizeof__(self) -> int:
        self.size = super().__sizeof__()


class Employee(models.Model):
    class TypeEmloyee(models.TextChoices):
        EMPLOYEE = 'EP', 'EMPLOYEE'
        ADMIN = 'AD', 'ADMIN'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=TypeEmloyee.choices,
        default=TypeEmloyee.EMPLOYEE
    )
    division = models.ForeignKey(
        Dvision,
        on_delete=models.CASCADE,
    )
