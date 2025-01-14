
class ParkingSlot:
    def __init__(self, slot_id, slot_type):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.is_available = True

    def park(self):
        if not self.is_available:
            raise Exception("Slot already occupied!")
        self.is_available = False

    def unpark(self):
        if self.is_available:
            raise Exception("Slot is already empty!")
        self.is_available = True
