import numpy as np

def cargar_datos(ruta_archivo):
    """
    Carga los datos del archivo CSV utilizando NumPy.

    Parameters
    ----------
    ruta_archivo : str
        Ruta del archivo CSV que contiene los datos.

    Returns
    -------
    datos : numpy.ndarray
        Un array de NumPy con los datos contenidos en el archivo CSV.
    """
    datos = np.genfromtxt(ruta_archivo, delimiter=',', dtype=None, names=True, encoding='utf-8')
    return datos

if __name__ == "__main__":
    ruta_archivo = '../data/retail_sales_dataset.csv'
    datos = cargar_datos(ruta_archivo)
    print(datos)