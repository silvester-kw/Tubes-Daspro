import time

while True:
    input("Tanya dong: ")
    ms = time.time()*1000.0
    break

if ms//1 % 6 == 0:
    print("Ya")
elif ms//1 % 6 == 1:
    print("Tidak")
elif ms//1 % 6 == 2:
    print("Bisa Jadi")
elif ms//1 % 6 == 3:
    print("Mungkin")
elif ms//1 % 6 == 4:
    print("Tentunya")
else:
    print("Tidak Mungkin")