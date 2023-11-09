# -*- coding: utf-8 -*-

from pdfCreator import Pdf
from parse import parse_data, get_personnal_last_year, modify_last_year
from datetime import date
from tkinter import *
from App import App
import os

path_data = 'config/data.csv'

path_last = 'config/last_year.csv'


def input():
    root = Tk()
    myapp = App(root)
    myapp.mainloop()
    return {'pourcent': myapp.get_pourcent().replace(',', '.'), 'indice': myapp.get_indice().replace(',', '.')}


def calcul(name, last_year, pourcent):
    last = get_personnal_last_year(path_last, name, last_year)
    new = float(last) * float(pourcent) / 100 + float(last)
    return {'last': str(last), 'new': f"{new:.2f}"}


def create_document(element, path, entry):
    result = calcul(element['NOM'], str(int(year) - 1), entry['pourcent'])
    page = Pdf(path + '/' + element['NOM'])
    page.set_date()
    page.add_exp_info('EARL DU BOUTON D\'OR\n1 RUE D\'ALTECKENDORF\n67270 MINVERSHEIM\nTél: 06,05,11,08,72\nTél: 06,'
                      '85,28,06,29')
    page.add_rcv_info(element['NOM'], element['ADDRESS'], element['CODEP'])
    page.add_main_text(entry['indice'], entry['pourcent'])
    page.add_table(element['CHAMPS'])
    page.add_fermage(result['last'], result['new'], entry['pourcent'])
    page.add_footer_text()
    page.create()
    return result


def create_cheque(element, path):
    page = Pdf(path + '/' + element['NOM'])
    page.create_cheque(element, path)
    page.create()


def create_resume(path, new_data):
    page = Pdf(path + '/' + 'fiche_resume')
    page.fiche_resume(new_data)
    page.create()


if __name__ == '__main__':
    data = parse_data(path_data)
    year = date.today().strftime("%Y")
    if not os.path.isdir(year):
        os.mkdir(year)
    if not os.path.isdir(year + '/lettres'):
        os.mkdir(year + '/lettres')
    if not os.path.isdir(year + '/cheques'):
        os.mkdir(year + '/cheques')
    entry = input()
    new_data = []
    for elem in data:
        if 'NOM' not in elem:
            continue
        result = create_document(elem, year + '/lettres', entry)
        elem['new'] = result['new']
        create_cheque(elem, year + '/cheques')
        new_data.append(elem)
    new_data = modify_last_year(path_last, new_data, year, entry['pourcent'])
    create_resume(year, new_data)
