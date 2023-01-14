while True:

    Build_shape = input("What shape is the foundation of your building: \n A) Square. B) Rectangular. C) Circular [A/B/C]? : ")

    if Build_shape == "A":
        Build_length = float(input("Foundation length in m: "))
        Build_area = Build_length ** 2
        break
    elif Build_shape == "B":
        Build_length = float(input("Foundation length in m: "))
        Build_width = float(input("Foundation width in m: "))
        Build_area = Build_length * Build_width
        break
    elif Build_shape == "C":
        Build_radius = float(input("Foundation radius in m: "))
        import math
        Build_area = math.pi * (Build_radius ** 2)
        break
    else:
        print('Type a letter A-C')
        continue

print("The foundation has an area of " + str(round(Build_area, 2)) + "m^2")