import streamlit as st
from faker import Faker
import pandas as pd
import numpy as np

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')

col1, col2 = st.columns(2)
with col1:
	st.subheader('Generate Fake data in CSV')
with col2:
	st.button('Reset')

def create_matrix(rows, columns):
    matrix = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = st.number_input(f"Enter value for cell ({i+1}, {j+1})", key=f"{i}_{j}")
    return matrix

def main():
    st.title("Matrix Input App")

    # Get number of rows and columns from user
    rows = st.number_input("Enter number of rows", min_value=1, step=1)
    columns = st.number_input("Enter number of columns", min_value=1, step=1)

    # Create matrix input form
    matrix = create_matrix(rows, columns)

    # Display the input matrix
    st.table(matrix)

if __name__ == '__main__':
	
	main()	
