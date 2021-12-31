
class Names:
   def __init__(self, first_name, surname, company, position, email, phone, company_phone):
       self.first_name = first_name
       self.surname = surname
       self.company = company
       self.position = position
       self.email = email
       self.phone = phone
       self.company_phone = company_phone
       # Variables
#      self.name_len = 0

class BaseContact(Names):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
    def __str__(self):
       return f"{self.first_name} {self.surname} {self.phone} {self.email}"

    def contact(self):
       return print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.surname}")
    
    @property      #zamiana metody w argument
    def label_lenght(self):
       return (len(self.first_name) + len(self.surname) + 1)


class BusinessContact(Names):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.surname} {self.phone} {self.email} {self.company} {self.position} {self.company_phone}"
    
    def contact(self):
       return print(f"Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.surname}")

    #def label_length(self):
    #   return print(len(self.first_name) + len(self.surname) + 1)
    @property      #zamiana metody w argument
    def label_lenght(self):
       return (len(self.first_name) + len(self.surname) + 1)
#   @name_len.setter
#   def name_len(self, value):
#       value = len(self.first_name) + len(self.surname) + 1
#       if value >= self._name_len:
#          self._name_len = value
          
         
banekm = Names(first_name="Magda", surname="Banek", company="House", position="CEO", email="magda.banek@house.pl", phone="654247985", company_phone="17111444555")
banekk = Names(first_name="Krzysztof", surname="Banek", company="House-Expeditions", position="KOW", email="krzysztof.banek@house.pl", phone="654985122", company_phone="17222333444")
krakowskij = Names(first_name="Jerzy", surname="Krakowski", company="Carpatia", position="President", email="jerzy.krakowski@carpatia.pl", phone="699555444", company_phone="17444333222")
dobrowolskie = Names(first_name="Edward", surname="Dobrowolski", company="Kielbasy", position="Tester", email="edward.dobrowolski@kielbasy.pl", phone="611582741", company_phone="17321654987")
dudekm = Names(first_name="Maciej", surname="Dudek", company="Moonshine", position="Project_Manager", email="maciej.dudek@moonshine.pl", phone="678123456", company_phone="17235417896")

banekm1 = BaseContact(first_name="Magda", surname="Banek", company="House", position="CEO", email="magda.banek@house.pl", phone="654247985", company_phone="17111444555")
banekk1 = BaseContact(first_name="Krzysztof", surname="Banek", company="House-Expeditions", position="KOW", email="krzysztof.banek@house.pl", phone="654985122", company_phone="17222333444")
krakowskij1 = BaseContact(first_name="Jerzy", surname="Krakowski", company="Carpatia", position="President", email="jerzy.krakowski@carpatia.pl", phone="699555444", company_phone="17444333222")
dobrowolskie1 = BaseContact(first_name="Edward", surname="Dobrowolski", company="Kielbasy", position="Tester", email="edward.dobrowolski@kielbasy.pl", phone="611582741", company_phone="17321654987")
dudekm1 = BaseContact(first_name="Maciej", surname="Dudek", company="Moonshine", position="Project_Manager", email="maciej.dudek@moonshine.pl", phone="678123456", company_phone="17235417896")

banekm2 = BusinessContact(first_name="Magda", surname="Banek", company="House", position="CEO", email="magda.banek@house.pl", phone="654247985", company_phone="17111444555")
banekk2 = BusinessContact(first_name="Krzysztof", surname="Banek", company="House-Expeditions", position="KOW", email="krzysztof.banek@house.pl", phone="654985122", company_phone="17222333444")
krakowskij2 = BusinessContact(first_name="Jerzy", surname="Krakowski", company="Carpatia", position="President", email="jerzy.krakowski@carpatia.pl", phone="699555444", company_phone="17444333222")
dobrowolskie2 = BusinessContact(first_name="Edward", surname="Dobrowolski", company="Kielbasy", position="Tester", email="edward.dobrowolski@kielbasy.pl", phone="611582741", company_phone="17321654987")
dudekm2 = BusinessContact(first_name="Maciej", surname="Dudek", company="Moonshine", position="Project_Manager", email="maciej.dudek@moonshine.pl", phone="678123456", company_phone="17235417896")

names_list = [banekm, banekk, krakowskij, dobrowolskie, dudekm]
names_list1 = [banekm1, banekk1, krakowskij1, dobrowolskie1, dudekm1]
names_list2 = [banekm2, banekk2, krakowskij2, dobrowolskie2, dudekm2]

by_first_name = sorted(names_list, key=lambda name: name.first_name)
by_surname = sorted(names_list, key=lambda name: name.surname)
by_email = sorted(names_list, key=lambda name: name.email)


for name in names_list1:
    print(name)
    name.contact()
    print(name.label_lenght)

for name in names_list2:
    print(name)
    name.contact()
    print(name.label_lenght)