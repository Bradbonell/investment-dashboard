import pandas as pd
import random

def scan_all_used_items(min_roi):
    categories = [
        "Smartphones", "Laptops", "Tablets", "Cameras", "Headphones",
        "Gaming Consoles", "Video Games", "Graphics Cards", "Processors", "Monitors",
        "Keyboards", "Mice", "Printers", "3D Printers", "Drones",
        "Smartwatches", "TVs", "Projectors", "Home Theater Systems", "Routers",
        "Networking Equipment", "Power Tools", "Hand Tools", "Kitchen Appliances", "Microwaves",
        "Refrigerators", "Washing Machines", "Dryers", "Air Conditioners", "Heaters",
        "Bicycles", "Electric Scooters", "E-Bikes", "Car Parts", "Tires",
        "Furniture", "Office Chairs", "Desks", "Bookshelves", "Coffee Tables",
        "Antiques", "Collectibles", "Watches", "Handbags", "Shoes",
        "Musical Instruments", "DJ Equipment", "Speakers", "Vinyl Records", "Fitness Equipment",
        "Camping Gear", "Outdoor Grills", "Lawn Mowers", "Snow Blowers", "Baby Gear",
        "Board Games", "Toys", "LEGO Sets", "Model Kits", "Bicycles Parts",
        "RC Cars", "Telescopes", "Binoculars", "Sewing Machines", "Quilting Tools",
        "Fishing Gear", "Hunting Gear", "Paintball Equipment", "Surfboards", "Skateboards",
        "Scuba Gear", "Horse Riding Gear", "Gardening Tools", "Greenhouse Kits", "Aquariums",
        "Pet Supplies", "Cat Trees", "Dog Crates", "Pet Carriers", "Bird Cages",
        "Holiday Decorations", "Costumes", "Wedding Decor", "Lighting Fixtures", "Ceiling Fans",
        "Blenders", "Coffee Makers", "Juicers", "Toasters", "Slow Cookers",
        "Camera Lenses", "Tripods", "Flash Units", "Gimbals", "Action Cameras"
    ]

    item_data = []

    for category in categories:
        for i in range(3):  # Simulate 3 listings per category
            item = f"{category} {random.randint(1, 100)}"
            price = random.uniform(20, 500)
            resale_value = price * 2.0  # Double the investment
            roi = (resale_value - price) / price

            if roi >= min_roi:
                item_data.append({
                    "Item": item,
                    "Category": category,
                    "Purchase Price": round(price, 2),
                    "Estimated Resale": round(resale_value, 2),
                    "ROI": round(roi * 100, 2),
                    "Listing URL": f"https://example.com/{category.replace(' ', '_').lower()}/{item.replace(' ', '_').lower()}"
                })

    return pd.DataFrame(item_data)