from django.db import models
from django.conf import settings


# Revenue model class

class Revenue(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    month = models.DateField()
    collected_at=models.DateTimeField(auto_now_add=True)
    collected_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f'Revenue for the {self.month} : {self.amount}'

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name

class BudgetSubmission(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.department.name} - {self.total_amount}'

class BudgetItem(models.Model):
    submission = models.ForeignKey(BudgetSubmission, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.cost}'

class BudgetAllocation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    allocated_amount = models.DecimalField(max_digits=12, decimal_places=2)
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE)
    allocated_at = models.DateTimeField(auto_now_add=True)
    allocated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.department.name} - {self.allocated_amount}'

   



