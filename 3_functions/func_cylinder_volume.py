r = int(input("Radius: "))
h = int(input("Height: "))

#function with 2 arguments
def cylinder_volume(radius, height):
    '''
    :param radius: Radius of cylinder
    :param height: Height of cylinder
    :return: Volume of cylinder
    '''
    volume = (radius**2) * 3.14 * height
    return volume

# function with default value set to an argument
def cylinder_volume_constant_height(radius, height = 7):
    '''
    :param height: Default value of height of cylinder
    :param radius: Radius of cylinder
    :return: Volume of cylinder
    '''
    volume = (radius**2) * 3.14 * height
    return volume

print(cylinder_volume(r, h)) #positional arg passing
print(cylinder_volume(height = h, radius = r)) #keyword arg passing
print(cylinder_volume_constant_height(r))