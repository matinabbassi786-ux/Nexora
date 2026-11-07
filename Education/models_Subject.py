from django.db import models


class Subject(models.Model):

    Name = models.CharField(max_length=200, unique=True)

    Field = models.ManyToManyField(
        "Education.Field",
        related_name="subjects",
        blank=True
    )

    Description = models.TextField(blank=True)

    Is_Active = models.BooleanField(default=True)

    Create_By = models.DateTimeField(auto_now_add=True)

    Last_By = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ["Name"]