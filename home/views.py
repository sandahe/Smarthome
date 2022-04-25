from django.shortcuts import render
from . import hardware
# Create your views here.


def devicesStates(devices):
     for device in devices:

        pin = devices[device][0]
        status = hardware.checkStatus(pin)
        if status ==1:
            
            devices[device].append(status)
            devices[device].append("On")
        else:
            devices[device].append(status)
            devices[device].append("Off")


    
def home(request):
    devices = {"oven":[6],"light":[21],"fan":[16]}

   
    

        

    if request.method =='POST':



        device = list(request.POST)[1] # Geeting the device name from request 


        newstate =(request.POST[device]).strip() # Get status of the device (on/off)


       
        devicePin = devices[device][0]
     

        hardware.switchState(devicePin,newstate)

        
     

        
 

        # context = {'state':devices}

        # return render(request,'home/home.html',context)
       
    
    devicesStates(devices)
    
    context ={"devices":devices} 






    return render(request,'home/home.html',context)