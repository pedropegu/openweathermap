import requests
import json
import os
import sys

#MAIN

def dates_to_file(ciudades,weather_date):
    dicc = {}
    api_key = os.getenv("API_KEY_WEATHER")
    for lugar in ciudades:
        ciudad = lugar[:-1]

        parametros = {"q":ciudad,"mode":"json","units":"metric","APPID":api_key}
        get = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parametros)


        if get.status_code==200:
            datos = get.json()
            dicc[ciudad] = "{} °C".format(datos["main"]["temp"]) 
            weather_date.write(json.dumps(datos, sort_keys=True, indent=4))
        else:
            dicc[ciudad] = "No hemos encontrado ese lugar."
    return dicc


#Apartado de apertura de ficheros
weather_date=open(sys.argv[2], 'w')
ciudades=open(sys.argv[1],'r')




#Ejecución & cerrar ficheros
print(dates_to_file(ciudades,weather_date))
weather_date.close()
ciudades.close()


