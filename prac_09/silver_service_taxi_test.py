from silver_service_taxi import SilverServiceTaxi

# Create a new SilverServiceTaxi object
my_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Drive the taxi 18 km
my_taxi.drive(18)

# Calculate and print the fare
fare = my_taxi.get_fare()
print(my_taxi)
print(f"Fare: ${fare:.2f}")