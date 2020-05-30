hrs = input ("Enter Hours:")
h = float (hrs)
rateinput = input("Enter Rate:")
r = float (rateinput)
if h > 40:
    hex = h - float(40) #5
    rateex = float(1.5) * r #1.5*10.50 = 15.75
    exval = (hex * rateex) #5*15.75 = 78.75
    finalvalue = ((float (40) * r) + exval) #40*10.50+78.75 =

else:
    finalvalue = (h * r)

print ("Pay:", finalvalue)
