import psutil
import logging

# This sets up a log file that records any alerts that happen
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# These are your "danger zones." If usage goes above 80%, we trigger an alert.
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0

def check_system_health():
    # 1. Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        msg = f"ALERT: High CPU Usage detected: {cpu_usage}%"
        print(msg) # Shows in your terminal
        logging.warning(msg) # Saves to system_health.log
        
    # 2. Check Memory (RAM) usage
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        msg = f"ALERT: High Memory Usage detected: {memory_info.percent}%"
        print(msg)
        logging.warning(msg)

    # 3. Check Disk space
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        msg = f"ALERT: Low Disk Space detected: {disk_info.percent}% used"
        print(msg)
        logging.warning(msg)

    print("System health check complete. Check 'system_health.log' for details.")

if __name__ == "__main__":
    check_system_health()