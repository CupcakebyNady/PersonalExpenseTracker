from django.shortcuts import render
from .models import Expense

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenseapp/expense_list.html', {'expenses': expenses})
