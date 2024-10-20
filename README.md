# Expense Manager Project

## Overview
The **Daily Expenses Sharing Application** is a backend application designed to help users manage and share their daily expenses. Users can add expenses, split costs using different methods, and generate balance sheets for easy tracking of expenses.

## Objective
To create a user-friendly backend for a daily-expenses sharing application that allows users to efficiently manage their expenses and share costs with others.

## Features
- **User Management**: Create and retrieve user details.
- **Expense Management**:
  - Add expenses.
  - Split expenses based on:
    - Exact amounts.
    - Percentages.
    - Equal splits.
  - Retrieve expenses.
- **Balance Sheet Generation**: Generate and download balance sheets.
- **API Endpoints**:
  - Create User: `/api/users/`
  - Add Expense: `/api/expenses/`
  - Retrieve Expenses: `/api/expenses/`
  - Download Balance Sheet: `/api/expenses/download/`
- **Input Validation**: Validates user inputs and expense splits for accuracy.

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Django REST Framework

### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/abhijha910/Expense_Manager_Project.git
cd Expense_Manager_Project
```
# Screenshots
Admin Login Page
<img src="Snapshot_Running_Project/Screenshot 2024-10-20 144740.jpg" alt="Admin Login Page" width="600"/>

After Login
     <img src="Snapshot_Running_Project/Screenshot 2024-10-20 150747.jpg" alt="After Login" width="600"/>


### Install Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Run Database Migrations
Apply database migrations:
```bash
python manage.py migrate
```

### Start the Server
Run the server:
```bash
python manage.py runserver
```

### API Endpoints
- `/api/users/` : Create or retrieve users.
- `/api/expenses/` : Add or retrieve expenses.
- `/api/expenses/download/` : Download balance sheet.

## Bonus Features:
- Authentication and authorization
- Input validation and error handling
- Optimized for large datasets
- Unit and integration tests

