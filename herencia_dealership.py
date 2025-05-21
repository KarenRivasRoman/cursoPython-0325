class Vehicle:
    #encapsulacion
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} no esta disponible")

    #abstracción solo se puede acceder mediante los metodos
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
 #Herencia   
class Car(Vehicle):
    #Polimorfimos muchas formas pero comportamiento diferente
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
            
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no esta disponible"
            
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta  {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
            
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
        
            
class Truck(Vehicle):
    def start_engine(self):           
        if not self.is_available:
            return f"El motor del camión  {self.brand} está en marcha"
        else:
            return f"El  camión {self.brand} no esta disponible"
            
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión  {self.brand} se ha detenido"
        else:
            return f"El camión  {self.brand} no esta disponible"
            
class Customer:  
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    

    def buy_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo sieno {vehicle.brand} no esta disponile")

    def inquire_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory =[]
        self.customers = []

    def add_vehicles(self, vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehiculo {vehicle.brand} ha sido añadido al inventario")

    def register_curtomers(self, customer:Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.nam} ha sido añadido al inventario")

    def show_availables_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"El vehiculo {vehicle.brand} por {vehicle.price}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07",7000)
truck1 = Truck("Volvo", "FH16",80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_availables_vehicle()

#Cliente consultarun vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_availables_vehicle()


         
     
        
