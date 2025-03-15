import time
import random
Things_to_do = ("ingnoring your father and play video games", "summon ten bananas for no apparent reason", "chop a tree", "wait for the next day to clean")
print("hello there, fellow human")
time.sleep(2)
print("I noticed that you are given the ImPoSsIbLe task of")
time.sleep(2)
print("CLEANING YOUR ROOM.")
time.sleep(2)
print("SO go out there and start", random.choice(Things_to_do))
time.sleep(3)
print("Oh, it looks like you got scolded by your father.")
time.sleep(2)
print("That's what happens if you listen to my advice")
time.sleep(2)
answer=input("So, will you clean your room, or" + random.choice(Things_to_do) )
if answer == 'clean my room':
    print("I'm so sorry, but the sun just exploded so you just died")
else:
   print('''ahahahahha you just got 
   trolled ptptptptp ur dad did not ask you to go clean your room
   it's all just a nightmare ;)''')
