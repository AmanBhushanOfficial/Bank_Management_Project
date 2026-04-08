# Bank Management System

*A Streamlit-based Web Application for Basic Banking Operations*

---

## Overview

The Bank Management System is a Python-based web application built using Streamlit, designed to simulate core banking functionalities. It provides a simple and interactive interface for managing bank accounts, performing transactions, and maintaining user data.

This project demonstrates the use of Object-Oriented Programming (OOP) along with a lightweight frontend framework to build functional web applications.

---

## Key Features

* Account creation with user details
* Deposit and withdrawal operations
* Account information retrieval
* Update account credentials
* Account deletion functionality
* Interactive user interface

---

## Tech Stack

* Frontend: Streamlit
* Backend: Python (OOP-based architecture)
* State Management: Streamlit Session State

---

## Project Structure

```bash
Bank-Management-System/
│
├── app.py        # Streamlit application (UI Layer)
├── hello.py      # Backend logic (Bank class implementation)
└── README.md     # Project documentation
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bank-management-system.git
cd bank-management-system
```

### 2. Install Dependencies

```bash
pip install streamlit
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Access the Application

Open your browser and navigate to:

```
http://localhost:8501
```

---

## Functional Modules

### Create Account

Allows users to register by providing details such as name, age, email, and PIN.

### Deposit Funds

Enables users to add money to their account after verification.

### Withdraw Funds

Allows withdrawal of funds with balance validation.

### Check Account Details

Displays account information upon successful authentication.

### Update Account

Supports updating user details such as name, email, and PIN.

### Delete Account

Permanently removes an account from the system.

---

## Limitations

* No database integration (data is not persistent)
* PIN is not encrypted
* Limited input validation
* No authentication or session security

---

## Future Enhancements

* Database integration (SQLite, MongoDB)
* Secure authentication and encryption
* Transaction history tracking
* Improved user interface
* Cloud deployment

---

## Learning Outcomes

* Implementation of Object-Oriented Programming in Python
* Building web applications using Streamlit
* Handling user input and session state
* Structuring a real-world project

---

## Author

Aman Bhushan
Aspiring AI Engineer | Python Developer

---

## License

This project is open-source and intended for educational purposes.
