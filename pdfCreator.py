# -*- coding: utf-8 -*-

from fpdf import FPDF
from datetime import date
from num2words import num2words


class Pdf:
    def __init__(self, name):
        self.name = name
        self.pdf = FPDF(format='A4')
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=14)
        self.pdf.set_margins(20, 20, 20)
        self.pdf.set_xy(20, 20)

    def add_exp_info(self, text):
        self.pdf.set_xy(20, 20)
        self.pdf.multi_cell(0, 5, txt=text, align="L")

    def set_date(self):
        self.pdf.set_xy(20, 20)
        today = date.today().strftime("%d/%m/%Y")
        self.pdf.cell(170, 0, txt="LE " + today, align="R")

    def add_rcv_info(self, name, addr, codep):
        self.pdf.set_xy(110, 40)
        self.pdf.cell(50, 5, txt=name, ln=1, align="L")
        self.pdf.set_xy(110, 45)
        self.pdf.multi_cell(0, 5, txt=addr, align="L")
        self.pdf.set_xy(110, 50)
        self.pdf.multi_cell(0, 5, txt=codep, align="L")


    def add_main_text(self, indice, pourcentage):
        year = date.today().strftime("%Y")
        last_year = str(int(year) - 1)
        self.pdf.set_xy(20, 60)
        self.pdf.cell(50, 5, txt="Règlement du fermage " + year, ln=1, align="L")
        self.pdf.set_xy(20, 70)
        self.pdf.multi_cell(0, 5, txt="        Veuillez trouver ci-joint le chèque correspondant au règlement" +
                                 " du fermage de l\'année " + year + " dont l\'indice nationnal a la valeur de " + indice
                                 + (", soit une augmentation de " if float(pourcentage.replace(',', '.')) > 0 else
                                 ", soit une diminution de ") + pourcentage + "% par rapport à " + last_year + ".",
                                 align="L")

    def add_table(self, array):
        self.pdf.ln(10)
        col_width = self.pdf.w / 5
        row_height = self.pdf.font_size
        self.pdf.set_right_margin(20)
        for row in array:
            for item in row:
                self.pdf.cell(col_width, row_height * 2, txt=item, border=1)
            self.pdf.ln(row_height * 2)

    def create(self):
        self.pdf.output(self.name + '.pdf')

    def add_fermage(self, old_total, total, pourcentage):
        year = date.today().strftime("%Y")
        last_year = str(int(year) - 1)
        self.pdf.ln(10)
        self.pdf.cell(100, 5, txt="Fermages " + last_year + ": " + old_total, align="R", ln=1)
        self.pdf.cell(100, 5, txt=("+ " if float(pourcentage.replace(',', '.')) > 0 else " ") + pourcentage + "%", align="R", ln=1)
        self.pdf.cell(100, 5, txt="Fermages " + year + ": " + total, align="R", ln=1)

    def add_footer_text(self):
        self.pdf.ln(10)
        self.pdf.multi_cell(0, 5, txt="Pour rappel, en cas de dégrèvement de taxes foncières suite aux calamités"
            " agricoles, le montant revient au bailleur et doit lui être restitué.\n\n        Nous vous remercions de"
            " votre confiance et vous souhaitons d'agréables fêtes de fin d'année.\n\nCordialement,", align="L")
        self.pdf.ln(10)
        self.pdf.cell(170, 0, txt="Fornes Christophe", align="R")

    def fiche_resume(self, array):
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_margins(10, 10, 10)
        self.pdf.set_xy(10, 10)
        col_width = self.pdf.w / 5.5
        row_height = self.pdf.font_size
        self.pdf.set_right_margin(10)
        for row in array:
            temp_y = 0
            for item in row:
                x = self.pdf.get_x()
                y = self.pdf.get_y()
                self.pdf.multi_cell(col_width, row_height * 2 + temp_y, txt=item, border=1)
                if (y + row_height * 2 + temp_y) < self.pdf.get_y():
                    temp_y += self.pdf.get_y() - (y + row_height * 2)
                self.pdf.set_xy(x + col_width, y)
            self.pdf.ln(row_height * 2 + temp_y)
            if self.pdf.get_y() > 270:
                self.pdf.add_page()
    
    def create_cheque(self, data, path):
        self.pdf.set_font("Arial", size=10)
        self.pdf.set_margins(10, 10, 10)
        self.pdf.set_xy(55, 33)

        somme = data['new'].split('.')
        euro = num2words(somme[0], lang='fr')
        cent = num2words(somme[1], lang='fr')
        self.pdf.multi_cell(100, 4, txt=(euro + ' euros ' + cent + ' centimes'))
        self.pdf.set_xy(35, 43)
        self.pdf.cell(100, 5, txt=data['NOM'], align="L")
        self.pdf.set_xy(150, 43)
        self.pdf.cell(40, 5, txt=data['new'], align="R")
        self.pdf.set_xy(150, 53)
        self.pdf.cell(40, 5, txt='Minversheim', align="R")
        today = date.today().strftime("%d/%m/%Y")
        self.pdf.set_xy(150, 58)
        self.pdf.cell(40, 5, txt=today, align="R")
