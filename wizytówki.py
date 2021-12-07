
class Names:
   def __init__(self, first_name, surname, company, position, email):
       self.first_name = first_name
       self.surname = surname
       self.company = company
       self.position = position
       self.email = email
       # Variables
#       self._name_len = 0
       

   def __str__(self):
       return f"{self.first_name} {self.surname} {self.email}"
   def contact(self):
       return print(f"Kontaktuję się z {self.first_name} {self.surname} {self.position} {self.email}")
   def name_len(self):
       return print(len(self.first_name) + len(self.surname) + 1)
#   @property
#   def name_len(self):
#       return self._name_len
#   @name_len.setter
#   def name_len(self, value):
#       value = len(self.first_name) + len(self.surname) + 1
#       if value >= self._name_len:
#          self._name_len = value
          
         
BanekM = Names(first_name="Magda", surname="Banek", company="House", position="CEO", email="magda.banek@house.pl")
BanekK = Names(first_name="Krzysztof", surname="Banek", company="House-Expeditions", position="KOW", email="krzysztof.banek@house.pl")
KrakowskiJ = Names(first_name="Jerzy", surname="Krakowski", company="Carpatia", position="President", email="jerzy.krakowski@carpatia.pl")
DobrowolskiE = Names(first_name="Edward", surname="Dobrowolski", company="Kielbasy", position="Tester", email="edward.dobrowolski@kielbasy.pl")
DudekM = Names(first_name="Maciej", surname="Dudek", company="Moonshine", position="Project_Manager", email="maciej.dudek@moonshine.pl")

Names_list = [BanekM, BanekK, KrakowskiJ, DobrowolskiE, DudekM]
by_first_name = sorted(Names_list, key=lambda name: name.first_name)
by_surname = sorted(Names_list, key=lambda name: name.surname)
by_email = sorted(Names_list, key=lambda name: name.email)

for name in Names_list:
    Names.name_len(name)
#print(BanekM.name_len)
