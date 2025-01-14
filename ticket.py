import uuid
from datetime import datetime

class Ticket:
    def __init__(self, vehicle, slot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.slot = slot
        self.entry_time = datetime.now()
