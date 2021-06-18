from Libraries import persistencia as sd
import json

data = {
    "carros":[
        {
            "marca": "Renault",
            "modelo": 2010
        },
        {
            "marca": "Mazda",
            "modelo": 2011
        }
    ]    
}
print("prueba")
# Buffer de escritura de datos
with open("midatalst.json","w") as write_file: 
    json.dump(data, write_file,indent=4)      