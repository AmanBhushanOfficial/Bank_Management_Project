# Improvise with the Help of AI

import streamlit as st
from hello import Bank   # your backend file

bank = Bank()

st.title("🏦 Bank Management System")

options = [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Check Details",
    "Update",
    "Delete"
]

if "menu" not in st.session_state:
    st.session_state.menu = options[0]

menu = st.sidebar.selectbox(
    "Select Option",
    options,
    index=options.index(st.session_state.menu),
    key="menu_select"
)

st.session_state.menu = menu

# -----------------------------

if menu == "Create Account":
    st.header("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN")

    if st.button("Create"):
        result = bank.create_account(name, age, email, int(pin))
        st.success(result)

# -----------------------------

elif menu == "Deposit":
    st.header("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount")

    if st.button("Deposit"):
        result = bank.deposit(acc, int(pin), amount)
        st.success(result)

# -----------------------------

elif menu == "Withdraw":
    st.header("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount")

    if st.button("Withdraw"):
        result = bank.withdraw(acc, int(pin), amount)
        st.success(result)

# -----------------------------

elif menu == "Check Details":
    st.header("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Show"):
        result = bank.get_details(acc, int(pin))
        st.write(result)

# -----------------------------

elif menu == "Update":
    st.header("Update Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Old PIN")

    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        result = bank.update(acc, int(pin), name, email, new_pin)
        st.success(result)

# -----------------------------

elif menu == "Delete":
    st.header("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Delete"):
        result = bank.delete(acc, int(pin))
        st.error(result)
