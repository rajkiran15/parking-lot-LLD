
from parking_slot import ParkingSlot
from vehicle import VehicleType

class ParkingFloor:
    def __init__(self, floor_number, slots_per_floor):
        self.floor_number = floor_number
        # for simplicity assuming each slot on each floor consists of vehicle type as car
        self.slots = [
            ParkingSlot(f"{floor_number}-{i+1}", VehicleType.CAR) for i in range(slots_per_floor)
        ]

    def get_available_slot(self, vehicle_type):
        for slot in self.slots:
            if slot.is_available and slot.slot_type == vehicle_type:
                return slot
        return None
