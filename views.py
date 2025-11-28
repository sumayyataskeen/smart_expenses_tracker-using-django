from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Expense

def register_user(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect("login")
    return render(request, "expenses/register.html")


def login_user(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "expenses/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    total = sum(e.amount for e in expenses)
    return render(request, "expenses/dashboard.html", {"expenses": expenses, "total": total})


@login_required
def add_expense(request):
    if request.method == "POST":
        Expense.objects.create(
            user=request.user,
            title=request.POST['title'],
            amount=request.POST['amount'],
            category=request.POST['category']
        )
        return redirect("/")
    return render(request, "expenses/add.html")
