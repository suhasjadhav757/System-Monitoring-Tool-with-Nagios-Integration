import psutil
import logging
import configparser

# Initialize logging
logging.basicConfig(filename='monitoring.log', level=logging.ERROR)

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Function to monitor CPU usage
def monitor_cpu():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        threshold = config.getfloat('thresholds', 'cpu')
        if cpu_usage > threshold:
            logging.error(f"High CPU Usage: {cpu_usage}%")
            print(f"Alert: High CPU Usage ({cpu_usage}%)")
        else:
            print(f"CPU Usage: {cpu_usage}%")
    except Exception as e:
        logging.error(f"Error monitoring CPU usage: {e}")

# Function to monitor memory usage
def monitor_memory():
    try:
        memory_usage = psutil.virtual_memory().percent
        threshold = config.getfloat('thresholds', 'memory')
        if memory_usage > threshold:
            logging.error(f"High Memory Usage: {memory_usage}%")
            print(f"Alert: High Memory Usage ({memory_usage}%)")
        else:
            print(f"Memory Usage: {memory_usage}%")
    except Exception as e:
        logging.error(f"Error monitoring memory usage: {e}")

# Function to monitor disk usage
def monitor_disk():
    try:
        disk_usage = psutil.disk_usage('/').percent
        threshold = config.getfloat('thresholds', 'disk')
        if disk_usage > threshold:
            logging.error(f"High Disk Usage: {disk_usage}%")
            print(f"Alert: High Disk Usage ({disk_usage}%)")
        else:
            print(f"Disk Usage: {disk_usage}%")
    except Exception as e:
        logging.error(f"Error monitoring disk usage: {e}")

if __name__ == "__main__":
    monitor_cpu()
    monitor_memory()
    monitor_disk()
