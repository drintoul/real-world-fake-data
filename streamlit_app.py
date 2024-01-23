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
			types.append(st.selectbox("Column Type", options=['Name', 'Address', 'SSN', 'IPv4 Address', 'Company', 'Credit Card', 'Date_time', 'Geo', 'Phone Number', 'Job', 'Currency'], key=col+columns))

	data = dict(zip(names, types))

	return data

def main():

	import pandas as pd
	from faker import Faker
	from faker.providers import internet

	fake = Faker()
	fake.add_provider(internet)
	
	mappings = {'Name': 'name', 'Address': 'address', 'SSN': 'ssn', 'IPv4 address': 'ipv4_private', 'Company': 'company', 'Credit Card': 'credit_card', 'Datetime': 'date_time', 'Geo': 'geo', 'Phone Number': 'phone_number', 'Job':'job', 'Currency': 'currency'}

	columns, rows = specify_dims()

	data = show_grid(columns, rows)
	
	nkeys = sum(1 for key, value in data.items() if key)
	nvals = sum(1 for key, value in data.items() if value)

	if nkeys == nvals:

		colnames = data.keys()
		df = pd.DataFrame(columns=colnames)
		
		for _ in range(rows):

			for mapping in mappings:
				item = exec("fake.{}()".format(mapping))
				st.write(item)

			#st.write([exec('fake.{}()'.format(mappings[item])) for item in data.values()])
			#row = pd.DataFrame([exec('fake.{}()'.format(mappings[item])) for item in data.values()]).T
			#st.write(row)
			#row.columns = colnames
			#df = pd.concat([df, row], axis=0)

		st.dataframe(df)

if __name__ == '__main__':
	
	main()	
