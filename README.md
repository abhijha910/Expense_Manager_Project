
# Expencse Manager Project

## Objective:
Design and implement a backend for a daily-expenses sharing application. This 
application allows users to add expenses and split them based on three 
different methods: exact amounts, percentages, and equal splits. The 
application manages user details, validates inputs, and generates 
downloadable balance sheets.

## Features:
- User management (Create, retrieve user details)
- Expense management (Add, split, retrieve expenses)
- Balance sheet generation
- API Endpoints
  - Create User
  - Add Expense
  - Retrieve Expenses
  - Download Balance Sheet
- Validation for user inputs and expense splits

## Setup Instructions:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run database migrations with `python manage.py migrate`.
4. Start the server using `python manage.py runserver`.

## API Endpoints:
- `/api/users/` : Create or retrieve users.
- `/api/expenses/` : Add or retrieve expenses.
- `/api/expenses/download/` : Download balance sheet.

## Requirements:
- Python 3.x
- Django
- Django REST Framework

## Bonus Features:
- Authentication and authorization
- Input validation and error handling
- Optimized for large datasets
- Unit and integration tests
