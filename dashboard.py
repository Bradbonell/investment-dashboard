import streamlit as st
from modules import stock_analysis, used_item_finder, business_finder, real_estate_finder, investment_comparator

st.title("📈 Investment Opportunity Dashboard")

min_roi = st.slider("Minimum ROI (%)", 0, 200, 20)
zip_filter = st.text_input("Filter by Zip Code (comma separated)", "")
zip_list = [z.strip() for z in zip_filter.split(",") if z.strip()]

with st.spinner("🔍 Analyzing investments..."):
    stocks_df = stock_analysis.scan_all_stocks(min_roi / 100)
    items_df = used_item_finder.scan_all_items(min_roi / 100)
    businesses_df = business_finder.scan_all_businesses(min_roi / 100)
    real_estate_df = real_estate_finder.scan_all_real_estate(min_roi / 100, zip_list)

best_df = investment_comparator.find_best_investments(stocks_df, items_df, businesses_df, real_estate_df)

st.header("📊 Stock Opportunities")
st.dataframe(stocks_df)

st.header("🛒 Used Item Arbitrage")
st.dataframe(items_df)

st.header("🏢 Private Businesses for Sale")
st.dataframe(businesses_df)

st.header("🏘️ Real Estate Opportunities")
st.dataframe(real_estate_df)

st.header("🏆 Best Investment Picks")
st.dataframe(best_df)