import math

def dot(vector_A, vector_B):
    return vector_A.x * vector_B.x + vector_A.y * vector_B.y + vector_A.z * vector_B.z

def cross(vector_A, vector_B):
    x = vector_A.y*vector_B.z - vector_A.z*vector_B.y
    y = vector_A.z*vector_B.x - vector_A.x*vector_B.z
    z = vector_A.x*vector_B.y - vector_A.y*vector_B.x
    return Vector(x, y, z)

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f[{self.x}, {self.y}, {self.z}]

while True:
    print("Welcome to the vector calculator!")

    while True:
        print("Please select from following options. Type number of choice:")
        print("1 Dot Product")
        print("2 Cross Product")
        print("3 Find magnitude of vector")
        print("4 Add/Subtract Vectors")
        print("0 Return")
        print("")

        solution = input()

        if solution == int(1):
            print("")
            print("We will now do dot product")
            print("Please enter your vector A values")
            ax = int(input("x: "))
            ay = int(input("y: "))
            az = int(input("z: "))
            vector_A = Vector(ax,ay,az)


            print("Please enter your vector B values")
            bx = int(input("x: "))
            by = int(input("y: "))
            bz = int(input("z: "))
            vector_B = Vector(bx,by,bz)

            print("Dot Product is: ",dot(vector_A, vector_B))
            print("")
            print("")

        if solution == int(2):
            print("")
            print("We will now do cross product")
            print("")
            print("Please enter your vector A values")
            ax = int(input("x: "))
            ay = int(input("y: "))
            az = int(input("z: "))
            vector_A = Vector(ax,ay,az)


            print("Please enter your vector B values")
            bx = int(input("x: "))
            by = int(input("y: "))
            bz = int(input("z: "))
            vector_B = Vector(bx,by,bz)

            print("Cross Product is: ",cross(vector_A, vector_B))
            print("")
            print("")


        if solution == str(3):
            print("")
            print("We will now find the magnitude of a vector")
            print("Please enter your vector values")
            ax = int(input("x: "))
            ay = int(input("y: "))
            az = int(input("z: "))

            print("Magnitude: ", abs(round(float(math.sqrt(ax**2+ay**2+az**2)),2)))
            print("")
            print("")

        if solution == str(4):
            print("1 Add Vectors")
            print("2 Subtract Vectors")
            print("0 Return")

            addsub = int(input())

            while True:
                if addsub == str(1):
                    print("We will now add two vectors")
                    print("Please enter your vector A values")
                    ax = int(input("x: "))
                    ay = int(input("y: "))
                    az = int(input("z: "))
                    vector_A = Vector(ax,ay,az)


                    print("Please enter your vector B values")
                    bx = int(input("x: "))
                    by = int(input("y: "))
                    bz = int(input("z: "))
                    vector_B = Vector(bx,by,bz)

                    vector_C = Vector(ax+bx,ay+by,az+bz)

                    print(vector_C)
                    print("")
                    print("")
                    break

                if addsub == str(2):
                    print("We will now subtract two vectors")
                    print("Please enter your vector A values")
                    ax = int(input("x: "))
                    ay = int(input("y: "))
                    az = int(input("z: "))
                    vector_A = Vector(ax,ay,az)


                    print("Please enter your vector B values")
                    bx = int(input("x: "))
                    by = int(input("y: "))
                    bz = int(input("z: "))
                    vector_B = Vector(bx,by,bz)

                    vector_C = Vector(ax-bx,ay-by,az-bz)

                    print(vector_C)
                    print("")
                    print("")
                    break

                if addsub == str(0):
                    print("")
                    break

        if solution == "0":
            print("")
            break
