from parking_floor import ParkingFloor
from ticket import Ticket
from payment import Payment
from datetime import datetime

class ParkingLot:
    def __init__(self, num_floors, slots_per_floor):
        self.floors = [ParkingFloor(i + 1, slots_per_floor) for i in range(num_floors)]

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            slot = floor.get_available_slot(vehicle.vehicle_type)
            if slot:
                slot.park()
                return Ticket(vehicle, slot)
        raise Exception("No parking slots available!")

    def unpark_vehicle(self, ticket):
        ticket.slot.unpark()
        exit_time = datetime.now()
        fee = Payment.calculate_fee(ticket.entry_time, exit_time)
        return fee
