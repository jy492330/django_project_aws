from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=300, unique=True, null=False)
    location = models.CharField(max_length=300, unique=True, null=False)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=300, unique=False, null=False)
    
    hospitals = models.ManyToManyField(Hospital, related_name="departments")

    def __str__(self):
        return self.name


class Cost_Center(models.Model):
    cc_color = models.CharField(unique=True, null=False, max_length=20)
    cc_code = models.IntegerField(unique=True, null=False)

    department = models.OneToOneField(
        Department,
        related_name="cost_center",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.cc_code)
