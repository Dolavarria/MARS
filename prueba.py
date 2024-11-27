import matplotlib.pyplot as plt

def leer_archivo(nombre_archivo: str) -> tuple:
    meses = []
    iquique = []
    san_antonio = []
    coronel = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split()
            if datos:
                meses.append(datos[0])
                iquique.append(float(datos[1]))
                san_antonio.append(float(datos[2]))
                coronel.append(float(datos[3]))
    return meses, iquique, san_antonio, coronel

def calcular_arancel(montos: list, tasa: float) -> list:
    aranceles = [monto * tasa for monto in montos]
    return aranceles

def calcular_total(aranceles_iq: list, aranceles_sa: list, aranceles_co: list) -> list:
    total = [iq + sa + co for iq, sa, co in zip(aranceles_iq, aranceles_sa, aranceles_co)]
    return total

def graficar(meses: list, aranceles_iq: list, aranceles_sa: list, aranceles_co: list, total: list):
    plt.plot(meses, aranceles_iq, label='Iquique')
    plt.plot(meses, aranceles_sa, label='San Antonio')
    plt.plot(meses, aranceles_co, label='Coronel')
    plt.plot(meses, total, label='Total')
    plt.title('Recaudaciones por Puerto y Total')
    plt.xlabel('Meses')
    plt.ylabel('Recaudación')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def iniciar():
    nombre_archivo = 'datos.txt'
    meses, iquique, san_antonio, coronel = leer_archivo(nombre_archivo)
    arancel_iq = calcular_arancel(iquique, 0.0015)
    arancel_sa = calcular_arancel(san_antonio, 0.0028)
    arancel_co = calcular_arancel(coronel, 0.0039)
    total = calcular_total(arancel_iq, arancel_sa, arancel_co)
    graficar(meses, arancel_iq, arancel_sa, arancel_co, total)

iniciar()