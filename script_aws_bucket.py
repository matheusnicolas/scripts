import pymysql.cursors
import os.path
from os import listdir
import os
import csv

connection = pymysql.connect(host = "***", user = "***", password = "***", db = "***", charset = "utf8")

diretorio = "C:/Users/..."
diretorio2 = "C:/Users/..."

lista_arquivos = listdir(diretorio)
for arquivo in lista_arquivos:
    input_arc = open(diretorio + arquivo, 'r')
    output_arc = open(diretorio2 + arquivo, 'w')

    for line in input_arc.readlines():
        for caracteres in line:
            if(caracteres == " "):
                caracteres.replace(" ", "")

            elif(caracteres == ";"):
                caracteres.split(";")
                
        if not line.strip(): continue
        if(line.strip() == "***"): continue
        if(line.strip() == "***"): continue
        
        output_arc.write(line)

local = ""
cursor = connection.cursor()           

lista_csv_to_bd = listdir(diretorio2)
for arquivo in lista_csv_to_bd:
    if(arquivo != "***" or arquivo != "***"):
        #local = diretorio2 + arquivo
        input_file = csv.DictReader(open(arquivo, encoding='utf-8'), delimiter=',')
        for row in input_file:
            print(row)
            query = "INSERT INTO `***` (***, ***, ***) VALUES (%s, %s, %s)" 
            identificador = (row['***'], row['***'], row['***'])
            print(identificador)
            cursor.execute(query, identificador)
            connection.commit()
        
input_arc.close()
output_arc.close()
print("Dados inseridos com sucesso!")
