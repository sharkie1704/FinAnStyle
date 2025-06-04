import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state variables
if 'expenses' not in st.session_state:
    st.session_state.expenses = []
if 'incomes' not in st.session_state:
    st.session_state.incomes = []
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Main Menu"
if 'savings_goal' not in st.session_state:
    st.session_state.savings_goal = 0
if 'savings_progress' not in st.session_state:
    st.session_state.savings_progress = 0

# Set page configuration
st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define pages
tab1, tab2, tab3 = st.tabs(["🏠 Main Menu", "💰 Budgeting", "💸 Savings Goals"])

# Main Menu Page
def menu_page():
    st.title("Welcome to FineAnStyle!")
    # st.image(logo_url, width=200)  # Display logo image
    
    st.write("""
        ### Take Control of Your Financial Future
        This app is designed to help you track your expenses, incomes, and savings goals in a simple, user-friendly way.
        
        **Why Choose FineAnStyle?**
        - Easy-to-use budgeting tools.
        - Track your expenses and incomes in real-time.
        - Get insights with graphical data visualizations.
        - Personalized budget tracking based on your inputs.
        
        **Ready to kickstart your budgeting journey?**
    """)
    
    user_name = st.text_input("Your full name:")
    user_age = st.text_input("Your age:")
    user_education_status = st.selectbox("Your education status:", ["High School", "College", "University", "Post-Graduate"])
    
    if st.button("I'm ready!"):
        if user_name and user_age and user_education_status:
            st.session_state.active_tab = "Budgeting"
        else:
            st.error("Please fill in all the fields before proceeding.")

# Expenses Page
def expenses_page():
    st.title("Expense Tracker")
    st.write("""
        Track your daily expenses and make better financial decisions.
    """)
    
    expense_name = st.text_input("Expense Name")
    expense_amount = st.number_input("Expense Amount", min_value=0.01, format="%.2f")
    expense_category = st.selectbox("Expense Category", ["Food", "Transportation", "Entertainment", "Bills", "Other"])
    
    if st.button("Add Expense"):
        if expense_name and expense_amount > 0:
            st.session_state.expenses.append({
                'Name': expense_name,
                'Amount': expense_amount,
                'Category': expense_category
            })
            st.session_state.savings_progress -= expense_amount
            st.success(f"Added {expense_name} for ${expense_amount} under {expense_category} category.")
        else:
            st.error("Please enter valid expense details.")
    
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        st.write("### Your Expenses:")
        st.dataframe(df, use_container_width=True)
        
        total_spent = df['Amount'].sum()
        st.write(f"### Total Spent: ${total_spent:.2f}")

        category_totals = df.groupby('Category')['Amount'].sum()
        fig, ax = plt.subplots()
        ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90, colors=["#F1C40F", "#E74C3C", "#8E44AD", "#1ABC9C", "#2C3E50"])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.write("### Expenses by Category:")
        st.pyplot(fig)
    else:
        st.write("No expenses added yet.")

# Income Page
def income_page():
    st.title("Income Tracker")
    st.write("""
        Keep track of your income sources and set financial goals.
    """)
    
    income_name = st.text_input("Income Name")
    income_amount = st.number_input("Income Amount", min_value=0.01, format="%.2f")
    income_category = st.selectbox("Income Category", ["Salary", "Scholarship/Bursary", "Loans", "Bonus", "Gift", "Other"])
    
    if st.button("Add Income"):
        if income_name and income_amount > 0:
            st.session_state.incomes.append({
                'Name': income_name,
                'Amount': income_amount,
                'Category': income_category
            })
            st.session_state.savings_progress += income_amount
            st.success(f"Added {income_name} for ${income_amount} under {income_category} category.")
        else:
            st.error("Please enter valid income details.")
    
    if st.session_state.incomes:
        df = pd.DataFrame(st.session_state.incomes)
        st.write("### Your Incomes:")
        st.dataframe(df, use_container_width=True)
        
        total_gained = df['Amount'].sum()
        st.write(f"### Total Gained: ${total_gained:.2f}")
        
        category_totals = df.groupby('Category')['Amount'].sum()
        fig, ax = plt.subplots()
        ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90, colors=["#F39C12", "#2980B9", "#16A085", "#8E44AD", "#2ECC71"])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.write("### Incomes by Category:")
        st.pyplot(fig)
    else:
        st.write("No incomes added yet.")

# Savings Goals Page
def savings_page():
    st.title("Savings Goals")
    st.write("Set and track your savings goals.")
    savings_goal = st.number_input("Set your savings goal:", min_value=0.01, format="%.2f")
    if st.button("Set Savings Goal"):
        st.session_state.savings_goal = savings_goal
        st.success(f"Savings goal set to ${savings_goal:.2f}")
    st.write(f"### Current Savings Goal: ${st.session_state.savings_goal:.2f}")
    st.write(f"### Savings Progress: ${st.session_state.savings_progress:.2f}")
    if st.session_state.savings_goal > 0:
        progress_percentage = (st.session_state.savings_progress / st.session_state.savings_goal) * 100

# Conditionally render based on the active tab
if st.session_state.active_tab == "Main Menu":
    with tab1:
        menu_page()
    with tab2:
        st.write("Please go to the Main Menu tab first!")
    with tab3:
        st.write("Please go to the Main Menu tab first!")
else:
    with tab1:
        st.write("You can head over to the Budgeting tab!")
    with tab2:
        expenses_page()
        income_page()
    with tab3:
        savings_page()
