from flat import Bill, Flatmate
from report import PdfReport

amount = float(input('Please enter the bill amount: '))
period = input('What is the bill period?: E.g. December 2022: ')
name1 = input('What is your name? ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house during the bill period? '))
name2 = input('What is your neighbor\' name? ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house during the bill period? '))

bill = Bill(amount, period)
person1 = Flatmate(name1, days_in_house1)
person2 = Flatmate(name2, days_in_house2)

print(f'{name1} pays: ', person1.pays(bill, person2))
print(f'{name2} pays: ', person2.pays(bill, person1))

pdf_report = PdfReport(filename=f'{bill.period}.pdf')
pdf_report.generate(person1, person2, bill)
