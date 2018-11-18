import time

print("\n%Y/%d/%m - %H:%M:%S   "+time.strftime("%Y/%d/%m - %H:%M:%S"))	# år / månad / dag - timme:minut:sekunder
print("")
print("%c                    "+ time.strftime("%c"))	# Thu Oct 19 23:37:43 2017
print("")
print("%A %B                 "+time.strftime("%A %B"))  # Wednesday February
print("\n\n\nThis is my Test\n")

print(time.strftime("%H:%M:%S"))
print(time.strftime("%A %d/%m"))
print()
"""
TIME (big font)
Torsdag 12/02


%A 
%d %m
"""