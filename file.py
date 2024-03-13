
try:
    f = open("hello.tst", "a")

    f = open("test.tst", "a")
print(f.readline())
print(f.readline())
f.write("hello today, tomorrow")

f.close()

except FileExistsError:

print(FileExistsError)


# to remove file
import os
os.remove("test-01.tst")

try:
   os.mkdir("downloads")

except FileExistsError:
#  print("Directory Already")'''
    
    import requests


url = "http://drive.google.com/file/d/10Bf"

r = requests.get(url)

print(r.status_code)

if r.status_code == 200:
    f =  open("my-pic.jpg", "xb")
    f.write(r.content)
    f.close()
