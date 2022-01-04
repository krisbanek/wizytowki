import sys

from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, email, phone):
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
       self.phone = phone
      
    def __str__(self):
       return f"{self.first_name} {self.last_name} {self.email} {self.phone}"

    def contact(self):
       return print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")
    
    @property      #zamiana metody w argument
    def label_lenght(self):
       return (len(self.first_name) + len(self.last_name) + 1)

class BusinessContact(BaseContact):
    def __init__(self, company, position, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.company_phone = company_phone
  
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.company} {self.position} {self.company_phone}"
    
    def contact(self):
       return print(f"Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.last_name}")

    @property      #zamiana metody w argument
    def label_lenght(self):
       return (len(self.first_name) + len(self.last_name) + 1)
        
         
banekm1 = BaseContact(first_name="Magda", last_name="Banek", email="magda.banek@house.pl", phone="654247985")
banekk1 = BaseContact(first_name="Krzysztof", last_name="Banek", email="krzysztof.banek@house.pl", phone="654985122")
krakowskij1 = BaseContact(first_name="Jerzy", last_name="Krakowski", email="jerzy.krakowski@carpatia.pl", phone="699555444")
dobrowolskie1 = BaseContact(first_name="Edward", last_name="Dobrowolski", email="edward.dobrowolski@kielbasy.pl", phone="611582741")
dudekm1 = BaseContact(first_name="Maciej", last_name="Dudek", email="maciej.dudek@moonshine.pl", phone="678123456")

banekm2 = BusinessContact(first_name="Magda", last_name="Banek", company="House", position="CEO", email="magda.banek@house.pl", phone="654247985", company_phone="17111444555")
banekk2 = BusinessContact(first_name="Krzysztof", last_name="Banek", company="House-Expeditions", position="KOW", email="krzysztof.banek@house.pl", phone="654985122", company_phone="17222333444")
krakowskij2 = BusinessContact(first_name="Jerzy", last_name="Krakowski", company="Carpatia", position="President", email="jerzy.krakowski@carpatia.pl", phone="699555444", company_phone="17444333222")
dobrowolskie2 = BusinessContact(first_name="Edward", last_name="Dobrowolski", company="Kielbasy", position="Tester", email="edward.dobrowolski@kielbasy.pl", phone="611582741", company_phone="17321654987")
dudekm2 = BusinessContact(first_name="Maciej", last_name="Dudek", company="Moonshine", position="Project_Manager", email="maciej.dudek@moonshine.pl", phone="678123456", company_phone="17235417896")

names_list1 = [banekm1, banekk1, krakowskij1, dobrowolskie1, dudekm1]
names_list2 = [banekm2, banekk2, krakowskij2, dobrowolskie2, dudekm2]


def create_contacts(a,n):
    if a == 1:
        for _ in range(n):
            contacts = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), phone=fake.phone_number())
            print(contacts)
    elif a == 2:
        for _ in range(n):
            contacts = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.email(), phone=fake.phone_number(), company_phone=fake.phone_number())
            print(contacts)
    else:
        print("Wybierz prawidłowy rodzaj wizytówki = 1 dla BaseContact, 2 dla BusinessContact")

if __name__ == "__main__":
    a = int(input("Podaj proszę rodzaj wizytówki = 1 dla BaseContact, 2 dla BusinessContact: "))
    n = int(input("Podaj proszę liczbę wizytówek: "))
    create_contacts(a,n)
    


#for name in names_list1:
#    print(name)
#    name.contact()
#    print(name.label_lenght)

#for name in names_list2:
#    print(name)
#    name.contact()
#    print(name.label_lenght)