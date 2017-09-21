class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Mest:
    def __init__(self, eits=[], fellows=[]):
        self.eits = eits
        self.fellows = fellows

    def add_eit(self, eit_details):
        self.eits.append(eit_details)

    def add_fellow(self, fellow_details):
        self.fellows.append(fellow_details)

    def recite_facts(self, find_name):
        for eit_details in self.eits:
            if eit_details.eit_name == find_name:
                return eit_details.eit_fun_facts

    def feed_fellow(self, fellow_name):
        for fellow_details in self.fellows:
            if fellow_details.name == fellow_name:
                fellow_details.fellow_happiness += 2
                return str(fellow_details.fellow_happiness)

    def teach(self, fellow_name):
        for fellow_details in self.fellows:
            if fellow_details.name == fellow_name:
                fellow_details.fellow_happiness -= 2
                return str(fellow_details.fellow_happiness)


class Eits(Person):
    def __init__(self, name, nationality, eit_fun_facts=''):
        super().__init__(name, nationality)
        self.eit_fun_facts = eit_fun_facts


class Fellows(Person):
    number_of_fellows = 0

    def __init__(self, name, nationality, fellow_happiness=5):
        super().__init__(name, nationality)
        self.fellow_happiness = int(fellow_happiness)
        Fellows.number_of_fellows += 1


mest = Mest()


def check_nationality(county):
    if county in ('kenya', 'nigeria', 'ghana', 'ivory coast', 'south africa'):
        return True
    else:
        print('*********Invalid country************')
        return False



def evaluate_choice():

    choice = input('Choose option: \n 1 to add EIT \n 2 '
                   'to add Fellow \n 3 to recite fun fact \n '
                   '4 to make a fellow to teach \n '
                   '5 feed a fellow: ')
    if choice == '1':
        name = input('Enter name: ')
        nationality = input('Enter nationality: ')
        fun_facts = input('Enter fun fact: ')

        if check_nationality(nationality) is True:
            mest.add_eit(Eits(name, nationality, fun_facts))
            print('*********EIT Added*************')
        print()

    elif choice == '2':

        if Fellows.number_of_fellows < 4:
            name = input('Enter name: ')
            nationality = input('Enter nationality: ')
            happiness = input('Enter happiness value: ')
            mest.add_fellow(Fellows(name, nationality, happiness))
            print('*********Fellow added**********')
        else:
            print('*************Fellow quota exeeded*******')

        print()
    elif choice == '3':
        name = input('Enter name: ')
        fact = mest.recite_facts(name)
        print('********'+fact+'*************')
        print()
    elif choice == '4':
        name = input('Enter name: ')
        happiness = mest.teach(name)
        print('********' + happiness + '*************')
        print()
    elif choice == '5':
        name = input('Enter name: ')
        happiness = mest.feed_fellow(name)
        print('********' + happiness + '*************')
        print()
    elif choice == '6':
        exit()

    while choice != '6':
        evaluate_choice()


evaluate_choice()
