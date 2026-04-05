# countdown timer (with 1 sec gap)

#goal :
# print a countdown before somthing "exciting" happens(linke " launching")
#"happy new year"

import time
count=int(input("Enter the coundown starting number: "))

print("\n countdown starts now:")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)

print("\nWOHOO! Happy New Year")

