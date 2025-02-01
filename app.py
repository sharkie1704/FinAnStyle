
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#LOGIN PAGE
#EXPENSES UPDATE PAGE
#MENU PAGE
#PAGE FOR EACH MENU OPTION

st.title("Hello World! This is our ConUHacks IV project.")
st.write("This is a simple Streamlit Finance and Budgeting app.")
st.balloons()

# Initialize session state if it's not already initialized
if 'expenses' not in st.session_state:
    st.session_state.expenses = []


# Streamlit app layout for EXPENSES
st.title("Expense Tracker")
st.write("This is where you can track your expenses.")
# Input fields for the user to enter expenses
expense_name = st.text_input("Expense Name", "")
expense_amount = st.number_input("Expense Amount", min_value=0.01, format="%.2f")
expense_category = st.selectbox("Expense Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])

# Button to add the expense to the list
if st.button("Add Expense"):
    if expense_name and expense_amount > 0:
        st.session_state.expenses.append({
            'Name': expense_name,
            'Amount': expense_amount,
            'Category': expense_category
        })
        st.success(f"Added {expense_name} for ${expense_amount} under {expense_category} category.")
    else:
        st.error("Please enter valid expense details.")

# Display the table of expenses
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.write("### Your Expenses:")
    st.dataframe(df)
    
    # Calculate and display the total
    total_spent = df['Amount'].sum()
    st.write(f"### Total Spent: ${total_spent:.2f}")

    # Visualize expenses by category with a pie chart
    category_totals = df.groupby('Category')['Amount'].sum()
    fig, ax = plt.subplots()
    ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.write("### Expenses by Category:")
    st.pyplot(fig)
else:
    st.write("No expenses added yet.")

st.title("Income Tracker")
st.write("This is where you can track your incomes.")
income_name = st.text_input("Income Name", "");
income_amount = st.number_input("Income Amount", min_value=0.01, format="%.2f")
income_category = st.selectbox("Income Category", ["Salary", "Scholarship/Bursary", "Loans", "Bonus", "Gift", "Other"])

# Button to add an income to the list
if st.button("Add Income"):
    if income_name and income_amount > 0:
        st.session_state.incomes.append({
            'Name': income_name,
            'Amount': income_amount,
            'Category': income_category
        })