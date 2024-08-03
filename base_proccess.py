import psutil
import time
import subprocess



while True:

    try:
        print(f"(CPU utilization : ({psutil.cpu_percent()}) %) ") 
        print(f"(Memory utilization : ({psutil.virtual_memory().percent}) %)") 
        print('\n')
        
        time.sleep(1)

        print('\n')
        print('Press {CTRL + C}  to stop the runnig file!')
        print('Getting the proccess detail........')
        print("_" *50)

        
        
    except Exception:
        print('Restart the loop again!')
    
    

    time.sleep(1)

