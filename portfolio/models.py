from django.db import models



#RPA-IoT-DataScience-Development

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, blank =True, null=True)
    github_link = models.CharField(max_length=200)

    def __str__(self):
        return self.summary


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=200)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name