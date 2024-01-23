import streamlit as st

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
			types.append(st.selectbox("Column Type", options=['Name', 'Address', 'SSN', 'IPv4 Address', 'Company', 'Datetime', 'Phone Number', 'Job', 'Currency'], key=col+columns))

	data = dict(zip(names, types))

	return data

def gen_fake(type):

	from faker import Faker
	from faker.providers import internet

	fake = Faker()
	fake.add_provider(internet)

	if type == 'Name':
		return fake.name()
	if type == 'Address':
		return fake.address()
	if type == 'SSN':
		return fake.ssn()
	if type == 'Datetime':
		return fake.date_time()
	if type == 'IPv4 Address':
		return fake.ipv4_private()
	if type == 'Company':
		return fake.company()
	if type == 'Phone Number':
		return fake.phone_number()
	if type == 'Job':
		return fake.job()
	if type == 'Currency':
		return fake.currency()
	return False

def main():

	import pandas as pd

	columns, rows = specify_dims()

	data = show_grid(columns, rows)

	st.write(data)

	keys = [key for key, value in data.items()]
	vals = [value for key, value in data.items()]
	
	nkeys = len(keys) #sum(1 for key, value in data.items() if key)
	nvals = len(vals) #sum(1 for key, value in data.items() if value)

	if nkeys == nvals:

		df = pd.DataFrame(columns=keys)
		
		for _ in range(rows):

			info = []

			for key in keys:

				info += gen_fake(vals[keys.index(key)])

			df = pd.concat([df, info], axis=0)

		st.dataframe(df)

	df.to_csv('rwfd.csv', ignore_index=True)
	st.write(f'Wrote {columns:,} columns x {rows:,} columns dataframe to rwfd.csv')

if __name__ == '__main__':
	
	main()	
