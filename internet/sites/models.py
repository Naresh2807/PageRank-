from django.db import models

# Create your models here.


# class WebsiteManager(models.Manager):
#     def check_and_add(self, link):
#         query_set = self.get_queryset()
#         query_list = [site.name for site in query_set]
#         if link not in query_list:
#             website = self.model(name=link)
#             website.save()
#             return website


class Website(models.Model):
    name = models.CharField(max_length=100)

    # objects = WebsiteManager()

    def __str__(self):
        return self.name
