score = input ("Enter Score:")

try:
    s = float (score)
except:
    print ("Please, enter numeric value between 0.0 and 1.0")
    quit()
if s > float (1.0):
    print("Please, enter numeric value between 0.0 and 1.0")
elif s >=float(0.9):
    print ("Grade A")
elif s >=float(0.8):
    print ("Grade B")
elif s >=float(0.7):
    print ("Grade C")
elif s >=float(0.6):
    print ("Grade D")
elif s <float(0.6):
    print ("Grade F")
