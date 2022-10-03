temp = int(input("Please enter the current temperature:"))

x = temp

if x > 90 and x < 110:
    print("Wear Shorts")

if x > 70 and x < 90:
    print("short sleeves are fine")

if x > 50 and x < 70:
    print("Wear a jacket")

if x > 32 and x < 50:
    print("Wear a heavy coat")

if x < 32:
    print("Stay Inside")

