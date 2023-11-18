class WaterBottle:
    def __init__(self, max_capacity=2.0) -> None:
        self.max_capacity = max_capacity
        self.current_contents = 0.0

    def fill(self) -> None:
        self.current_contents = self.max_capacity

    def drink(self, amount: float) -> float:
        extracted_amount = max(0, min(amount, self.current_contents))
        assert 0 <= extracted_amount <= self.current_contents

        self.current_contents -= extracted_amount
        return extracted_amount

    def __str__(self) -> str:
        return f"The bottle currently holds {self.current_contents:.1f}L of water."
