import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A5')
        pdf.add_page()

        # Add icon
        pdf.image(name='files/house.png', w=50, h=50)

        # Insert title
        pdf.set_font(family='Times', size=30, style='B')
        pdf.cell(w=0, h=40, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=150, h=40, txt='Period:', border=1, align='C')
        pdf.cell(w=0, h=40, txt=bill.period, border=1, align='C', ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=10, style='' )
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=1, align='C')
        pdf.cell(w=0, h=40, txt=flatmate1_pay, border=1, align='C', ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=150, h=40, txt=flatmate2.name, border=1, align='C')
        pdf.cell(w=0, h=40, txt=flatmate2_pay, border=1, align='C', ln=1)

        os.chdir('files')

        pdf.output(self.filename)
        webbrowser.open(self.filename)