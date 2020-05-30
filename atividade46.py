def computepay (hours, rate):
    if hours > 40:
        hex = hours - float(40) #5
        rateex = float(1.5) * rate #1.5*10.50 = 15.75
        exval = (hex * rateex) #5*15.75 = 78.75
        finalvalue = ((float (40) * rate) + exval) #40*10.50+78.75 =
    else:
        finalvalue = (hours * rate)

    return finalvalue

hrs = input ("Enter Hours:")
h = float (hrs)
rateinput = input("Enter Rate:")
r = float (rateinput)

p = computepay (h,r)

print ("Pay", p)
