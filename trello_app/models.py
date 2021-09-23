from django.db import models
from django.http import request
from django.utils import timezone
from django.contrib.auth.models import User

# user will create boards in boards it have list and in list it have tasks
# Create your models here.
class Board(models.Model):
  # TODO: Add name field with max_length = 50
  name = models.CharField(max_length= 60, null = True)
  created_at = models.DateTimeField(default=timezone.now)

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  #dunder str method
  def __str__(self):
      return f"{self.name}"

class TaskList(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(
    default=timezone.now
  )
  # TODO: Add board field which is foreign key to the Board model
  # board = ...
  board = models.ForeignKey(Board, on_delete= models.CASCADE, null = True)

  def __str__(self):
    return f"{self.name}"

class Task(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  created_at = models.DateTimeField(
    default=timezone.now
  )
  due_date = models.DateTimeField()
  list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name}"