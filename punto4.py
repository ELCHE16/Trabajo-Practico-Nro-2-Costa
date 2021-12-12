# Determinar todos los pedidos que se pudieron completar priorizando la
# fecha (los más antiguos primero). Mostar el listado y cuántos fueron. 
# Determinar cuáles fueron los pedidos que fueron a la ciudad de Rosario y
# valorizarlos

#Listo todos los pedidos completos desde el mas antiguo al mas reciente (indico cant de pedidos completos).

import csv

def listar_pedidos_rosario(pedidos_rosario : dict) -> None:
    if(len(pedidos_rosario) > 0):
        print("|||PEDIDOS EN ROSARIO|||")
        print(f"Pedidos en Rosario: {len(pedidos_rosario)}")
        for numero, pedidos in pedidos_rosario.items():
            print(f"Numero pedido: {numero}, Fecha: {pedidos[0]}, Cliente: {pedidos[1]}, Ciudad: {pedidos[2]}, Provincia: {pedidos[3]}")
            print("     Artículos: ")
            for articulo in pedidos[4]:
                print(f"        Numero artículo: {articulo[0]}, Color: {articulo[1]}, Cantidad: {articulo[2]}, Descuento: {articulo[3]}")
    else:
        print("No hay pedidos que se encuentren en Rosario")

def pedidos_en_rosario(pedidos_procesados : dict, pedidos_rosario : dict) -> dict:
    ciudad : str = ""
    valor_total : int = 0
    for numero, pedidos in pedidos_procesados.items():
        ciudad = pedidos[3]
        if(ciudad.lower() == "rosario"):
            pedidos_rosario[numero] = pedidos
    
    for numero, pedidos in pedidos_rosario.items():
        for articulo in pedidos[4]:
            if(articulo[0] == "1334"):
                valor_total += (int(articulo[2]) * 15)
            elif(articulo[0] == "568"):
                valor_total += (int(articulo[2]) * 8)
    
        pedidos_rosario[numero].append(valor_total)

    return pedidos_rosario

def listar_pedidos_completos(pedidos_terminados : dict) -> None:
    print("|||PEDIDOS COMPLETADOS|||")
    print(f"Pedidos completados: {len(pedidos_terminados)}")
    for numero, pedidos in pedidos_terminados.items():
        print(f"Numero pedido: {numero}, Fecha: {pedidos[0]}/{pedidos[1]}/{pedidos[2]}, Cliente: {pedidos[3]}, Ciudad: {pedidos[4]}, Provincia: {pedidos[5]}")
        print("     Artículos: ")
        for articulo in pedidos[6]:
            print(f"        Numero artículo: {articulo[0]}, Color: {articulo[1]}, Cantidad: {articulo[2]}, Descuento: {articulo[3]}")

#Ordeno los pedidos primero por dia despues por mes y por ultimo por fecha.
def ordenar_pedidos_fecha(pedidos_separados_fecha : dict) -> dict:
    pedidos_terminados_ordenado_dia : list = []
    pedidos_terminados_ordenado_dia = sorted(pedidos_separados_fecha.items(), key = lambda x: x[1][0], reverse = False)
    dict_ordenado_dia : dict = {}
    for pedido in pedidos_terminados_ordenado_dia:
        dict_ordenado_dia[pedido[0]] = pedido[1]

    pedidos_terminados_ordenado_mes : list = []
    pedidos_terminados_ordenado_mes = sorted(dict_ordenado_dia.items(), key = lambda x: x[1][1], reverse = False)
    dict_ordenado_mes : dict = {}
    for pedido in pedidos_terminados_ordenado_mes:
        dict_ordenado_mes[pedido[0]] = pedido[1]

    pedidos_terminados_ordenado_final : list = []
    pedidos_terminados_ordenado_final = sorted(dict_ordenado_mes.items(), key = lambda x: x[1][2], reverse = False)
    dict_ordenado_final : dict = {}
    for pedido in pedidos_terminados_ordenado_final:
        dict_ordenado_final[pedido[0]] = pedido[1]

    return dict_ordenado_final

#crea un dict que separa las fechas "12/10/2001" --- "12","10","2001"
def separar_fechas(pedidos_terminados : dict, pedidos_fechas_separada : dict) -> dict:
    dia : int = 0
    mes : int = 0
    anio : int = 0
    for numero, pedido in pedidos_terminados.items():
        fecha_seperada = pedidos_terminados[numero][0].split("/")
        dia = fecha_seperada[0]
        mes = fecha_seperada[1]
        anio = fecha_seperada[2]
        pedidos_fechas_separada[numero] = [dia, mes, anio, pedido[1], pedido[2], pedido[3], pedido[4]]

    return pedidos_fechas_separada

#leo el csv y comparo con la lista de ids de pedidos completados que obtengo de la funcion hacer_camiones()
def pasar_listaCsv_dict(pedidos_procesados : dict, pedidos_que_salen : list, lista_csv : list) -> dict:
    for objeto in lista_csv:
        if((objeto[0] not in pedidos_procesados.keys()) and (objeto[0] in pedidos_que_salen)):
            pedidos_procesados[objeto[0]] = [objeto[1], objeto[2], objeto[3], objeto[4], [[objeto[5],objeto[6],objeto[7],objeto[8]]]]
        elif((objeto[0] in pedidos_procesados.keys()) and (objeto[0] in pedidos_que_salen)):
            pedidos_procesados[objeto[0]][4].append([objeto[5],objeto[6],objeto[7],objeto[8]])

    return pedidos_procesados

def main() -> None:
    pedidos_fechas_separada : dict = {}
    pedidos_terminados_dict : dict = {}
    pedidos_procesados : dict = {}
    pedidos_rosario : dict = {}
    lista_csv : list = [['1', '01/11/2021', 'Juan Alvarez', 'Villa MarÃ\xada', 'CÃ³rdoba', '1334', 'Azul', '36', '5'], ['1', '01/11/2021', 'Juan Alvarez', 'Villa MarÃ\xada', 'CÃ³rdoba', '568', 'Azul', '12', '5'], ['1', '01/11/2021', 'Juan Alvarez', 'Villa MarÃ\xada', 'CÃ³rdoba', '568', 'Negro', '6', '5'], ['1', '01/11/2021', 'Juan Alvarez', 'Villa MarÃ\xada', 'CÃ³rdoba', '1334', 'Amarilla', '12', '5'], ['2', '01/11/2021', 'Carlos Rodriguez', 'Parana', 'Santa Fe', '1334', 'Rojo', '5', '0'], ['2', '01/11/2021', 'Carlos Rodriguez', 'Parana', 'Santa Fe', '1334', 'Negro', '5', '0'], ['3', '02/11/2021', 'Juan Lopez', 'Santa Rosa', 'La Pampa', '1334', 'Amarillo', '12', '10'], ['3', '02/11/2021', 'Juan Lopez', 'Santa Rosa', 'La Pampa', '1334', 'Azul', '48', '10'], ['3', '02/11/2021', 'Juan Lopez', 'Santa Rosa', 'La Pampa', '1334', 'Rojo', '48', '10'], ['3', '02/11/2021', 'Juan Lopez', 'Santa Rosa', 'La Pampa', '1334', 'Negro', '12', '10'], ['3', '02/11/2021', 'Juan Lopez', 'Santa Rosa', 'La Pampa', '568', 'Azul', '48', '10'], ['3', '02/11/2021', 'Juan Lopez', 'Santa Rosa', 'La Pampa', '568', 'Negro', '48', '10'], ['4', '02/11/2021', 'Carlos Arana', 'Bariloche', 'Rio Negro', '1334', 'Rojo', '12', '0'], ['5', '02/11/2021', 'Mario Mangiafave', 'CABA', 'Buenos Aires', '1334', 'Rojo', '60', '15'], ['5', '02/11/2021', 'Mario Mangiafave', 'CABA', 'Buenos Aires', '1334', 'Amarillo', '30', '15'], ['5', '02/11/2021', 'Mario Mangiafave', 'CABA', 'Buenos Aires', '1334', 'Azul', '48', '15'], ['6', '02/11/2001', 'Mario Mangiafave', 'CABA', 'ROsarIo', '1334', 'Azul', 
'48', '15'], ['6', '02/11/2001', 'Mario Mangiafave', 'CABA', 'ROsarIo', '568', 'Azul', '20', '15'], ['6', '02/11/2001', 'Mario Mangiafave', 'CABA', 'ROsarIo', '1334', 'Azul', '29', '15']]
    #hacer_camiones(a) = lista_ids_pedidos
    lista_ids_pedidos : list = ['1', '2', '3', '4', '5', '6']
    pedidos_procesados = pasar_listaCsv_dict(pedidos_procesados, lista_ids_pedidos, lista_csv)
    pedidos_rosario = pedidos_en_rosario(pedidos_procesados, pedidos_rosario)
    pedidos_fechas_separada = separar_fechas(pedidos_procesados, pedidos_fechas_separada)
    pedidos_terminados_dict = ordenar_pedidos_fecha(pedidos_fechas_separada)
    listar_pedidos_completos(pedidos_terminados_dict)#PUNTO 4
    listar_pedidos_rosario(pedidos_rosario)#PUNTO 5

main()

#COMENTÉ hacer_camiones(a) para que no me explote el codigo, abajo esta un ejemplo de esta misma funcion (la lista que retorna esta misma) 
#lista_csv y lista_ids_pedidos son listas que uso de ejemplo para procesar pedidos. Estas son reemplazadas con las listas que obtienen de otras funciones lista_csv( parse_pedidos_csv() ) y lista_ids_pedidos( hacer_camiones() )
