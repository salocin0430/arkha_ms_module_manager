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
def calcular_modulos_arka(P, T, TipoC):
    """
    Calcula la cantidad de cada tipo de módulo necesario para el Arka.

    Args:
        P (int): Número de pasajeros.
        T (int): Tiempo de la misión en días.
        TipoC (bool): Indica si se está realizando una misión de tipo Científico.

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
    if TipoC:
        Bloques_L = P // 16
        Resto_L = P % 16
        if T <= 500:
            modulos_necesarios["003"] += 4 * Bloques_L
        elif 500 < T < 1000:
            modulos_necesarios["002"] += 1 * Bloques_L
            modulos_necesarios["003"] += 3 * Bloques_L
        else:  # T >= 1000
            modulos_necesarios["002"] += 4 * Bloques_L       
        
        if 1 <= Resto_L <= 4:
            if T <= 500:
                modulos_necesarios["003"] += 1
            elif 500 < T < 1000:
                modulos_necesarios["002"] += 1
            else:  # T >= 1000
                modulos_necesarios["003"] += 2
        elif 5 <= Resto_L <= 8:
            if T <= 500:
                modulos_necesarios["003"] += 2
            elif 500 < T < 1000:
                modulos_necesarios["002"] += 2
            else:  # T >= 1000
                modulos_necesarios["003"] += 3
        elif 9 <= Resto_L <= 12:
            if T <= 500:
                modulos_necesarios["003"] += 3
            elif 500 < T < 1000:
                modulos_necesarios["002"] += 1
                modulos_necesarios["003"] += 2
            else:  # T >= 1000
                modulos_necesarios["003"] += 4
        elif 13 <= Resto_L <= 16:
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
    Bloques_R = P // 12
    Resto_R = P % 12

    if T <= 180:
        modulos_necesarios["006"] += 1 * Bloques_R
    elif 180 < T <= 500:
        modulos_necesarios["005"] += 1 * Bloques_R
        modulos_necesarios["006"] += 1 * Bloques_R
    else:
        modulos_necesarios["005"] += 2 * Bloques_R

    if 1 <= Resto_R <= 4:
        if 180 < T <= 500:
            modulos_necesarios["006"] += 1
        elif T > 500:
            modulos_necesarios["005"] += 1
    elif 5 <= Resto_R <= 8:
        if T <= 180:
            modulos_necesarios["006"] += 1
        elif 180 < T <= 500:
            modulos_necesarios["005"] += 1
        else:
            modulos_necesarios["005"] += 1
            modulos_necesarios["006"] += 1
    elif 9 <= Resto_R <= 12:
        if T <= 180:
            modulos_necesarios["005"] += 1
        elif 180 < T <= 500:
            modulos_necesarios["005"] += 1
            modulos_necesarios["006"] += 1
        else:
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
    
    Bloques_S = P // 6
    Resto_S = P % 6
    
    if T < 500:
        modulos_necesarios["012"] += 1 * Bloques_S
    else:
        modulos_necesarios["013"] += 1 * Bloques_S

    if 1 <= Resto_S <= 2:
        if T < 500: modulos_necesarios["012"] += 1
        else: modulos_necesarios["013"] += 1
    elif 3 <= Resto_S <= 5:
        if T <= 180: modulos_necesarios["012"] += 1
        else: modulos_necesarios["013"] += 1
    elif Resto_S == 6:
        if T <= 60: modulos_necesarios["012"] += 1
        elif 60 < T < 500: modulos_necesarios["013"] += 1
        else: 
            modulos_necesarios["012"] += 1
            modulos_necesarios["013"] += 1

    # 11. Módulos EXERCISE (014 y 015)
    Bloques_E = P // 12
    Resto_E = P % 12
    if T <= 30:
        modulos_necesarios["014"] += 2 * Bloques_E
    elif 30 < T < 500:
        modulos_necesarios["014"] += 1 * Bloques_E
        modulos_necesarios["015"] += 1 * Bloques_E
    else:
        modulos_necesarios["015"] += 2 * Bloques_E

    if 1 <= Resto_E <= 4:
        if T < 500: modulos_necesarios["014"] += 1
        else: modulos_necesarios["015"] += 1
    elif 5 <= Resto_E <= 8:
        modulos_necesarios["015"] += 1
        if T >= 500: modulos_necesarios["014"] += 1
    elif 9 <= Resto_E <= 12:
        if T <= 30: modulos_necesarios["014"] += 2
        elif 30 < T < 500:
            modulos_necesarios["014"] += 1
            modulos_necesarios["015"] += 1
        else:
            modulos_necesarios["015"] += 2

    # 12. Módulos SYSTEM (016 y 017)
    Bloques_SYS = P // 12
    Resto_SYS = P % 12
    if T <= 180:
        modulos_necesarios["017"] += 2 * Bloques_SYS
    elif 180 < T < 500:
        modulos_necesarios["016"] += 3 * Bloques_SYS
    else:
        modulos_necesarios["016"] += 2 * Bloques_SYS
        modulos_necesarios["017"] += 1 * Bloques_SYS

    if 1 <= Resto_SYS <= 4:
        if T <= 180: modulos_necesarios["016"] += 1
        elif 180 < T < 500: modulos_necesarios["017"] += 1
        else:
            modulos_necesarios["017"] += 1
            modulos_necesarios["016"] += 1 
    elif 5 <= Resto_SYS <= 6:
        if T <= 180: modulos_necesarios["016"] += 1
        elif 180 < T < 500: modulos_necesarios["016"] += 2
        else:
            modulos_necesarios["016"] += 1
            modulos_necesarios["017"] += 1
    elif 7 <= Resto_SYS <= 8:
        if T <= 180: modulos_necesarios["017"] += 1
        elif 180 < T < 500: modulos_necesarios["016"] += 2
        else:
            modulos_necesarios["016"] += 1
            modulos_necesarios["017"] += 1
    elif 9 <= Resto_SYS <= 10:
        if T <= 180:
            modulos_necesarios["016"] += 1
            modulos_necesarios["017"] += 1
        elif 180 < T < 500:
            modulos_necesarios["016"] += 3
        else:
            modulos_necesarios["016"] += 2
            modulos_necesarios["017"] += 1
    elif 11 <= Resto_SYS <= 12:
        if T <= 180: modulos_necesarios["017"] += 2
        elif 180 < T < 500: modulos_necesarios["016"] += 3
        else:
            modulos_necesarios["016"] += 2
            modulos_necesarios["017"] += 1

    # 11. Módulos STORAGE (018 y 019)
    # Basado en el producto de P * T
    
    T_storage = min(T, 365)
    pt_product = 0.012 * P * T_storage
    
    modulos_necesarios["019"] = math.floor(pt_product/11.9)
    if pt_product % 11.9 > 8.1:
        modulos_necesarios["019"] += 1
    elif pt_product % 11.9 != 0:
        modulos_necesarios["018"] = 1

    


    # 12. Módulos COMPUTER (020 y 021) - REGLAS ACTUALIZADAS
    Bloques_C = P // 16
    Resto_C = P % 16
    if T <= 180:
        modulos_necesarios["020"] += 2 * Bloques_C
    else:
        modulos_necesarios["021"] += 2 * Bloques_C

    if 1 <= Resto_C <= 8:
        if T <= 180: modulos_necesarios["020"] += 1
        else: modulos_necesarios["021"] += 1
    elif 9 <= Resto_C <= 12:
        modulos_necesarios["021"] += 1
    elif 13 <= Resto_C <= 16:
        if T <= 180: modulos_necesarios["020"] += 2
        else: modulos_necesarios["021"] += 2

    # 13. Módulos MEALPREP (022 y 023)
    if T <= 180:
        modulos_necesarios["022"] = math.ceil(P / 8)
    elif 180 < T < 500:
        modulos_necesarios["023"] = math.ceil(P / 8)
    else: # T >= 500
        modulos_necesarios["022"] = math.ceil(P / 8) + 1

    # 14. Módulos MEDICAL (024 y 025)
    Bloques_M = P // 12
    Resto_M = P % 12
    if T <= 180:
        modulos_necesarios["025"] += 2 * Bloques_M
    else:
        modulos_necesarios["024"] += 2 * Bloques_M

    if 1 <= Resto_M <= 4:
        if T <= 180: modulos_necesarios["024"] += 1
        else: modulos_necesarios["025"] += 1
    elif 5 <= Resto_M <= 6:
        if T <= 60: modulos_necesarios["024"] += 1
        elif 60 < T < 500: modulos_necesarios["025"] += 1
        else: modulos_necesarios["024"] += 2
    elif 7 <= Resto_M <= 8:
        if T <= 180: modulos_necesarios["025"] += 1
        elif 180 < T < 500: modulos_necesarios["025"] += 2
        else:
            modulos_necesarios["024"] += 1
            modulos_necesarios["025"] += 1
    elif 9 <= Resto_M <= 12:
        if T <= 180: modulos_necesarios["025"] += 2
        else: modulos_necesarios["024"] += 2
            
    # 15. Módulos SLEEP (026 y 027)
    Bloques_SLP = P // 4
    Resto_SLP = P % 4
    modulos_necesarios["027"] += Bloques_SLP
    if Resto_SLP in (1,2):
        modulos_necesarios["026"] += 1
    elif Resto_SLP in (3,4):
        modulos_necesarios["027"] += 1

    return modulos_necesarios

# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # --- PARÁMETROS DE ENTRADA DE LA MISIÓN ---
    numero_de_pasajeros = 30
    tiempo_en_dias = 500
    # -------------------------------------------

    print(f"Calculando módulos para una misión con {numero_de_pasajeros} pasajeros y {tiempo_en_dias} días de duración...\n")

    # Ejecutar el algoritmo
    resultado = calcular_modulos_arka(numero_de_pasajeros, tiempo_en_dias, TipoC=True)

    # Imprimir los resultados de forma clara
    print("--- INVENTARIO DE MÓDULOS NECESARIOS PARA EL ARKA ---")
    for codigo, cantidad in resultado.items():
        if cantidad > 0:
            nombre_modulo = MODULOS_INFO.get(codigo, "Desconocido")
            print(f"- Módulo {codigo} ({nombre_modulo}): {cantidad} unidad(es)")
    print("-----------------------------------------------------")