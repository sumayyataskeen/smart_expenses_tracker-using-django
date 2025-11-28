Smart Expense Tracker — A Simple Daily Money Manager (Built with Django)
Managing money is difficult when we don’t remember where it’s going.
This project helps you track every rupee you spend, organize expenses into categories, and visually see where most of your money is going — all in one clean dashboard.
It’s simple. It’s fast. And it makes you more aware of your spending habits.
What this project does
Add your expenses daily — food, shopping, travel, bills… anything.
See your spending pattern with colorful charts.
Know how much you spent this month in one click.
Edit or delete an entry anytime.
All your data stays safe under your own login.
Why I built this
I wanted a practical project that solves a real-life problem.
We spend money everywhere — online, offline, small purchases, impulse buys…
Keeping track manually is tiring.
So I built a tool that quietly records everything and tells me:

“Hey, you spent too much on Swiggy this month ”

This helps me control extra spending and plan better.
Tech behind the project
Django (Python) — handles backend & database
SQLite — default database, easy to run
HTML + CSS + Bootstrap — simple and clean UI
Chart.js — beautiful graphs for analysis
The project is small enough to understand completely,
yet strong enough to showcase in interviews.
Folder Overview
smart_expense_tracker/
│── smart_tracker/      → Main project settings
│── expenses/           → Core logic (views, models, templates)
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│── manage.py
