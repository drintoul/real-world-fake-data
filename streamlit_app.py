import streamlit as st
from faker import Faker
import pandas as pd

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')
st.subheader('Generate Fake data in CSV')

def main():

	rows = st.slider('Enter number of rows desired', 1, 25, 1)

	fake = Faker()

	if rows > 1:
		for _ in range(rows):
			st.write(fake.name(), '\t', fake.address())

if __name__ == '__main__':
	
	main()	
