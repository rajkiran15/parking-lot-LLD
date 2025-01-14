from vehicle import Vehicle, VehicleType
from parking_lot import ParkingLot

# Initialize parking lot
parking_lot = ParkingLot(num_floors=5, slots_per_floor=8)

# Create a vehicle
car = Vehicle("CAR123", VehicleType.CAR)

# Park the vehicle
ticket = parking_lot.park_vehicle(car)
print(f"Car parked with Ticket ID: {ticket.ticket_id}")

# Unpark the vehicle
fee = parking_lot.unpark_vehicle(ticket)
print(f"Car unparked. Fee: ${fee:.2f}")
