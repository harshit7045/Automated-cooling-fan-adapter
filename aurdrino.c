import psutil
import serial
ser = serial.Serial()                                          
ser.baudrate = 9600                                             
ser.port = "COM5"                                               
ser.open()                                                      
                  
while(1):                                                   
    cpu = psutil.cpu_percent(interval=1.2)+5             
                                                            
    if cpu < 10:
        cpuStr = "" + str(cpu)                         
    elif cpu > 100:
        cpu -= 5
        cpuStr = "" + str(cpu)                                 
    else:
        cpuStr = str(cpu)                                      

    serialDataStr = cpuStr        
    serialDataBytes = serialDataStr.encode("UTF-8")             

    print(serialDataBytes)                                      
    ser.write(serialDataBytes)                                

ser.close()