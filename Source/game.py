Office_Decode = {
    'Normal': 100,
    'Automatic': 1200,
    'Large': 2400
}

Tax_Decode = {
    1: 1.1,
    2: 1.2,
    3: 1.3,
    4: 1.4,
    5: 1.5,
    6: 1.6,
    7: 1.7,
    8: 1.8,
    9: 1.9,
    10: 2.0
}

class Business:
    def __init__(self, name):
        self.name = name
        self.money = 10000
        self.offices = []
        self.tax = 0
        
    def Info(self):
        print(f'{self.name} Info')
        print(f'Money: {format(self.money, ",")}')
        
        self.names = []
        for office in self.offices:
            self.names.append(office.name)
        print(f'Offices: {self.names}')
        
        print(f'Taxxes: {self.tax}') 
        
    def Calculate_Tax(self):
        for office in self.offices:
            self.tax += office.tax

class Office:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl
        
        self.tax = Office_Decode[self.type] * Tax_Decode[self.lvl]