radius = int(input("Radius: "))
height = int(input("Height: "))

def cylinder_volume(radius, height):
    '''
    :param radius: Radius of cylinder
    :param height: Height of cylinder
    :return: Volume of cylinder
    '''
    volume = (radius**2) * 3.14 * height
    return volume

print(cylinder_volume(radius, height))