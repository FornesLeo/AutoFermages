# -*- coding: utf-8 -*-

import shutil
import os

def is_line_separator(string):
    for c in string:
        if c != ';':
            return 0
    return 1


def parse_data(path):
    file = open(path, "r")
    content = file.read()
    file.close()

    content = content.split('\n')
    data = []
    array = [['COMMUNE', 'SECTION', 'PLAN', 'SURFACE']]
    first = True
    temp = {}

    content = content[3:]


    for line in content:
        if len(line) == 0:
            continue
        if is_line_separator(line):
            first = True
            temp['CHAMPS'] = array
            data.append(temp)
            temp = {}
            array = [['COMMUNE', 'SECTION', 'PLAN', 'SURFACE']]
            continue
        if first:
            line = line.split(';')
            temp['NOM'] = line[0]
            temp['ADDRESS'] = line[1]
            temp['CODEP'] = line[2]
            first = False
        else:
            array.append(line.split(';'))

    temp['CHAMPS'] = array
    data.append(temp)
    return data


def get_personnal_last_year(path, name, year):
    file = open(path, "r")
    content = file.read()
    file.close()
    content = content.split('\n')
    column = 0
    line = content[0].split(';')
    for word in line:
        if year in word:
            break
        column += 1
    for line in content:
        if name in line:
            line = line.split(';')
            return line[column]
    return 0


def modify_last_year(path, data, year, pourcent):
    file = open(path, "r")
    content = file.read()
    file.close()
    if not os.path.isdir(year + '/config'):
        os.mkdir(year + '/config')
    shutil.copyfile(path, (year + '/' + path))
    content = content.split('\n')
    column_last_year = 0
    column_last_last_year = 0
    first_line = content[0].split(';')
    for word in first_line:
        if str(int(year) - 1) in word:
            break
        column_last_year += 1
    for word in first_line:
        if str(int(year) - 2) in word:
            break
        column_last_last_year += 1
    new_content = [['NOM', year + ' ' + pourcent + '%', first_line[column_last_year],
                    first_line[column_last_last_year], 'Surface ha']]
    for line in content:
        find = False
        for people in data:
            if people['NOM'] in line:
                total = 0
                for ha in people['CHAMPS']:
                    if 'SURFACE' in ha[3]:
                        continue
                    total += float(ha[3].replace(',', '.'))
                line = line.split(';')
                new_content.append([people['NOM'], people['new'], line[column_last_year], line[column_last_last_year],
                                    f"{total:.2f}"])
                find = True
                break
        if not find:
            if len(line) > 0 and line != content[0]:
                line = line.split(';')
                new_content.append([line[0], '', line[column_last_year], line[column_last_last_year],
                                    line[4]])
    #for people in data:
     #   find = False
      #  for line in content:
       #     if people['NOM'] in line:
        #        total = 0
         #       for ha in people['CHAMPS']:
          #          if 'SURFACE' in ha[3]:
           #             continue
           #         total += float(ha[3].replace(',', '.'))
           #     line = line.split(';')
           #     new_content.append([people['NOM'], people['new'], line[column_last_year], line[column_last_last_year],
            #                        f"{total:.2f}"])
             #   find = True
              #  break
        #if not find:
         #   new_content.append

    file = open(path, "w")
    for line in new_content:
        file.write(line[0] + ';' + line[1] + ';' + line[2] + ';' + line[3] + ';' + line[4] + '\n')
    file.close()
    return new_content
