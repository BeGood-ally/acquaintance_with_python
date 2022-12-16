import math

def enter_of_coord(str1, str2):
    while True:
        print(f'введите координату {str1} точки {str2}')
        coord = input()
        try:
            dcoord = float(coord)
        except Exception:
            print("вы ввели не цифру")
        else:
            return dcoord

def distance_between_spots(AX, AY, BX, BY):
    print(round(math.sqrt((BX-AX)**2+(BY-AY)**2),2))

distance_between_spots(enter_of_coord("X","A"),
                       enter_of_coord("Y","A"),
                       enter_of_coord("X","B"),
                       enter_of_coord("Y","B"))
