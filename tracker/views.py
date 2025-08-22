from django.shortcuts import render,redirect
from .models import Current_balance, Tracker
from django.db.models import Sum

# Create your views here.
def index(request):
    if request.method=='POST':
        description=request.POST.get('description')
        amount=request.POST.get('amount')
        current_balance,_ = Current_balance.objects.get_or_create(id =1)
        expense_type = 'credit' 
        if float(amount) < 0 :
            expense_type = 'debit'
        tracker = Tracker.objects.create(amount=float(amount), description=description, expense_type=expense_type, current_balance=current_balance)
        current_balance.current_balance += float(tracker.amount)
        current_balance.save()
        return redirect('/')
    current_balance,_ = Current_balance.objects.get_or_create(id =1)
    income = 0
    expense = 0
    for tracking_history in Tracker.objects.all():
        if tracking_history.expense_type == "credit":
            income += tracking_history.amount
        else:
            expense += tracking_history.amount
    context = {'transactions' : Tracker.objects.all(),'current_balance': current_balance, 'income': income, 'expense': expense}
    return render(request, 'index.html',context)

def delete_transaction(request,id):
    tracking_history = Tracker.objects.filter(id=id)
    if tracking_history.exists():
        current_balance,_ = Current_balance.objects.get_or_create(id =1)
        tracking_history = tracking_history[0]
        current_balance.current_balance -= tracking_history.amount
        current_balance.save()
        tracking_history.delete()
    return redirect('/')    