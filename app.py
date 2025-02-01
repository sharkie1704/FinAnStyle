
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Welcome to the Fine-Ance and Budgeting App!")
st.write("This is your first step towards a better financial life (hopefully).")

if "attendance" not in st.session_state:
    st.session_state.attendance = set()
def take_attendance():
    if st.session_state.name in st.session_state.attendance:
        st.info(f"{st.session_state.name} has already been counted.")
    else:
        st.session_state.attendance.add(st.session_state.name)


with st.form(key="my_form"):
    st.text_input("Name", key="name")
    st.form_submit_button("I'm ready to go!", on_click=take_attendance)

# Initialize session state if it's not already initialized
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Streamlit app layout
st.title("Personal Finance Tracker")

# Input fields for the user to enter expenses
expense_name = st.text_input("Expense Name", key="expenseName")
expense_amount = st.number_input("Expense Amount", min_value=0.01, format="%.2f",key="expenseAmount")
expense_category = st.selectbox("Expense Category", ["Food", "Transport", "Entertainment", "Bills", "Other"], key="expenseCategory")

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

# # Example: Adding HTML content
# html_code = """
#     <div style="background-color: lightblue; padding: 10px; text-align: center; border-radius: 10px;">
#         <h1 style="color: #003366;">Welcome to the Personal Finance Tracker</h1>
#         <p style="color: #333;">Track your expenses and manage your finances easily.</p>
#     </div>
# """
# css_code = """
#     <style>
#         body {
#             background-color: #f4f4f9;
#             font-family: 'Arial', sans-serif;
#         }
#         .header {
#             color: #003366;
#             font-size: 36px;
#             font-weight: bold;
#             text-align: center;
#             padding: 20px;
#         }
#         .button {
#             background-color: #4CAF50;
#             color: white;
#             border: none;
#             padding: 10px 24px;
#             text-align: center;
#             font-size: 16px;
#             cursor: pointer;
#             border-radius: 5px;
#         }
#         .button:hover {
#             background-color: #45a049;
#         }
#     </style>
# """
# st.markdown(html_code, unsafe_allow_html=True)
# st.markdown(css_code, unsafe_allow_html=True)