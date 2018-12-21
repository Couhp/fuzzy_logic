import xlrd
from os.path import join
import os

def read_impediment_lamp_rule():
    impediment_rule = []
    with xlrd.open_workbook(join(os.path.dirname(__file__),'rule_lamp.xlsx')) as book:
        sheet = book.sheet_by_index(0)

        lamp = [y for y in sheet.col_values(1)]
        distance = [z for z in sheet.col_values(2)]
        speed = [t for t in sheet.col_values(3)]
        for i in range(len(lamp)):
            impediment_rule.append((lamp[i].strip(), distance[i].strip(), speed[i].strip()))
    return impediment_rule

def read_impediment_stone_rule():
    impediment_rule = []
    with xlrd.open_workbook(join(os.path.dirname(__file__),'rule_stone.xlsx')) as book:
        sheet = book.sheet_by_index(0)

        distance = [y for y in sheet.col_values(1)]
        speed = [z for z in sheet.col_values(2)]

        for i in range(len(speed)):
            impediment_rule.append((distance[i].strip(), speed[i].strip()))
    return impediment_rule
