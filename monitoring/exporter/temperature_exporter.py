from prometheus_client import start_http_server, Gauge
import requests
import time

# Definir la métrica Prometheus
temperature_gauge = Gauge('temperature_celsius', 'Current temperature in Santa Cruz de Tenerife in Celsius')

# Función para obtener la temperatura desde la API
def get_temperature():
    api_key = 'ab60180de2a359f2c47970581559444f'  
    city = 'Santa Cruz de Tenerife'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    return temperature

# Función para actualizar la métrica
def collect_temperature():
    while True:
        temperature = get_temperature()
        temperature_gauge.set(temperature)
        print(f'Updated temperature: {temperature}°C')
        time.sleep(60)  # Actualizar cada 60 segundos

if __name__ == '__main__':
    # Iniciar el servidor HTTP en el puerto 8000
    start_http_server(8000)
    print('Prometheus exporter started on port 8000')

    # Recoger la temperatura y actualizar la métrica cada cierto tiempo
    collect_temperature()
