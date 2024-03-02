from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

Office_Decode = {
    'Normal': 10000,
    'Automatic': 70000,
    'Medium': 350000,
    'Factory': 900000,
    'Warehouse': 1600000,
    'Airport': 3200000,
    'Large': 7400000,
}

Gain_Decode = {
    'Normal': 17,
    'Automatic': 112,
    'Medium': 345,
    'Factory': 800,
    'Warehouse': 1280,
    'Airport': 2460,
    'Large': 4820,
}

Lvl_Decode = {
    1: 1.0,
    2: 1.8,
    3: 2.6,
    4: 3.4,
    5: 4.0
}    

class Officeform:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.lvl = 1
        self.price = Office_Decode[self.type]

kv_code = '''
<MainMenu>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint_y: 0.05
            Button:
                text: 'Credits'
                on_press: root.manager.current = 'credits'
                size_hint_y: 1
            
            Button:
                text: '?'
                size_hint_y: 1
                on_press: root.manager.current = 'help'
            
        Label:
            id: moneydisplay
            text: 'Money: 10,000'
            size_hint_y: 0.25
            height: '48dp'
       
        Button:
            text: 'Work'
            size_hint_y: 0.55
            height: '48dp'
            on_press: root.work()
       
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.15
            Button:
                text: 'Shop'
                size_hint_x: 0.5
                height: '48dp'
                on_press: root.gotoshop()
            Button:
                text: 'Manage'
                size_hint_x: 0.5
                height: '48dp'
                on_press: root.manager.current = 'manage_menu'

<ShopMenu>:
    BoxLayout:
        orientation: 'vertical'
        padding: '10dp'
        
        Label:
            text: 'Office Menu'
            size_hint_y: None
            height: '48dp'
            font_size: '18sp'
        
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: '10dp'
                
                Label:
                    text: '`'
               
                Label:
                    text: 'You can only buy 5 Offices.'
               
                Button:
                    text: 'Normal Office - 10,000'
                    size_hint_y: None
                    height: '48dp'
                    on_press: root.purchase_office('Normal')
                
                Button:
                    text: 'Automatic Office - 70,000'
                    size_hint_y: None
                    height: '48dp'
                    on_press: root.purchase_office('Automatic')
                
                Button:
                    text: 'Medium Office - 350,000'
                    size_hint_y: None
                    height: '48dp'
                    on_press: root.purchase_office('Medium')
                
                Button:
                    text: 'Factory - 900,000'
                    size_hint_y: None
                    height: '48dp'
                    on_press: root.purchase_office('Factory')
                
                Button:
                    text: 'Warehouse - 1,600,000'
                    size_hint_y: None
                    height: '48dp'
                    on_press: root.purchase_office('Warehouse')
                
                Button:
                    text: 'Airport - 3,200,000'
                    size_hint_y: None
                    height: '48dp'
                    on_press: root.purchase_office('Airport')
                
                Button:
                    text: 'Large Office - 7,400,000'
                    size_hint_y: None
                    height: '48dp'
                    on_press: root.purchase_office('Large')
                    
        Button:
            text: 'Back'
            size_hint_y: None
            height: '48dp'
            on_press: root.manager.current = 'main_menu'   

<ManageMenu>:
    BoxLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.3
            size_hint_y: 1

            id: office_list
       
        BoxLayout:
            orientation: 'vertical' 
            size_hint_x: 0.7
            size_hint_y: 1
            
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: 0.7
                size_hint_x: 1
               
                Label:
                    id: names
                    text: 'Name: Loading'
                    
                Label:
                    id: levels
                    text: 'Level: Loading'
                
                Label:
                    id: price
                    text: 'Price: Loading'
            
            BoxLayout:
                orientation: 'horizontal'
                size_hint_x: 1
                size_hint_y: 0.3
                Image:
                    source: 'city.png'
                    
                Button:
                    text: 'Upgrade'
                    on_press: root.upgrade()
                
                Button:
                    text: 'Demolish'
                    on_press: root.demolish()
                
                Button:
                    text: 'Exit'
                    on_press: root.manager.current = 'main_menu'            
<Credits>:
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            text: 'BitroBik - Dev - GitHub'
        
        Label:
            text: 'BitroBik - Dev - Roblox'
        
        Label:
            text: 'KylePandaRoblox - Dev - Roblox'
        
        Label:
            text: 'JustSomeRandomAcc326 - Veto - Roblox'
        
        Label:
            text: 'Ashl123smith - Tester - Roblox'
        
        Button:
            text: 'X'
            on_press: root.manager.current = 'main_menu'

<Help>:
    BoxLayout:
        orientation: 'vertical'
        
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: '10dp'
                
                Label:
                    text: '`'
                    
                Label:
                    text: 'How to start. first Buy a Office'
                
                Image:
                    source: '1.png'
                    size_hint: None, None
                    size: 600, 600
                
                Label:
                    text: 'Now that you bought a Office you need to have more money to buy more office'
                
                Image:
                    source: '2.png'
                    size_hint: None, None
                    size: 600, 600
                
                Label:
                    text: 'Now you can now progress into the next office'
                    
                Image:
                    source: '3.png'
                    size_hint: None, None
                    size: 600, 600
        Button:
            text: 'X'
            size_hint_y: 0.2
            on_press: root.manager.current = 'main_menu'    
                    
'''

Builder.load_string(kv_code)

class MainMenu(Screen):
    def work(self):
        app = App.get_running_app()
        
        self.gain = 0
        for office in app.offices:
              self.gain += Gain_Decode[office.type]*Lvl_Decode[office.lvl]
        
        app.money += self.gain
        self.ids.moneydisplay.text = f'Money: {format(app.money, ",")}'

    def gotoshop(self):
        self.manager.current = 'shop_menu'

class ShopMenu(Screen):
    def purchase_office(self, office_type):
        app = App.get_running_app()
        
        if len(app.offices) != 5:
            if app.money >= Office_Decode[office_type]:
                app.money -= Office_Decode[office_type]
                if office_type not in ['Factory', 'Warehouse', 'Airport']:
                    a = Officeform(f'{office_type} Office', office_type)
                else:
                    a = Officeform(f'{office_type}', office_type)
                    
                app.offices.append(a)
                self.parent.get_screen('main_menu').ids.moneydisplay.text = f'Money: {format(app.money, ",")}'
                self.parent.get_screen('manage_menu').update_building_soon(a)
            else:
                print('Insufficient funds')
    
class ManageMenu(Screen):
    def update_building_soon(self, office):
        app = App.get_running_app()
        self.ids.office_list.clear_widgets()
        
        for office_item in app.offices:
            office_button = Button(text=office_item.name)
            office_button.bind(on_press=lambda instance, office=office_item: self.update(office))
            office_button.bind(on_press=lambda instance, office=office_item: setattr(app, 'selected', office_item))
            self.ids.office_list.add_widget(office_button)
        
        self.ids.office_list.height = self.ids.office_list.minimum_height
    
    def update_building_limited(self):
        app = App.get_running_app()
        self.ids.office_list.clear_widgets()
        
        for office_item in app.offices:
            office_button = Button(text=office_item.name)
            office_button.bind(on_press=lambda instance, office=office_item: self.update(office))
            office_button.bind(on_press=lambda instance, office=office_item: setattr(app, 'selected', office_item))
            self.ids.office_list.add_widget(office_button)
        
        self.ids.office_list.height = self.ids.office_list.minimum_height
        
    def update(self, office):
        app = App.get_running_app()
        self.ids.names.text = f'Name: {office.name}'
        self.ids.levels.text = f'Level: {office.lvl}'
        self.ids.price.text = f'Price: {format(office.price, ",")}'
        app.selected = office
    
    def upgrade(self):
        app = App.get_running_app()
        
        try:
            if app.selected.lvl < 5:
                if app.money >= app.selected.price:
                    app.money -= app.selected.price
                    app.selected.lvl += 1
                    app.selected.price = app.selected.price * 2
                
                    self.ids.levels.text = f'Level: {office.lvl}'
                    self.ids.price.text = f'Price: {format(office.price, ",")}'
                    self.parent.get_screen('main_menu').ids.moneydisplay.text = f'Money: {format(app.money, ",")}'
        except:
            pass

    def demolish(self):
        app = App.get_running_app()
        
        try:
            for off in app.offices:
                if off == app.selected:
                    app.offices.remove(off)
                    self.update_building_limited()
                    break
        except:
            pass

class Credits(Screen):
    pass

class Help(Screen):
    pass
      
class BusinessSimulationApp(App):
    def build(self):
        self.money = 10000
        self.offices = []
        self.selected = None
        
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(ShopMenu(name='shop_menu'))
        sm.add_widget(ManageMenu(name='manage_menu'))
        sm.add_widget(Credits(name='credits'))
        sm.add_widget(Help(name='help'))
        
        return sm

if __name__ == '__main__':
    BusinessSimulationApp().run()