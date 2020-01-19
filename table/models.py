from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

class Status(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.title)
        
    
class Task(models.Model):
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    desctription = models.TextField()

    def __str__(self):
        if len(str(self.title)) < 50:
            return str(self.title)
        else:
            return str(self.title)[:50] + "..."
