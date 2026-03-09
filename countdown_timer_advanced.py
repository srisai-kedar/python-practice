import time
my_time = int(input("Enter the time in seconds: "))
for x in reversed(range (my_time)):
    seconds = x % 60 
    minutes = int (x/60) % 60
    hours = int(x/3600)
    print (f"0:{minutes:02}:{seconds:02}")
    time.sleep(1)
print ("Time's Up bro.")