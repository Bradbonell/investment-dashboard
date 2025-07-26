# investment_dashboard/modules/business_finder.py
import pandas as pd
import random

def scan_all_businesses(min_roi):
    categories = [
        "Laundromat", "Coffee Shop", "Car Wash", "Auto Repair", "Franchise Restaurant",
        "Nail Salon", "Hair Salon", "Fitness Center", "Dog Grooming", "Daycare",
        "Mobile Car Wash", "Landscaping", "Cleaning Services", "Tutoring Center", "Digital Marketing Agency",
        "eCommerce Store", "Smoke Shop", "Liquor Store", "Convenience Store", "Thrift Store",
        "Boutique", "Photography Studio", "Food Truck", "Yoga Studio", "Dance Studio",
        "Vending Machine Business", "Boba Shop", "Ice Cream Parlor", "Catering Company", "Event Rental Service",
        "Dry Cleaner", "Gas Station", "RV Rental", "Boat Rental", "Property Management",
        "Accounting Firm", "Insurance Agency", "Travel Agency", "Courier Business", "Art Studio",
        "IT Services", "Bike Shop", "Pet Store", "Pawn Shop", "Window Tinting",
        "Custom T-Shirts", "Embroidery", "Auto Detailing", "Repair Technician", "Notary Services"
    ]

    businesses = []

    for category in categories:
        for i in range(2):  # Simulate 2 listings per category
            biz_name = f"{category} #{random.randint(100, 999)}"
            purchase_price = random.randint(10000, 150000)
            annual_profit = purchase_price * random.uniform(0.5, 1.5)
            roi = (annual_profit / purchase_price)

            if roi >= min_roi:
                businesses.append({
                    "Business": biz_name,
                    "Category": category,
                    "Purchase Price": purchase_price,
                    "Annual Profit": round(annual_profit, 2),
                    "ROI": round(roi * 100, 2),
                    "Listing URL": f"https://bizbuysell.com/{category.replace(' ', '-').lower()}/{biz_name.replace(' ', '-').lower()}"
                })

    return pd.DataFrame(businesses)
