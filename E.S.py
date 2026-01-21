import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime

# Datos proporcionados
#1. Desarrollar un programa en Python que grafique el tipo de cambio de compra y venta del 5 de marzo del 2024 al 3 abril del 2024
#  utilizando las librerías de gráficos de Python investigadas.

def main():
    informacion = {
        "fecha": [
            "5-mar-24", "6-mar-24", "7-mar-24", "8-mar-24", "9-mar-24", "10-mar-24",
            "11-mar-24", "12-mar-24", "13-mar-24", "14-mar-24", "15-mar-24", "16-mar-24",
            "17-mar-24", "18-mar-24", "19-mar-24", "20-mar-24", "21-mar-24", "22-mar-24",
            "23-mar-24", "24-mar-24", "25-mar-24", "26-mar-24", "27-mar-24", "28-mar-24",
            "29-mar-24", "30-mar-24", "31-mar-24", "1-abr-24", "2-abr-24", "3-abr-24"
        ],
        "tipo_cambio_compra": [
            509.76, 509.71, 508.65, 507.33, 506.33, 506.33, 506.33, 504.92, 504.10, 503.92,
            503.53, 501.37, 501.37, 501.37, 499.72, 500.67, 499.86, 500.92, 499.42, 499.42,
            499.42, 500.89, 499.32, 499.39, 499.39, 499.39, 499.39, 499.39, 497.74, 497.70
        ],
        "tipo_cambio_venta": [
            515.95, 515.07, 513.76, 512.99, 512.51, 512.51, 512.51, 511.45, 510.75, 509.98,
            509.43, 507.89, 507.89, 507.89, 505.80, 505.74, 505.84, 505.97, 505.68, 505.68,
            505.68, 505.36, 505.99, 506.60, 506.60, 506.60, 506.60, 506.60, 505.73, 504.75
        ] 
    }
if __name__ == "__main__":
    main()

def main(): 

    # Crear un DataFrame de pandas
    df = pd.DataFrame()
    # Convertir la columna fecha a formato datetime
    df['fecha'] = pd.to_datetime(df['fecha'], format='%d-%b-%y')
    # Configurar el estilo del gráfico
    plt.style.use('seaborn')
    plt.figure(figsize=(12, 6))
    # Graficar las líneas de compra y venta
    plt.plot(df['fecha'], df['tipo_cambio_compra'], label='Tipo de Cambio Compra', 
             color='blue', marker='o', linestyle='-', linewidth=2)
    plt.plot(df['fecha'], df['tipo_cambio_venta'], label='Tipo de Cambio Venta',
                color='red', marker='s', linestyle='-', linewidth=2)
    # Configurar título y etiquetas
    plt.title('Tipo de Cambio de Compra y Venta (5-mar-24 al 3-abr-24)', fontsize=14, pad=20)
    plt.xlabel('Fecha', fontsize=12)
    plt.ylabel('Tipo de Cambio', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    # Formatear el eje x para mostrar fechas correctamente
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))
    plt.gcf().autofmt_xdate()  # Rotar fechas para mejor legibilidad
    # Mostrar leyenda
    plt.legend(fontsize=10)
    # Añadir anotaciones para los valores mínimo y máximo
    max_compra = df['tipo_cambio_compra'].max()
    min_compra = df['tipo_cambio_compra'].min()
    max_venta = df['tipo_cambio_venta'].max()
    min_venta = df['tipo_cambio_venta'].min()
    plt.annotate(f'Máx Compra: {max_compra}', xy=(df['fecha'][df['tipo_cambio_compra'].idxmax()], max_compra),
                 xytext=(10, 10), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='blue'))
    plt.annotate(f'Mín Compra: {min_compra}', xy=(df['fecha'][df['tipo_cambio_compra'].idxmin()], min_compra),
                    xytext=(10, -20), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='blue'))
    plt.annotate(f'Máx Venta: {max_venta}', xy=(df['fecha'][df['tipo_cambio_venta'].idxmax()], max_venta),
                 xytext=(10, 10), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='red'))
    plt.annotate(f'Mín Venta: {min_venta}', xy=(df['fecha][df['tipo_cambio_venta'].idxmin()], min_venta),
                    xytext=(10, -20), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='red'))
    # Mostrar el gráfico
    plt.show()
if __name__ == "__main__":
    main()



    



