
# Expencse Manager Project

## Overview
The **Daily Expenses Sharing Application** is a backend application designed to help users manage and share their daily expenses. Users can add expenses, split costs using different methods, and generate balance sheets for easy tracking of expenses.

## Objective
To create a user-friendly backend for a daily-expenses sharing application that allows users to efficiently manage their expenses and share costs with others.

## Features
- **User Management**
  - Create and retrieve user details.
- **Expense Management**
  - Add expenses.
  - Split expenses based on:
    - Exact amounts.
    - Percentages.
    - Equal splits.
  - Retrieve expenses.
- **Balance Sheet Generation**
  - Generate and download balance sheets.
- **API Endpoints**
  - Create User: `/api/users/`
  - Add Expense: `/api/expenses/`
  - Retrieve Expenses: `/api/expenses/`
  - Download Balance Sheet: `/api/expenses/download/`
- **Input Validation**
  - Validates user inputs and expense splits for accuracy.
 
# Screenshots
Admin Login Page
<img src="Snapshot_Running_Project/Screenshot 2024-10-20 144740.jpg" alt="Admin Login Page" width="600"/>
After Login
<img src="Snapshot_Running_Project/Screenshot 2024-10-20 150747.jpg" alt="After Login" width="600"/>

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Django REST Framework

### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/daily-expenses-sharing-app.git
cd daily-expenses-sharing-app

## Bonus Features:
- Authentication and authorization
- Input validation and error handling
- Optimized for large datasets
- Unit and integration tests
