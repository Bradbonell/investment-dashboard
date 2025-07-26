# investment_dashboard/modules/real_estate_finder.py
import pandas as pd
import random

def scan_all_real_estate(min_roi, zip_filter=None, zip_count=25):
    zip_codes = [f"{random.randint(90001, 96162)}" for _ in range(zip_count)]
    if zip_filter:
        zip_codes = zip_filter

    listings = []

    for zip_code in zip_codes:
        for i in range(4):  # Simulate 4 listings per zip
            address = f"{random.randint(100, 9999)} Main St, ZIP {zip_code}"
            price = random.randint(75_000, 500_000)
            annual_rent = price * random.uniform(0.05, 0.12)
            roi = annual_rent / price

            if roi >= min_roi:
                listings.append({
                    "Address": address,
                    "ZIP Code": zip_code,
                    "Price": price,
                    "Annual Rent": round(annual_rent, 2),
                    "ROI": round(roi * 100, 2),
                    "Listing URL": f"https://example.com/properties/{zip_code}/{address.replace(' ', '-').lower()}"
                })

    return pd.DataFrame(listings)
