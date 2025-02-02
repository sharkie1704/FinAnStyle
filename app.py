import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#LOGIN PAGE in progress 
#EXPENSES UPDATE PAGE in progress
#MENU PAGE in progress
#PAGE FOR EACH MENU OPTION

import streamlit as st

# Table of contents with links
st.markdown("""
    <div style="position:fixed; top:10px; right:10px; width:200px;">
        <h3>Table of Contents</h3>
        <ul>
            <li><a href="#section1">Section 1</a></li>
            <li><a href="#section2">Section 2</a></li>
            <li><a href="#section3">Section 3</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Content Sections
st.markdown('<a id="section1"></a>', unsafe_allow_html=True)
st.header('Section 1')
st.write('This is the content for section 1.')

st.markdown('<a id="section2"></a>', unsafe_allow_html=True)
st.header('Section 2')
st.write('This is the content for section 2.')

st.markdown('<a id="section3"></a>', unsafe_allow_html=True)
st.header('Section 3')
st.write('This is the content for section 3.')

# Initialize session state
if 'expenses' not in st.session_state:
        st.session_state.expenses = []
if 'incomes' not in st.session_state:
    st.session_state.incomes = []

# Set page configuration
st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for theming
st.markdown("""
    <style>
    .css-18e3th9 {
        background-color: #f5f5f5;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .css-1d391kg {
        background-color: #2e3b4e;
        color: white;
    }
    .css-1d391kg a {
        color: white;
    }
    .css-1d391kg a:hover {
        color: #f39c12;
    }
    </style>
    """, unsafe_allow_html=True)

# Define pages:

# Login page
def login_page():
    st.title("Welcome to the Fine-An-Style App!")
    st.write("This is your next step towards a healthier financial life (hopefully).")
    #st.balloons()
    st.title("Login Page")
    st.write("This is the login page.")
    
# Menu page    
def menu_page():
    st.title("Welcome to the Fine-An-Style App!")
    st.write("This is your next step towards a healthier financial life (hopefully).")
    st.image("https://www.shutterstock.com/image-vector/bank-building-architecture-facade-government-600nw-2440534455.jpg", use_container_width=True)


# Expenses page
def expenses_page():
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

    weekly_budget = st.text_input("Weekly Budget", "")
    if total_spent > weekly_budget:
        st.write("You have exceeded your weekly budget. We recommend the following:")

# Income page
def income_page():
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
            st.success(f"Added {expense_name} for ${expense_amount} under {expense_category} category.")
        else:
            st.error("Please enter valid expense details.")      
    # Display the table of incomes
    if st.session_state.incomes:
        df = pd.DataFrame(st.session_state.incomes)
        st.write("### Your Incomes:")
        st.dataframe(df)
        # Calculate and display the total
        total_spent = df['Amount'].sum()
        st.write(f"### Total Gained: ${total_spent:.2f}")
        # Visualize incomes by category with a pie chart
        category_totals = df.groupby('Category')['Amount'].sum()
        fig, ax = plt.subplots()
        ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.write("### Incomes by Category:")
        st.pyplot(fig)
    else:
        st.write("No expenses added yet.")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Menu", "Login", "Expenses", "Incomes"])

# Display the selected page
if page == "Login":
    login_page()
elif page == "Expenses":
    expenses_page()
elif page == "Incomes":
    income_page()
elif page == "Menu":
    menu_page()