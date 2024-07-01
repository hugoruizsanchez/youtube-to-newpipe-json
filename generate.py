# El cometido del programa será importar un fichero de texto plano (copia y pega del feed de suscripciones de youtube),
# con algunos canales comenzados en "@". Debemos recopilar el nombre de esos canales junto a sus correspondientes
# direcciones, y exportarlas en un fichero JSON con el formato newpipe

# Dependencias

import json; 

# Importar archivo

f = open ('subscriptions.txt', 'r');

subscriptions_content = f.readlines();

# Formato de exportación
# Siendo que cada canal debe responder al formato: {service_id:"", url:"", name:""}
export = {
    "app_version":"0.19.8", 
    "app_version_int":953,
    "subscriptions":[]
}

# Palabras clave para hacer el scrapping

keywords=["© 2024 Google LLC YouTube, a Google company", "Suscrito"];

# Función que se encarga de encontrar keybords en un string

def has_keyword (block, keywords):
    for word in keywords:
        if word in block:
            return True; 
    return False;

# Scrapping al fichero e introducción de la información en channels. 

buffer = 0;

for block in subscriptions_content: 
    if block != "\n":
        if buffer == 2:
            index_channel = {"service_id":0};
            index_channel["name"] = (block.replace("\n", ""));
            buffer = buffer-1;
        elif buffer == 1:
            if "@" in block:
                index_channel["url"] = ("https://youtube.com/"+block.split("•")[0]); 
                export["subscriptions"].append(index_channel);     
            buffer = buffer-1;

        if has_keyword (block, keywords):
            buffer = 2;  

# Conversión del archivo a JSON y exportación. 

print (export);

with open ("result.json", "w") as outfile: 
    json.dump (export, outfile);


