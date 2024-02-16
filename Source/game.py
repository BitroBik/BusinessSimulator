Office_Decode = {
    'Normal': 100,
    'Automatic': 800,
    'Large': 1600,
    'Factory': 3200,
    'Warehouse': 8000
}

Gain_Decode = {
    'Normal': 140,
    'Automatic': 1020,
    'Large': 2760,
    'Factory': 6400,
    'Warehouse': 10200
}

Employee_Decode = {
    'Normal': 2,
    'Automatic': 0,
    'Large': 6,
    'Factory': 12,
    'Warehouse': 8   
}

Exp_Decode = {
    1: 128,
    2: 256,
    3: 512,
    4: 1024,
}

Tax_Decode = {
    1: 1.0,
    2: 1.8,
    3: 2.6,
    4: 3.4,
    5: 4.0,
}

class Business:
    def __init__(self, name):
        self.name = name
        self.money = 2500
        self.offices = []
        self.tax = 0
    
    def Work(self):
        self.gain = 0
        for office in self.offices:
              self.gain += Gain_Decode[office.type]*Tax_Decode[office.lvl]
              
              for employee in office.employees:
                  self.gain += employee.give
                  
                  employee.exp += office.lvl*4
                  
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
                self.offices.remove(office)
    
    def Buy_Office(self):
        print('1. Normal 2,500$ \n2. Automatic 16,000 \n3. Large 40,000 \n4. Factory 80,000 \n5. Warehouse 160,000')
        Type = input('Type: ')
        
        if Type == '1':
            if self.money >= 2500:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Normal'))
                self.money -= 2500
            else:
                print('Not enough money:')
        elif Type == '2':
            if self.money >= 16000:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Automatic'))
                self.money -= 16000
            else:
                print('Not enough money:')
        elif Type == '3':
            if self.money >= 40000:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Large'))
                self.money -= 40000
            else:
                print('Not enough money:')
        elif Type == '4':
            if self.money >= 80000:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Factory'))
                self.money -= 80000
            else:
                print('Not enough money:')
        elif Type == '5':
            if self.money >= 160000:
                self.offices.append(Office(input('Name of Office: ').lower(), 'Warehouse'))
                self.money -= 160000
            else:
                print('Not enough money:')
        else:
            print('Type Doesnt Exist pick 1, 2, 3, 4, 5:')
    
    def Upgrade_Office(self):
        name = input('Name of Office: ').lower()
        for office in self.offices:
            if office.name == name:
                print(f'Cost: {office.price}')
                
                option = input('Buy Y/N: ').lower()
                
                if option == 'y':
                    office.Upgrade(self)
                else:
                    print('Did not Upgrade')

    def Hire_Employee(self):
        office_check = input('Name of Office:').lower()
        
        for office in self.offices:
            
            if office.name == office_check:
                print('Cost: 650')
                option = input('Buy Y/N: ').lower()
                
                if option == 'y':
                    office.Hire(self)
                else:
                    print('Did not Hire')
    
    def Fire_Employee(self):
        office_check = input('Name of Office:').lower()
        
        for office in self.offices:
            
            if office.name == office_check:
                option = input('Are you sure Y/N: ').lower()
                
                if option == 'y':
                    office.Fire()
                else:
                    print('Did not Fire')
            
                                             
class Office:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.lvl = 1
        self.price = Office_Decode[self.type]*12
        self.tax = Office_Decode[self.type]
        self.employee_count = Employee_Decode[self.type]
        self.employees = []
        
    def Upgrade(self, business):
        if self.lvl < 5:
            if business.money >= self.price:
                business.money -= self.price
                self.lvl += 1
                self.tax = Office_Decode[self.type]
                self.price = self.price * 2
                
                print(f'Upgraded to lvl {self.lvl}')
            else:
                print('Cannot upgrade: Not enough money')
        else:
            print('Max Level Reach')
            
    def Hire(self, business):
        if self.type != 'Automatic':
            if business.money >= 650 and self.employee_count < len(self.employees):
                business.money -= 650
                self.employees.append(Employee(input('Name of Employee: ').lower()))
            else:
                print('Not Enough Money Or Amount of Employee is Full')
        else:
            print('You cannot Hire an Employee in a Automatic Building') 
             
    def Fire(self):
        name = input('Name of Employee: ').lower()
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                
class Employee:
    def __init__(self, name):
        self.name = name
        self.give = 100
        self.salary = 60
        self.lvl = 1
        self.exp = 0
    
    def Update(self):
        if lvl != 5:
            if self.exp >= Exp_Decode[self.lvl]:
                self.exp = 0
                self.lvl += 1
                self.salary *= 2
                self.give *= 2
        
def Run_Game(debug=False):
    Tick = 0
    
    if not debug:
        Game = Business(input('Name of your Business: '))
    elif debug:
        Game = Business(input('Name of your Business: '))
   
    while True:
        print('----------------------------------')
        # Update
        gain = 0
        
        for office in Game.offices:
            if office.type == 'Automatic':
                gain += Office_Decode[office.type]*Tax_Decode[office.lvl]
            else:
                for employee in office.employees:
                    employee.Update()
                    
        Game.money += gain
        
        Game.Calculate_Tax()
        
        print(Tick)
        
        if Tick == 40:
            print('Autopaying Tax:')
            if Game.tax > Game.money:
                print('You are sent to Jail.')
                break
            else:
                Game.money -= Game.tax
                Game.tax = 0
            
            Tick = 0
        elif Tick >= 30:
            if Game.tax > Game.money:
                print('Your Money is lower then your tax. WORK')
            
            Tick += 1
        else:
            Tick += 1
        
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
            option = input('1. Office \n2. Employee \n:').lower()
            
            if option == '1':
                Game.Buy_Office()
            elif option == '2':
                Game.Hire_Employee()
                
        elif User == 'upgrade':
            Game.Upgrade_Office()
        elif User == 'demolish':
            Game.Demolish_Office()
        elif User == 'Fire':
            Game.Fire_Employee()
        elif User == 'stats':
            Game.Info()
        else:
            print(f'Unknown command {User}')