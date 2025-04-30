import time
import random

# Фейковые данные доходности (в реале — API WhatToMine)
COINS = {
    "Monero": {"hashrate": 5000, "profit": 0.005},  # KH/s, $/day
    "ETC": {"hashrate": 20, "profit": 0.01},       # MH/s, $/day
    "Ravencoin": {"hashrate": 15, "profit": 0.008} # MH/s, $/day
}
COMPUTE = {"rendering": {"hashrate": 10, "profit": 0.02}}  # GH/s, $/day

# Функция AI-агента GameForge
def gameforge_agent(cpu_usage, gpu_usage, temp):
    print(f"CPU: {cpu_usage}%, GPU: {gpu_usage}%, Temp: {temp}°C")
    
    # Ограничения по температуре
    if temp > 80:
        power = 30
        print("Temp > 80°C! Reducing to 30% power.")
    elif cpu_usage > 60:  # Игра
        power = 10
        print("Gaming detected! Setting 10% power.")
    elif cpu_usage < 10:  # Простой
        power = 100
        print("Idle detected! Full 100% power.")
    else:  # Видео/браузер
        power = 80
        print("Light usage! Setting 80% power.")
    
    # Выбор лучшей задачи
    best_task = max(COINS | COMPUTE, key=lambda x: COINS.get(x, COMPUTE.get(x))["profit"])
    hashrate = COINS.get(best_task, COMPUTE.get(best_task))["hashrate"] * (power / 100)
    profit = COINS.get(best_task, COMPUTE.get(best_task))["profit"] * (power / 100)
    
    print(f"GameForge chose: {best_task} | Hashrate: {hashrate:.2f} | Profit: ${profit:.3f}/day")
    return best_task, hashrate, profit

# Тест сценариев
scenarios = [
    {"cpu_usage": 70, "gpu_usage": 20, "temp": 65},  # Игра
    {"cpu_usage": 5, "gpu_usage": 10, "temp": 50},   # Простой
    {"cpu_usage": 20, "gpu_usage": 30, "temp": 85}   # Перегрев
]

for scenario in scenarios:
    print("\nTesting GameForge:")
    task, hashrate, profit = gameforge_agent(**scenario)
    time.sleep(1)  # Имитация работы
