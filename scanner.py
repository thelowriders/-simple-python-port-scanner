import socket
import sys
from datetime import datetime
import threading
from queue import Queue

# Configuration
TARGET = "127.0.0.1"  # Localhost for safe, legal testing
THREADS = 50           # Number of ports to test at the exact same time
print_lock = threading.Lock()

print("-" * 50)
print(f"Scanning target: {TARGET}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

# The queue will hold all the port numbers we want to scan (1 to 1024)
queue = Queue()

def port_scan(port):
    """Attempts to connect to a specific port on the target host."""
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 second timeout so it doesn't hang
        
        # Connect to target IP and port
        result = s.connect_ex((TARGET, port))
        
        if result == 0:
            # Thread-safe printing using a lock
            with print_lock:
                print(f"Port {port}: OPEN")
                # Log the results to a file
                with open("scan_results.log", "a") as log_file:
                    log_file.write(f"[{datetime.now()}] Port {port} is OPEN\n")
        s.close()
    except Exception:
        pass

def thread_worker():
    """Worker function that pulls ports out of the queue and scans them."""
    while not queue.empty():
        port = queue.get()
        port_scan(port)
        queue.task_done()

# 1. Fill the queue with standard ports (1 to 1024)
for port in range(1, 1025):
    queue.put(port)

# 2. Spawn and start the threads
thread_list = []
for _ in range(THREADS):
    thread = threading.Thread(target=thread_worker)
    thread_list.append(thread)
    thread.start()

# 3. Wait for all threads to finish before closing the script
for thread in thread_list:
    thread.join()

print("-" * 50)
print("Scan completed successfully. Results saved to scan_results.log")
print("-" * 50)
