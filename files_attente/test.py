import psutil

pid_list = [p for p in psutil.process_iter()]

print(pid_list)