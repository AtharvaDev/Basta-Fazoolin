class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name 
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " Menu is available from " + str(self.start_time) + " to " + str(self.end_time)
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_items in purchased_items:
      if purchased_items in self.items:
        bill += self.items[purchased_items]

    return bill

##This class is used to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    
    for i in self.menus:
      if time >= i.start_time and time <= i.end_time:
        available_menus.append(i)

    return available_menus

class Business :
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu("brunch", brunch_items, 1100, 1600)

##TEST
#print(brunch_menu.name)
#print(brunch_menu.items)
#print(brunch_menu)
#print(brunch_menu.calculate_bill(['pancakes', 'home fries','coffee']))

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu("Early bird", early_bird, 1500, 1800)

##TEST
#print(early_bird_menu.name)
#print(early_bird_menu.items)
#print(early_bird_menu)
#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner, 1700, 2300)

##TEST
#print(dinner_menu.name)
#print(dinner_menu.items)
#print(dinner_menu)


kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu("kids", kids, 1100, 2100)



franchise_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("franchise", franchise_items, 1000, 2000)
##TEST
#print(kids_menu.name)
#print(kids_menu.items)
#print(kids_menu)


##Franchise class
menus = [brunch_menu, early_bird_menu ,dinner_menu, kids_menu]

##Franchise stores example
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

##TEST
#print(flagship_store)
#print(flagship_store.available_menus(1900))


## Business class
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa = Business("Take a' Arepa", [arepas_place])
print(arepa)

