import streamlit as st
from faker import Faker
import pandas as pd

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')

col1, col2 = st.columns(2)
with col1:
	st.subheader('Generate Fake data in CSV')
with col2:
	st.button('Reset')

def main():

	fake = Faker()

	rows = st.slider('Enter number of rows desired', 1, 25, 1)

	columns=['Name', 'Address', 'Birthdate', 'SIN', 'IP Address']
	df = pd.DataFrame(columns=columns)

	if rows > 1:
		for _ in range(rows):

			data = [fake.name(), fake.address(), fake.date(), fake.ssn(), fake.ipv4_private()]

			for col in range(len(columns)):
				key = columns[col]
				val = data[col]
				dict[key] = val

			df = pd.append(dict, ignore_index=True)

	st.dataframe(df) #, hide_index=True)

							 
if __name__ == '__main__':
	
	main()	
