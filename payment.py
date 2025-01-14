
class Payment:
    @staticmethod
    def calculate_fee(entry_time, exit_time):
        duration = (exit_time - entry_time).total_seconds() / 60  
        return duration * 2.0  
