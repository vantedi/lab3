from threading import Thread
import csv
import time
import psutil
import pynput.mouse as mouse
import codecs

def get_cpu_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    return round(cpu_percent, 2)

def get_mouse_metrics():
    mouse_seconds = mouse.Controller().position[0]
    return int(mouse_seconds)

def save_metrics():
    while True:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        cpu_metrics = get_cpu_metrics()
        mouse_metrics = get_mouse_metrics()

        with codecs.open('metrics.csv', '+a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, 'CPU', cpu_metrics])
            writer.writerow([current_time, 'Mouse', mouse_metrics])

        time.sleep(60)

metrics_thread = Thread(target=save_metrics)
metrics_thread.start()