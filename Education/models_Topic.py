from django.db import models


class Topic(models.Model):

    Name = models.CharField(max_length=200)

    Subject = models.ManyToManyField(
        "Education.Subject",
        related_name="topics",
        blank=True
    )

    Description = models.TextField(blank=True)

    Is_Active = models.BooleanField(default=True)

    Create_By = models.DateTimeField(auto_now_add=True)

    Last_By = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["Name"]
        constraints = [
            models.UniqueConstraint(
                fields=["Name"],
                name="unique_topic_name"
            )
        ]

    def __str__(self):
        return self.Name