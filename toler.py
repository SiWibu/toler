import time
import os

print("")
print("::::::::::::   ...         ...      .,::      .:")
print(";;;;;;;;''''.;;;;;;;.   .;;;;;;;.   `;;;,  .,;; ")
print("     [[    ,[[     \[[,,[[     \[[,   '[[,,[['  ")
print("     $$    $$$,     $$$$$$,     $$$    Y$$$P    ")
print("     88,   'www,_ _,SSS'FFF,_ _,88P  oP'AAA'Yo, ")
print("     MMM     'YMMMMMP"   "YMMMMMP',m'       'Mm,")
print("------------------------------------------------")
print("                Create By:SX7H                  ")
print("")
print("[1] sqliv (sqli/dorks scanner)")
print("[2] ")
print("[3] ")
print("[4] Exit")
print("")

select = input("Select Numbers: ")

if select == "1":
  print("Install sqliv...")
  time.sleep(2)
  os.system("git clone https://github.com/the-robot/sqliv.git")
  os.system("cd")
  os.system("cd sqliv")
  os.system("python2 setup.py -i")
  os.system("python2 sqliv.py")
else:
  print("Please Select Numbers!")
  time.sleep(1)




