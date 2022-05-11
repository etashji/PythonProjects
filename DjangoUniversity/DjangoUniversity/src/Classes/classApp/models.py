from django.db import models

#This designs the model
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.DecimalField(default=0.0, max_digits=10000, decimal_places=2)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(default=0.0)

# This creates the objects and saves them
object1 = djangoClasses(title = "object1", courseNumber = 1, instructorName = "Instructor1", duration = 1)
object1.save()

object2 = djangoClasses(title = "object2", courseNumber = 2, instructorName = "Instructor2", duration = 2)
object2.save()

object3 = djangoClasses(title = "object4", courseNumber = 3, instructorName = "Instructor3", duration = 3)
object3.save()