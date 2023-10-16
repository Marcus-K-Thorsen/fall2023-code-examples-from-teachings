db = {
    "Audi": {"A3", "A4", "A6", "Q5", "Q7"},
    "BMW": {"3 Series", "5 Series", "7 Series", "X3", "X5"},
    "Mercedes-Benz": {"C-Class", "E-Class", "S-Class", "GLC", "GLE"},
    "Volkswagen": {"Golf", "Passat", "Polo", "Tiguan", "Arteon"},
    "Volvo": {"S60", "S90", "V60", "XC60", "XC90"},
    "Toyota": {"Corolla", "Camry", "RAV4", "Prius", "Hilux"},
    "Honda": {"Civic", "Accord", "CR-V", "Fit", "HR-V"},
    "Ford": {"Focus", "Fiesta", "Mustang", "Escape", "Explorer"},
    "Nissan": {"Altima", "Rogue", "Sentra", "Maxima", "Murano"},
    "Mazda": {"Mazda3", "Mazda6", "CX-5", "CX-9", "MX-5"}
}

class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    def get_db(self):
        return db
    
    @property
    def make(self):
        return self.make
    
    @make.setter
    def make(self, make):
        self.make = make