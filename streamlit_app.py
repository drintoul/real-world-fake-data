import streamlit as st
from faker import Faker
import pandas as pd

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')
st.subheader('Generate Fake data in CSV')

def main():

	fake = Faker()

	for _ in range(10):
		st.write(fake.name())

if __name__ == '__main__':
	
	main()	
