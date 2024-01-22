import streamlit as st
from faker import Faker
import pandas as pd

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')
st.subheader('Generate Fake data in CSV')

def main():

	fake = Faker()

	col1, col2 = st.columns(2)
	with col1:
		st.write('Reset')
	with col2:
		rows = st.slider('Enter number of rows desired', 1, 25, 1)
	
	df = pd.DataFrame()
	df.columns = ['Name', 'Address', 'Birthdate']

	if rows > 1:
		for _ in range(rows):
			df = df.concat([df, pd.DataFrame((fake.name(), fake.address(), fake.date()))], hide_index=True)

	st.dataframe(df)

							 
if __name__ == '__main__':
	
	main()	
