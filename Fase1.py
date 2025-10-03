import math

# --- Base de Datos de Módulos (del archivo de inventario) ---
# Un diccionario que mapea el código del módulo a su nombre para una salida más clara.
MODULOS_INFO = {
    "001": "ARKHA_base_L1_V1",
    "002": "ARKHA_LabTri_L2_V1",
    "003": "ARKHA_Lab_L2_V1",
    "004": "ARKHA_PowerCore_L1_V1",
    "005": "ARKHA_RecreacionTri_L1_V1",
    "006": "ARKHA_Recreacion_L1_V1",
    "007": "ARKHA_HuertaTri_L1_V1",
    "008": "ARKHA_Huerta_L1_V1",
    "009": "ARKHA_Circulacion_L1_V1",
    "010": "ARKHA_AccessCore_L1_V1",
    "011": "ARKHA_TransCore_L2_V1",
    "012": "ARKHA_SanitaryBay_L2_V1",
    "013": "ARKHA_SanitaryBayTri_L2_V1",
    "014": "ARKHA_L2_ExerciseBay_V1",
    "015": "ARKHA_L2_ExerciseBayTri_V1",
    "016": "ARKHA_L2_SystemsBay_V1",
    "017": "ARKHA_L2_SystemsBayTri_V1",
    "018": "ARKHA_L2_StorageBay_V1",
    "019": "ARKHA_L2_StorageBayTri_V1",
    "020": "ARKHA_L3_GalleyComputerBay_V1",
    "021": "ARKHA_L3_GalleyComputerBayTri_V1",
    "022": "ARKHA_L3_MealPrepBay_V1",
    "023": "ARKHA_L3_MealPrepBayTri_V1",
    "024": "ARKHA_L3_MedBay_V1",
    "025": "ARKHA_L3_MedBayTri_V1",
    "026": "ARKHA_L2_SleepWardBay_V1",
    "027": "ARKHA_L2_SleepWardBayTri_V1",
}

# --- Algoritmo Principal ---
def calcular_modulos_arka(P, T):
    """
    Calcula la cantidad de cada tipo de módulo necesario para el Arka.

    Args:
        P (int): Número de pasajeros.
        T (int): Tiempo de la misión en días.

    Returns:
        dict: Un diccionario con el código del módulo como clave y la cantidad necesaria como valor.
    """
    # Inicializamos un diccionario para guardar el recuento de cada módulo.
    # Usamos f-string para formatear los números de 1 a 27 como '001', '002', etc.
    modulos_necesarios = {f"{i:03d}": 0 for i in range(1, 28)}

    # --- REGLAS DE CÁLCULO ---

    # 1. Módulo BASE (001)
    # Uno por cada "011": "ARKHA_TransCore_L2_V1" en lvl 2
    # -----------------------------------------------------------------   
    
    
    # 2. Módulos LABORATORY (002 (tri) y 003)
    # La lógica sigue la tabla de reglas para P y T.
    if 1 <= P <= 4:
        if T <= 500:
            modulos_necesarios["003"] += 1
        elif 500 < T < 1000:
            modulos_necesarios["002"] += 1
        else:  # T >= 1000
            modulos_necesarios["003"] += 2
    elif 5 <= P <= 8:
        if T <= 500:
            modulos_necesarios["003"] += 2
        elif 500 < T < 1000:
            modulos_necesarios["002"] += 2
        else:  # T >= 1000
            modulos_necesarios["003"] += 3
    elif 9 <= P <= 12:
        if T <= 500:
            modulos_necesarios["003"] += 3
        elif 500 < T < 1000:
            modulos_necesarios["002"] += 1
            modulos_necesarios["003"] += 2
        else:  # T >= 1000
            modulos_necesarios["003"] += 4
    elif 13 <= P <= 16:
        if T <= 500:
            modulos_necesarios["003"] += 4
        elif 500 < T < 1000:
            modulos_necesarios["002"] += 1
            modulos_necesarios["003"] += 3
        else:  # T >= 1000
            modulos_necesarios["002"] += 4


    # 3. Módulo POWERCORE (004)
    # Uno por cada "001": "ARKHA_base_L1_V1",
    # -----------------------------------------------------------------

    # 4. Módulos RECREATION (005 (tri) y 006)
    # La lógica sigue la tabla de reglas para P y T.
    if 1 <= P <= 4:
        if 180 < T <= 500:
            modulos_necesarios["006"] += 1
        elif T > 500:
            modulos_necesarios["005"] += 1

    elif 5 <= P <= 8:
        if T <= 180:
            modulos_necesarios["006"] += 1
        elif 180 < T <= 500:
            modulos_necesarios["005"] += 1
        elif T > 500:
            modulos_necesarios["005"] += 1
            modulos_necesarios["006"] += 1

    elif 9 <= P <= 12:
        if T <= 180:
            modulos_necesarios["005"] += 1
        elif 180 < T <= 500:
            modulos_necesarios["005"] += 1
            modulos_necesarios["006"] += 1
        elif T > 500:
            modulos_necesarios["005"] += 2

    # 5. Módulos HUERTA (007 (Tri) y 008)
    Gu = P * 4
    modulos_necesarios["007"] = math.floor(Gu / 16)
    if Gu % 16 > 10:
        modulos_necesarios["007"] += 1
    elif Gu % 16 != 0:
        modulos_necesarios["008"] = math.ceil(Gu % 16)


    # 6. Módulo CIRCULACION (009)
    # Como se indica en las reglas, la cantidad depende de la disposición final.
    # Este algoritmo no puede determinarlo; se necesitaría un algoritmo de layout.

    # 7. Módulo ACCESS (010)
    if T <= 600:
        modulos_necesarios["010"] = math.ceil(P / 6)
    else: 
        modulos_necesarios["010"] = math.ceil(P / 6) * 2
    
    # 8. Módulos TRANSCORE (011)
    # Uno por cada nivel > 1 and < n de cada base
    
    # 9. Módulos SANITARY (012 y 013(tri))
    if 1 <= P <= 2:
        if T < 500:
            modulos_necesarios["012"] += 1
        elif T >= 500:
            modulos_necesarios["013"] += 1      
    elif 3 <= P <= 5:
        if T <= 180:
            modulos_necesarios["012"] += 1
        elif T > 180:
            modulos_necesarios["013"] += 1
    elif P == 6:
        if T <= 60: 
            modulos_necesarios["012"] += 1
        elif 60 < T < 500:
            modulos_necesarios["013"] += 1
        elif T >= 500: 
            modulos_necesarios["012"] += 1
            modulos_necesarios["013"] += 1

    # 11. Módulos EXERCISE (014 y 015)
    if 1 <= P <= 4:
        if T < 500:
            modulos_necesarios["014"] += 1
        else: # T >= 500
            modulos_necesarios["015"] += 1
    elif 5 <= P <= 8:
        modulos_necesarios["015"] += 1
        if T >= 500: modulos_necesarios["014"] += 1
    elif 9 <= P <= 12:
        if T <= 30: modulos_necesarios["014"] += 2
        elif 30 < T < 500:
            modulos_necesarios["014"] += 1
            modulos_necesarios["015"] += 1
        else: # T >= 500
            modulos_necesarios["015"] += 2

    # 12. Módulos SYSTEM (016 y 017)
    if 1 <= P <= 4:
        if T <= 180:
            modulos_necesarios["016"] += 1
        elif 180 < T < 500:
            modulos_necesarios["017"] += 1
        elif T >= 500:
            modulos_necesarios["017"] += 1
            modulos_necesarios["016"] += 1 
    elif 5 <= P <= 6:
        if T <= 180:
            modulos_necesarios["016"] += 1
        elif 180 < T < 500:
            modulos_necesarios["016"] += 2
        elif 500 <= T < 600:
            modulos_necesarios["016"] += 1
            modulos_necesarios["017"] += 1
        elif T >= 600:
            modulos_necesarios["016"] += 1
            modulos_necesarios["017"] += 1
    elif 7 <= P <= 8:
        if T <= 180:
            modulos_necesarios["017"] += 1
        elif 180 < T < 500:
            modulos_necesarios["016"] += 2
        elif T >= 500:
            modulos_necesarios["016"] += 1
            modulos_necesarios["017"] += 1
    elif 9 <= P <= 10:
        if T <= 180:
            modulos_necesarios["016"] += 1
            modulos_necesarios["017"] += 1
        elif 180 < T < 500:
            modulos_necesarios["016"] += 3
        elif T >= 500:
            modulos_necesarios["016"] += 2
            modulos_necesarios["017"] += 1
    elif 11 <= P <= 12:
        if T <= 180:
            modulos_necesarios["017"] += 2
        elif 180 < T < 500:
            modulos_necesarios["016"] += 3
        elif T >= 500:
            modulos_necesarios["016"] += 2
            modulos_necesarios["017"] += 1

    # 11. Módulos STORAGE (018 y 019)
    # Basado en el producto de P * T
    pt_product = P * T

    


    # 12. Módulos COMPUTER (020 y 021) - REGLAS ACTUALIZADAS
    if 1 <= P <= 8:
        if T <= 180:
            modulos_necesarios["020"] += 1
        else:
            modulos_necesarios["021"] += 1
    elif 9 <= P <= 12:
         modulos_necesarios["021"] += 1 # No depende de T
    elif 13 <= P <= 16:
        if T <= 180:
            modulos_necesarios["020"] += 2
        else:
            modulos_necesarios["021"] += 2

    # 13. Módulos MEALPREP (022 y 023)
    if 1 <= P <= 4:
        if T <= 180:
            modulos_necesarios["022"] += 1
        else:
            modulos_necesarios["023"] += 1
    elif 5 <= P <= 6:
        if T <= 60:
            modulos_necesarios["022"] += 1
        else:
            modulos_necesarios["023"] += 1
    elif 7 <= P <= 10:
        if T < 500: modulos_necesarios["023"] += 1
        else: modulos_necesarios["022"] += 2
    elif P > 10: # P >= 11
        if T < 500:
            modulos_necesarios["022"] += 2
        else:
            modulos_necesarios["023"] += 2

    # 14. Módulos MEDICAL (024 y 025)
    if 1 <= P <= 4:
        if T <= 180:
            modulos_necesarios["024"] += 1
        else:
            modulos_necesarios["025"] += 1
    elif 5 <= P <= 6:
        if T <= 60:
            modulos_necesarios["024"] += 1
        elif 60 < T < 500:
            modulos_necesarios["025"] += 1
        else: # T >= 500
            modulos_necesarios["024"] += 2
    elif 7 <= P <= 8:
        if T <= 180: 
            modulos_necesarios["025"] += 1
        elif 180 < T < 500:
            modulos_necesarios["025"] += 2
        else: # T >= 500
            modulos_necesarios["024"] += 1
            modulos_necesarios["025"] += 1
    elif 9 <= P <= 12: 
        if T <= 180:
            modulos_necesarios["025"] += 2
        else: # T > 180
            modulos_necesarios["024"] += 2
            
    # 15. Módulos SLEEP (026 y 027)
    if 1 <= P <= 2:
        modulos_necesarios["026"] += 1
    elif 3 <= P <= 4:
        modulos_necesarios["027"] += 1

    return modulos_necesarios

# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # --- PARÁMETROS DE ENTRADA DE LA MISIÓN ---
    numero_de_pasajeros = 14
    tiempo_en_dias = 200
    # -------------------------------------------

    print(f"Calculando módulos para una misión con {numero_de_pasajeros} pasajeros y {tiempo_en_dias} días de duración...\n")

    # Ejecutar el algoritmo
    resultado = calcular_modulos_arka(numero_de_pasajeros, tiempo_en_dias)

    # Imprimir los resultados de forma clara
    print("--- INVENTARIO DE MÓDULOS NECESARIOS PARA EL ARKA ---")
    for codigo, cantidad in resultado.items():
        if cantidad > 0:
            nombre_modulo = MODULOS_INFO.get(codigo, "Desconocido")
            print(f"- Módulo {codigo} ({nombre_modulo}): {cantidad} unidad(es)")
    print("-----------------------------------------------------")