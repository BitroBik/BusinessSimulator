Office_Decode = {
    'Normal': 100,
    'Automatic': 1200,
    'Large': 2400
}

Tax_Decode = {
    1: 1.0,
    2: 1.1,
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
        self.money = 2500
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
    
    def Demolish_Office(self, name):
        for office in self.offices:
            if office.name == name:
                self.office.remove(name)
    
    def Buy_Office(self, name):
        print('1. Normal 2,500$ \n 2. Automatic 18,000 \n 3. Large 72,000')
        Type = input('Type: ')
        
        if Type == 1:
            if self.money >= 2500:
                self.offices.append(Office(input('Name of Office: '), 'Normal'))
            else:
                print('Not enough money:')
        elif Type == 2:
            if self.money >= 18000:
                self.offices.append(Office(input('Name of Office: '), 'Automatic'))
            else:
                print('Not enough money:')
        elif Type == 3:
            if self.money >= 72000:
                self.offices.append(Office(input('Name of Office: '), 'Large'))
            else:
                print('Not enough money:')
        else:
            print('Type Doesnt Exist pick 1, 2, 3:')
        
class Office:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.lvl = 1
        self.price = 1200
        
        self.tax = Office_Decode[self.type] * Tax_Decode[self.lvl]
    
    def Upgrade(self, name, business):
        if business.money >= self.price:
            self.lvl += 1
            self.tax = Office_Decode[self.type] * Tax_Decode[self.lvl]
            self.price = self.price * 2
            
            print(f'Upgraded to lvl {self.lvl}')
        else:
            print('Cannot upgrade: Not enough money')

