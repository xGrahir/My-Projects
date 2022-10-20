import pickle, types, glob, os

class Car:

    Cars = []

    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine
        Car.Cars.append(self)

    def __call__(self, model):
        self.model = model
        print("MODEL CHANGED")

    def __iadd__(self, other):
        if type(other) == str:
            model = self.model
            model += other
            return Car(self.brand, model, self.engine)

    def get_info(self):
        print("Model: {}".format(self.model))
        print("Brand: {}".format(self.brand))
        print("Engine: {}".format(self.engine))

    @staticmethod
    def globing(path):
        c = os.path.join(path, "*md")
        a = glob.glob(c)
        return a

class Truck(Car):

    def __init__(self,brand, model, engine, capacity):
        super().__init__(brand, model, engine)
        self.capacity = capacity

    def get_info(self):
        super().get_info()
        print("Capacity: {}".format(self.capacity))

    def save_to_file(self, path):
        with open(path, "wb") as f:
            pickle.dump(self, f)


Scania = Truck("Scania", "A", "5.0", "30t")
Scania.get_info()
Scania.save_to_file("object.md")

def add_new_object(cls, path):
    with open(path, "rb") as f:
        plik = pickle.load(f)
        a = cls.Cars.append(plik)
    print("file loaded")
    return a

Car.add_new_object = types.MethodType(add_new_object, Car)
Car.add_new_object("object.md")

for car in Car.Cars:
    car.get_info()
    print("\n")

print(Scania.globing(r"C:\Users\tomas\PycharmProjects\My-Projects"))

Scania("B")
Scania += "COCO"

Scania.get_info()
