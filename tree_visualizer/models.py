from django.db import models

class TreeNode(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    value = models.IntegerField()
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"Node({self.value})"
