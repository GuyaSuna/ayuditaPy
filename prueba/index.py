import requests

# Endpoint para obtener los datos
endpoint = 'https://api.binance.com/api/v3/klines'

# Símbolo y marco temporal
symbol = 'BTCUSDT'
interval = '15m'

# Parámetros para la solicitud
params = {
    'symbol': symbol,
    'interval': interval,
    'limit': 100
}

# Realiza la solicitud y obtiene los datos
response = requests.get(endpoint, params=params)
data = response.json()

# Extrae los precios de cierre
close_prices = [float(d[4]) for d in data]

# Calcula el EMA para 100 velas
ema100 = []
k = 2 / (100 + 1)
ema_yesterday = close_prices[0]
for i in range(1, len(close_prices)):
    ema_today = (close_prices[i] * k) + (ema_yesterday * (1 - k))
    ema100.append(ema_today)
    ema_yesterday = ema_today

# Calcula el EMA para 50 velas
ema50 = []
k = 2 / (50 + 1)
ema_yesterday = close_prices[0]
for i in range(1, len(close_prices)):
    ema_today = (close_prices[i] * k) + (ema_yesterday * (1 - k))
    ema50.append(ema_today)
    ema_yesterday = ema_today

# Calcula el EMA para 9 velas
ema9 = []
k = 2 / (9 + 1)
ema_yesterday = close_prices[0]
for i in range(1, len(close_prices)):
    ema_today = (close_prices[i] * k) + (ema_yesterday * (1 - k))
    ema9.append(ema_today)
    ema_yesterday = ema_today

# Imprime los precios de cierre y los EMAs
print(close_prices)
print(ema100[-1])
print(ema50[-1])
print(ema9[-1])
