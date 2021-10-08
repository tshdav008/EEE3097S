# importing all the required libraries
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import threading
from time import time
start1 = time()

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create count for changing the interval when pressing the button
count = 10
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P1)
# create the button and initialise it as it is connected to D23
button = digitalio.DigitalInOut(board.D23)
button.dirrection =digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
# allows the person to nly press the button only once per runtime
number_presses = 0
# function for using the button wisely
def button_callback():
 global number_presses
 number_presses = 1;
 global count
# change the interval(count) when ever the button is pressed
 if count == 10:
  count = 5
 elif count == 5:
  count = 0
 else:
  count = 10
 print("Interval changed to",str(count)+"s")

def Display_Results_using_Threads():
 global number_presses
 number_presses = 0;
 global start
 global count
# using the threading timer to time the thread to wait for specific seconds as specified
#by pressing the button
 thread = threading.Timer(count, Display_Results_using_Threads)
 thread.daemon=True
 thread.start()
 end = int(time() − start1)
# converting temperature from volts to degrees C
 temp = round(((chan.voltage−0.5)/0.01),3)
 print("{:<11}{:<16}{:<10}C".format(str(end)+"s",chan.value,temp))

if __name__ == "__main__":
 print("Runtime Temp Reading Temp")
 Display_Results_using_Threads()
# the program must run for a maximum of 1 minute but with the interval varying
#but the button
 start = time() +70
 while True:
  if time()>start:
   break
  if not button.value:
  if number_presses<1:
    button_callback() # calling the button method when the button is pressed

def button_callback():
 global number_presses
 number_presses = 1;
 global count
# change the interval(count) when ever the button is pressed
 if count == 10:
  count = 5
 elif count == 5:
  count = 0
 else:
  count = 10
 print("Interval changed to",str(count)+"s")

if __name__ == "__main__":
 print("Runtime Temp Reading Temp")
 main()
  # the program must run for a maximum of 1 minute but with the interval varying
   #but the button
 start = time() +70
 while True:
  if time()>start:
   break
  if not button.value:
  if number_presses<1:
   button_callback() # calling the button method when the button is pressed


