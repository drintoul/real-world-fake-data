import streamlit as st
from faker import Faker
import pandas as pd

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')
st.subheader('Generate Fake data in CSV')

def main():

	rows = st.number_input('Enter number of rows desired', min_value=1, max_value=25, value=0, step=1)

	fake = Faker()

	for _ in range(rows+1):
		st.write(fake.name(), fake.address())

if __name__ == '__main__':
	
	main()	
