class CAR:
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

Toyota = CAR(300, 100)
print(f"Toyota's max speed is {Toyota.maxSpeed}")
print(f"Toyota's mileage is {Toyota.mileage}\n")

Suzuki = CAR(220, 180)
print(f"Suzuki's max speed is {Suzuki.maxSpeed}")
print(f"Suzuki's mileage is {Suzuki.mileage}")