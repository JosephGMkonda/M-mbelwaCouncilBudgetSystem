from django.contrib import admin
from .models import Revenue,Department,BudgetSubmission,BudgetItem,BudgetAllocation


class BudgetItemInline(admin.TabularInline):
    model = BudgetItem
    extra = 1

class BudgetSubmissionAdmin(admin.ModelAdmin):
    list_display = ('department', 'total_amount', 'submitted_by', 'submitted_at')
    inlines = [BudgetItemInline]  

admin.site.register(Department)
admin.site.register(Revenue)
admin.site.register(BudgetAllocation)
admin.site.register(BudgetSubmission, BudgetSubmissionAdmin)
admin.site.register(BudgetItem)

