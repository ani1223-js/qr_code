import qrcode as qr


val = int(input("how many rolls do you want to attach: "))
roll = input(" Enter the roll number and skip the last value for iteration and see the magic ")
for i in range(1,val+1):
    new_roll = roll+str(i)
    Qr = qr.make(new_roll)
    Qr.save( f"your file_{i}.png")
    i += 1
    
print("successfully  qr code completed")
print(" please check your files")    
    
   
    






