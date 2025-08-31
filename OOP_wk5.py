# Assignment: Combined Script
# --- Smartphone Classes ---
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Private attribute
        self.battery = battery
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")
    def get_storage(self):
        return self.__storage
    def set_storage(self, storage):
        self.__storage = storage
        print(f"Storage updated to {self.__storage}GB")
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system.")

# --- Vehicle Classes ---
class Vehicle:
    def move(self):
        pass  # Generic method
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")
class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")
# Objects & Actions
# Smartphone objects
phone1 = Smartphone("Samsung", "Galaxy S23", 128, "4000mAh")
phone2 = GamingPhone("Asus", "ROG Phone 7", 256, "6000mAh", "Advanced Liquid Cooling")
print("--- Smartphones ---")
phone1.make_call("0712345678")
print(f"{phone1.brand} storage: {phone1.get_storage()}GB")
phone2.make_call("0798765432")
phone2.play_game("Call of Duty")
phone2.set_storage(512)
# Vehicle objects demonstrating polymorphism
vehicles = [Car(), Plane(), Boat()]
print("\n--- Vehicles ---")
for v in vehicles:
    v.move()
