# Part a: Create a travel itinerary planner
travel_itinerary = []

# Part b: Use lists to store destinations
destinations = ["Paris", "Tokyo", "New York", "Sydney", "Rome"]

# Part d: Use dictionaries to store details about each destination
destination_details = {
    "Paris": {
        "accommodation": "Hotel ABC",
        "activities": ["Visit Eiffel Tower", "Louvre Museum", "Seine River Cruise"],
        "travel_info": "Flight from your city to Paris"
    },
    "Tokyo": {
        "accommodation": "Ryokan XYZ",
        "activities": ["Explore Tokyo Tower", "Visit Asakusa Shrine", "Try sushi at Tsukiji Market"],
        "travel_info": "Direct flight from Paris to Tokyo"
    },
    "New York": {
        "accommodation": "City Hotel",
        "activities": ["Times Square", "Central Park", "Statue of Liberty"],
        "travel_info": "Flight from Tokyo to New York"
    },
    "Sydney": {
        "accommodation": "Harbor View Hotel",
        "activities": ["Sydney Opera House", "Bondi Beach", "Harbor Bridge Climb"],
        "travel_info": "Flight from New York to Sydney"
    },
    "Rome": {
        "accommodation": "Italian Villa",
        "activities": ["Colosseum", "Vatican City", "Trevi Fountain"],
        "travel_info": "Flight from Sydney to Rome"
    }
}

# Part c: Utilize loops to iterate through the itinerary
for destination in destinations:
    print(f"\n{destination} Itinerary:")
    print(f"Accommodation: {destination_details[destination]['accommodation']}")
    print("Activities:")
    for activity in destination_details[destination]['activities']:
        print(f"- {activity}")
    print(f"Travel Information: {destination_details[destination]['travel_info']}")
    print("----------------------")

# Outputting the entire itinerary
print("\nComplete Travel Itinerary:")
for destination in destinations:
    print(f"\n{destination} Itinerary:")
    print(f"Accommodation: {destination_details[destination]['accommodation']}")
    print("Activities:")
    for activity in destination_details[destination]['activities']:
        print(f"- {activity}")
    print(f"Travel Information: {destination_details[destination]['travel_info']}")
    print("----------------------")
