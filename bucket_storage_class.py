import boto3
import datetime
import gc
import os
import sys
import csv
import time
from botocore.exceptions import ClientError

nome_bucket = '#'
s3 = boto3.resource('s3');


def obter_arquivo_bucket(identificador):
    return s3.Object(nome_bucket, identificador)

def comparar_lista_db_bucket(documento):
    try:
        s3_object = obter_arquivo_bucket(documento)
        if(s3_object.content_length == 0):
            return "CORRUPTED"
        else:
            return  s3_object.storage_class
            
        del s3_object
    except ClientError as e: 
        result.append("{}, NOT_FOUND".format(id_doc))
        print("\n")
        print(e.response['Error'])

    return result

arquivo = open("info_cnpj_#######.txt", "w")

with open("documentos_cnpj_#########.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        storage = comparar_lista_db_bucket(row['identificador_documento'])
        arquivo.write("{0} - {1}".format(row['identificador_documento'], storage) + "\n")
        print("{0}: {1} - {2}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), row['identificador_documento'], storage) + "\n")
