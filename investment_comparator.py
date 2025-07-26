import pandas as pd

def compare_investments(stocks_df, items_df, businesses_df, real_estate_df):
    stocks_df['Type'] = 'Stocks'
    items_df['Type'] = 'Used Items'
    businesses_df['Type'] = 'Businesses'
    real_estate_df['Type'] = 'Real Estate'

    combined_df = pd.concat([stocks_df, items_df, businesses_df, real_estate_df], ignore_index=True)

    if 'ROI' not in combined_df.columns:
        raise ValueError("Missing ROI column in combined data.")

    top_investments = combined_df.sort_values(by="ROI", ascending=False).head(50)

    return top_investments[["Type", "Item", "Category", "Purchase Price", "Estimated Resale", "ROI", "Listing URL"]]
