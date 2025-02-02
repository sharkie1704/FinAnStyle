import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state
if 'expenses' not in st.session_state:
    st.session_state.expenses = []
if 'incomes' not in st.session_state:
    st.session_state.incomes = []
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Main Menu"

# Set page configuration
st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load your logo
logo_url = "https://example.com/logo.png"  # Replace with the path to your logo

# Define pages:
tab1, tab2 = st.tabs(["🏠 Main Menu", "💰 Budgeting"])

# Main Menu Page
def menu_page():
    st.title("Welcome to the Fine-An-Style App!")
    st.image(logo_url, width=200)  # Display logo image
    
    st.write("""
        ### Take Control of Your Financial Future
        This app is designed to help you track your expenses, income, and savings goals in a simple, user-friendly way.
        
        **Why Choose Fine-An-Style?**
        - Easy-to-use budgeting tools.
        - Track your expenses and incomes in real-time.
        - Get insights with graphical data visualizations.
        - Personalized budget tracking based on your inputs.
        
        Ready to kickstart your budgeting journey?
    """)
    
    user_name = st.text_input("Your full name:")
    user_age = st.text_input("Your age:")
    user_education_status = st.selectbox("Your education status:", ["High School", "College", "University", "Post-Graduate"])
    
    if st.button("I'm ready to kickstart my budgeting journey!"):
        st.session_state.active_tab = "Budgeting"

# Expenses Page
def expenses_page():
    st.title("Expense Tracker")
    st.write("""
        Track your daily expenses and make better financial decisions.
    """)
    
    expense_name = st.text_input("Expense Name")
    expense_amount = st.number_input("Expense Amount", min_value=0.01, format="%.2f")
    expense_category = st.selectbox("Expense Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
    
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

# Conditionally render based on the active tab
if st.session_state.active_tab == "Main Menu":
    with tab1:
        menu_page()
    with tab2:
        st.write("Please go to the Main Menu tab first!")
else:
    with tab1:
        st.write("You can head over to the Budgeting tab!")
    with tab2:
        expenses_page()
        income_page()

# Apply custom CSS for modern theming and background gradient
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #2ecc71, #8e44ad);  /* Green to purple gradient */
        color: #FFFFFF;  /* White text for contrast */
        font-family: 'Helvetica Neue', sans-serif;
    }
    .css-1d391kg {
        background-color: #34495E;  /* Darker blue header */
        color: white;
    }
    .css-1d391kg a {
        color: white;
    }
    .css-1d391kg a:hover {
        color: #F39C12;  /* Orange hover */
    }
    .stButton>button {
        background-color: #F39C12;  /* Orange button */
        color: white;
        border-radius: 8px;
        border: none;
        font-size: 16px;
        padding: 12px 25px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #E67E22;  /* Darker orange on hover */
    }
    .stDataFrame>div>div>table {
        font-family: 'Arial', sans-serif;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .stDataFrame>div>div>table th {
        background-color: #2C3E50;  /* Darker header for tables */
        color: white;
    }
    .stDataFrame>div>div>table td {
        background-color: #ECF0F1;  /* Light gray for table rows */
    }
    .stDataFrame>div>div>table td:hover {
        background-color: #BDC3C7;  /* Highlight rows on hover */
    }
    .stTextInput>div>div>input {
        background-color: #34495E;  /* Dark input fields */
        color: white;
        border-radius: 6px;
    }
    .stTextInput>div>div>input:focus {
        border: 2px solid #F39C12;  /* Focus effect */
    }
    </style>
""", unsafe_allow_html=True)
