from django.db import models

class Status(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.title)
        
    
class Task(models.Model):
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    
    def __str__(self):
        if len(str(self.title)) < 50:
            return str(self.title)
        else:
            return str(self.title)[:50] + "..."
