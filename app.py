import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#LOGIN PAGE in progress 
#EXPENSES UPDATE PAGE in progress
#MENU PAGE in progress
#PAGE FOR EACH MENU OPTION

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

# Define pages:


tab1, tab2 = st.tabs(["🏠 Dashboard", "💰 Transactions"])

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
    st.write("Please enter your username and password")
    st.text_input("Username")
    st.text_input("Password")
    st.write("Login Successful")

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
    #if total_spent > weekly_budget:
     #   st.write("You have exceeded your weekly budget. We recommend the following:")

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
#st.sidebar.title("Navigation")
#page = st.sidebar.radio("Go to", ["Menu", "Login", "Expenses", "Incomes"])

# Display the selected page
# if page == "Login":
#     login_page()
# elif page == "Expenses":
#     expenses_page()
# elif page == "Incomes":
#     income_page()
# elif page == "Menu":
#     menu_page()

with tab1:
    st.write("Welcome to the Dashboard!")
    login_page()
    menu_page()

with tab2:
    st.write("Welcome to the Transactions page!")
    expenses_page()
    income_page()
    # Display the selected page
    # if page == "Login":
    #     login_page()
    # elif page == "Expenses":
    #     expenses_page()
    # elif page == "Incomes":
    #     income_page()
    
    css = """
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:1.2rem;
        }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)