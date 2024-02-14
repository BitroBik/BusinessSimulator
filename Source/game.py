Office_Decode = {
    'Normal': 100,
    'Automatic': 1200,
    'Large': 2400
}

Tax_Decode = {
    1: 1.4,
    2: 1.8,
    3: 2.2,
    4: 2.6,
    5: 3.0,
}

class Business:
    def __init__(self, name):
        self.name = name
        self.money = 18000
        self.offices = []
        self.tax = 0
    
    def Work(self):
        self.gain = 0
        for office in self.offices:
              self.gain += Office_Decode[office.type]*Tax_Decode[office.lvl]
        
        self.money += self.gain
        print(f'Gained {self.gain}. Money is now {self.money}') 
              
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
    
    def Demolish_Office(self):
        name = input('Name of Office: ').lower()
        for office in self.offices:
            if office.name == name:
                self.office.remove(name)
    
    def Buy_Office(self):
        print('1. Normal 2,500$ \n2. Automatic 18,000 \n3. Large 72,000')
        Type = input('Type: ')
        
        if Type == '1':
            if self.money >= 2500:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Normal'))
                self.money -= 2500
            else:
                print('Not enough money:')
        elif Type == '2':
            if self.money >= 18000:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Automatic'))
                self.money -= 18000
            else:
                print('Not enough money:')
        elif Type == '3':
            if self.money >= 72000:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Large'))
                self.money -= 72000
            else:
                print('Not enough money:')
        else:
            print('Type Doesnt Exist pick 1, 2, 3:')
    
    def Upgrade_Office(self):
        name = input('Name of Office: ').lower()
        for office in self.offices:
            if office.name == name:
                print(f'Cost: {office.price}')
                
                option = input('Buy Y/N: ').lower()
                
                if option == 'y':
                    office.Upgrade(self)
                     
class Office:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.lvl = 1
        self.price = Office_Decode[self.type]*12
        self.tax = Office_Decode[self.type]
    
    def Upgrade(self, business):
        if business.money >= self.price:
            business.money -= self.price
            self.lvl += 1
            self.tax = Office_Decode[self.type]
            self.price = self.price * 2
            
            print(f'Upgraded to lvl {self.lvl}')
        else:
            print('Cannot upgrade: Not enough money')

def Run_Game(debug=False):
    Tick = 0
    Game = Business(input('Name of your Business: '))
    
    while True:
        print('----------------------------------')
        # Update
        gain = 0
        
        for office in Game.offices:
            if office.type == 'Automatic':
                gain += Office_Decode[office.type]*Tax_Decode[office.lvl]
        Game.money += gain
        
        Game.Calculate_Tax()
        
        if Tick == 60:
            print('Autopaying Tax:')
            if Game.tax > Game.money:
                print('You are sent to Jail.')
                break
            else:
                Game.money -= Game.tax
                Game.tax = 0
            
            Tick = 0
        elif Tick <= 40:
            if Game.tax > Game.money:
                print('Your Money is lower then your tax. WORK')
        
        # Input
        User = input('Action: ').lower()
        
        if User == 'help':
            print('Work - Work for money.')
            print('Buy - Buy office.')
            print('Upgrade - Upgrade office.')
            print('Demolish - Destroy useless office.')
            print('Stats - Display your stats.')
        elif User == 'work':
            Game.Work()
        elif User == 'buy':
            Game.Buy_Office()
        elif User == 'upgrade':
            Game.Upgrade_Office()
        elif User == 'demolish':
            Game.Demolish_Office()
        elif User == 'stats':
            Game.Info()