class Clock:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._normalize()

    def _normalize(self) -> None:
        carry_minutes, seconds = divmod(self.seconds, 60)
        self.seconds = seconds
        self.minutes += carry_minutes
        carry_hours, minutes = divmod(self.minutes, 60)
        self.minutes = minutes
        self.hours += carry_hours
        self.hours = self.hours % 24
