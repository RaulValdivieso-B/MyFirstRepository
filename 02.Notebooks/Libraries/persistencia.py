import json

def crearInfo(fileName,info):
    with open("data/"+fileName,"w") as write_file:
        json.dump(info, write_file, indent = 4)
        
def leerArchivo(fileName):
    with open("data/"+fileName,"r") as read_file:
        dataf = json.load(read_file)
    return dataf

def addInfo(new_data, filename='data.json'):
    with open("data/"+filename,'r+') as file:
        file_data = json.load(file)
        file_data["carros"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)