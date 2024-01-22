import streamlit as st
import pandas as pd

st.set_page_config(page_title="Canada/US Gas Price Comparison")
st.title('Canada/US Gas Price Comparison')
st.subheader('Calculate gas prices including currency exchange')

def main():

	@st.cache_data(ttl=3600*6)
	def fetch_exchange_rate():

		dfs = pd.read_html("https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates")
		df = dfs[0]
		df = df[df['Currency'] == 'US dollar']
		asof = df.columns[-1]
		return df, asof

	df, asof = fetch_exchange_rate()

	cdn = st.toggle("Start with Canadian Dollars", value=True)

	usd2cdn = df.iloc[-1, -1]
	cdn2usd = round(1 / usd2cdn, 4)

	st.write("""Exchange Rate from Bank of Canada:
	https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates""")

if ____ == 'main':

  main()
