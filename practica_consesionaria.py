class Vehiculo:
    def __init__(self, brand, model, color, num_serie):
        self.brand = brand
        self.model = model
        self.color = color
        self.num_serie = num_serie
        self.available = True

    def Sale(self):
        if self.available:
            self.available = False
        else:
            print(f"El vehiculo ya no esta disponible")

    def Acquisition(self):
        self.available = True
        print(f"El vehiculo marca {self.brand} y modelo {self.model} fue adquirido")

class Cliente:
    def __init__(self, id, name, last_name, phone_number):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.Cars = []

    def buy_car(self,car):
        if car.available:
            car.Sale()
            self.Cars.append(car)
            print(f"El Vehiculo  marca {car.brand} y modelo {car.model} fue vendido")
        else:
            print("El Vehiculo no esta disponible")

    def Sale_car(self, car):
        if car in self.Cars:
            car.Acquisition()
            self.Cars.remove(car)
            print("El auto fue vendido a la consesionaria")

class Consesionaria:
    def __init__(self):
        self.cars = []
        self.users = []

    def add_cars(self, car):
        self.cars.append(car)
        print(f"El vehiculo Marca {car.brand}, modelo {car.model}, color {car.color} con numero de serie {car.num_serie} fue registrado")

    def add_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_cars_availables(self):
        print("Vehiculos disponibles:")
        for car in self.cars:
            if car.available:
                print(f"vehiculo Marca {car.brand}, modelo {car.model}, color {car.color} con numero de serie {car.num_serie}")

vehiculo1 = Vehiculo("Toyota","Corolla 2022","silver","02154646")
vehiculo2 = Vehiculo("Ford","F-150 XLT 2023","blue","02154786")

client1 = Cliente("001","Karen","Rivas","2254876545")

consesionaria1  = Consesionaria()
consesionaria1.add_cars(vehiculo1)
consesionaria1.add_cars(vehiculo2)
consesionaria1.add_user(client1)

consesionaria1.show_cars_availables()

client1.buy_car(vehiculo2)

consesionaria1.show_cars_availables()

client1.Sale_car(vehiculo2)
consesionaria1.show_cars_availables()


        

