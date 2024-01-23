import streamlit as st
from faker import Faker
import pandas as pd
import numpy as np

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')

def specify_dims():

	col1, col2 = st.columns(2)
	with col1:
		columns = st.slider('Columns', min_value=1, max_value=10, step=1, value=1)
	with col2:
		rows = st.select_slider('Rows', options=[1, 5, 10, 100, 1000, 10000, 100000], value=5)

	return columns, rows

def show_grid(columns, rows):

	names = []
	types = []

	for col in range(columns):
		
		col1, col2 = st.columns(2)
		with col1:
			names.append(st.text_input("Column Name", key=col))
		with col2:
			types.append(st.selectbox("Column Type", options=['Name', 'Address', 'SSN'], key=col+columns))

	data = dict(zip(names, types))

	return data

def main():

	# mappings = {'Name': faker.name(), 'Address': faker.address(), 'SSN': faker.ssn()}
	
	fake = Faker()

	columns, rows = specify_dims()

	data = show_grid(columns, rows)
	
	nkeys = sum(1 for key, value in data.items() if key)
	nvals = sum(1 for key, value in data.items() if value)

	if nkeys == nvals:

		df = pd.DataFrame(columns=data.keys())
		st.dataframe(df)
		st.write(data)
		
	#	for _ in rows:
			
	#		list = []
			
	#		for type in data.values():
	#			list.append(mappings[type])

	#	df = pd.concat([df, pd.DataFrame(list)])

if __name__ == '__main__':
	
	main()	
