# This project takes in coordinates and relays if one object is inside another




import math
from sys import stdin


class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return ("(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")")

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        #  because self values are 0, these are for other?
        dist_x = (self.x - other.x) ** 2
        dist_y = (self.y - other.y) ** 2
        dist_z = (self.z - other.z) ** 2

        distance = math.sqrt(dist_x + dist_y + dist_z)

        return (distance)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.center = Point(x,y,z)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):

        center_string = "Center: " + str(self.center)
        radius_string = "Radius: " + self.radius

        return (center_string + ", " + radius_string)

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):

        return (4 * math.pi * (self.radius ** 2))

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):

        return ((4 / 3) * (math.pi * self.radius ** 3))

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):

        point_distance = Point.distance(self.center, p)
        return (point_distance < self.radius)

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        #  write a helper function given the center and side, find the 8 coordinates
        #  sphereA is the big one (self)
        #  checking if sphereB (other) is inside sphereA

        sphereA_diameter = self.radius * 2
        sphereB_diameter = other.radius * 2

        sphereA_x_min = self.x - self.radius
        sphereA_x_max = self.x + self.radius
        sphereA_y_min = self.y - self.radius
        sphereA_y_max = self.y + self.radius
        sphereA_z_min = self.z - self.radius
        sphereA_z_max = self.z + self.radius

        sphereB_x_min = other.x - other.radius
        sphereB_x_max = other.x + other.radius
        sphereB_y_min = other.y - other.radius
        sphereB_y_max = other.y + other.radius
        sphereB_z_min = other.z - other.radius
        sphereB_z_max = other.z + other.radius

        if (sphereB_diameter < sphereA_diameter) \
                and (sphereA_x_min < sphereB_x_min) and (sphereA_x_max > sphereB_x_max) \
                and (sphereA_y_min < sphereB_y_min) and (sphereA_y_max > sphereB_y_max) \
                and (sphereA_z_min < sphereB_z_min) and (sphereA_z_max > sphereB_z_max):
            return True

        else:
            return False

    #  this tests that two spheres are strictly outside each other
    def is_all_outside_sphere(self, other):

        sphereA_x_min = self.x - self.radius
        sphereA_x_max = self.x + self.radius
        sphereA_y_min = self.y - self.radius
        sphereA_y_max = self.y + self.radius
        sphereA_z_min = self.z - self.radius
        sphereA_z_max = self.z + self.radius

        sphereB_x_min = other.x - other.radius
        sphereB_x_max = other.x + other.radius
        sphereB_y_min = other.y - other.radius
        sphereB_y_max = other.y + other.radius
        sphereB_z_min = other.z - other.radius
        sphereB_z_max = other.z + other.radius

        #  if max of other sphere is less than min of self sphere, or if min of other sphere is greater than max of self sphere
        #     then, it is outside
        if (sphereB_x_max < sphereA_x_min or sphereB_x_min > sphereA_x_max) \
                or (sphereB_y_max < sphereA_y_min or sphereB_y_min > sphereA_y_max) \
                or (sphereB_z_max < sphereA_z_min or sphereB_z_min > sphereA_z_max):
            return True
        else:
            return False

        #  return true if it is completely outside

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are inside
    # the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):

        cube_diagonal = math.sqrt(3 * a_cube.side ** 2)
        sphere_diameter = self.radius * 2

        sphere_x_min = self.x - self.radius
        sphere_x_max = self.x + self.radius
        sphere_y_min = self.y - self.radius
        sphere_y_max = self.y + self.radius
        sphere_z_min = self.z - self.radius
        sphere_z_max = self.z + self.radius

        cube_x_min = a_cube.x - a_cube.side / 2
        cube_x_max = a_cube.x + a_cube.side / 2
        cube_y_min = a_cube.y - a_cube.side / 2
        cube_y_max = a_cube.y + a_cube.side / 2
        cube_z_min = a_cube.z - a_cube.side / 2
        cube_z_max = a_cube.z + a_cube.side / 2

        if (cube_diagonal < sphere_diameter) \
                and (sphere_x_min < cube_x_min) and (sphere_x_max > cube_x_max) \
                and (sphere_y_min < cube_y_min) and (sphere_y_max > cube_y_max) \
                and (sphere_z_min < cube_z_min) and (sphere_z_max > cube_z_max):
            return True

        else:
            return False

    def is_all_outside_cube(self, a_cube):

        cube_x_min = a_cube.x - a_cube.side / 2
        cube_x_max = a_cube.x + a_cube.side / 2
        cube_y_min = a_cube.y - a_cube.side / 2
        cube_y_max = a_cube.y + a_cube.side / 2
        cube_z_min = a_cube.z - a_cube.side / 2
        cube_z_max = a_cube.z + a_cube.side / 2

        sphere_x_min = self.x - self.radius
        sphere_x_max = self.x + self.radius
        sphere_y_min = self.y - self.radius
        sphere_y_max = self.y + self.radius
        sphere_z_min = self.z - self.radius
        sphere_z_max = self.z + self.radius

        if (cube_x_max < sphere_x_min or cube_x_min > sphere_x_max) \
                or (cube_y_max < sphere_y_min or cube_y_min > sphere_y_max) \
                or (cube_z_max < sphere_z_min or cube_z_min > sphere_z_max):
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):

        #  diagonal of a cylinder is the diameter_sphere of the sphere
        #  diagonal must be less than the diamter_sphere

        cyl_base_diam = a_cyl.radius * 2
        cyl_diag = math.sqrt(a_cyl.height ** 2 + cyl_base_diam ** 2)

        sphere_diam = self.radius * 2
        cyl_diag < sphere_diam

    # determine if another Sphere intersects this Sphere
    # there is a non-zero volume of intersection
    # other is a Sphere object
    # returns a Boolean
    def does_intersect_sphere(self, other):

        if (is_inside_sphere(self, other) == False) and (is_all_outside_sphere(self, other) == False):
            return True
        else:
            return False

    # determine if a Cube intersects this Sphere
    # there is a non-zero volume of intersection
    # there is at least one corner of the Cube in
    # the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):

        if (is_inside_cube(self, a_cube) == False) and (is_all_outside_cube(self, a_cube) == False):
            return True
        else:
            return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):

        sphere_diameter = self.radius * 2
        side = math.sqrt((sphere_diameter ** 2) / 3)

        cube = Cube(self.x, self.y, self.z, side)

        return cube


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):

        self.x = x
        self.y = y
        self.z = z
        self.side = side

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):

        center_string = "Center: " + "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
        side_string = "Side: " + self.side

        return (center_string + ", " + side_string)

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):

        return (6 * self.side ** 2)

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):

        return (self.side ** 3)

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):

        hypotenuse = math.sqrt(2 * (self.side ** 2))
        half_hyp = hypotenuse / 2

        if (abs(p.x - self.x < self.side / 2)) and (abs(p.y - self.y < self.side / 2)) and (
        abs(p.z - self.z < half_hyp)):
            return True

        else:
            return False

        # x of p is within x min and x max, etc. ; should it be the hypotenuse instead?

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        #  if all 8 vertices are inside, it is inside
        sphere_diameter = a_sphere.radius * 2
        sphere_diameter < self.side

        sphere_x_min = a_sphere.x - a_sphere.radius
        sphere_x_max = a_sphere.x + a_sphere.radius
        sphere_y_min = a_sphere.y - a_sphere.radius
        sphere_y_max = a_sphere.y + a_sphere.radius
        sphere_z_min = a_sphere.z - a_sphere.radius
        sphere_z_max = a_sphere.z + a_sphere.radius

        cube_x_min = self.x - self.side / 2
        cube_x_max = self.x + self.side / 2
        cube_y_min = self.y - self.side / 2
        cube_y_max = self.y + self.side / 2
        cube_z_min = self.z - self.side / 2
        cube_z_max = self.z + self.side / 2

        if (sphere_diameter < self.side) \
                and (sphere_x_min > cube_x_min) and (sphere_x_max < cube_x_max) \
                and (sphere_y_min > cube_y_min) and (sphere_y_max < cube_y_max) \
                and (sphere_z_min > cube_z_min) and (sphere_z_max < cube_z_max):
            return True

        else:
            return False

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        #  cubeA is the big cube
        #  see if cubeB fits into cubeA

        #  this is for a regularly oriented cube – need to figure out slight rotations
        a_x_min = self.x - self.side / 2
        b_x_min = other.x - other.side / 2

        a_x_max = self.x + self.side / 2
        b_x_max = other.x + other.side / 2

        a_y_min = self.y - self.side / 2
        b_y_min = other.y - other.side / 2

        a_y_max = self.y + self.side / 2
        b_y_max = other.y + other.side / 2

        a_z_min = self.z - self.side / 2
        b_z_min = other.z - other.side / 2

        a_z_max = self.z + self.side / 2
        a_z_max = other.z + other.side / 2

        if (b_x_min > a_x_min) and (b_x_max < a_x_max) and (b_y_min > a_y_min) and (b_y_max < a_y_max) and (
                b_z_min > a_z_min) and (b_z_max < a_z_max):
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        pass

    # determine if another Cube intersects this Cube
    # there is a non-zero volume of intersection
    # there is at least one vertex of the other Cube
    # in this Cube
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        pass

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        pass

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):

        sphere_radius = self.side / 2
        sphere = Sphere(self.x, self.y, self.z, sphere_radius)

        return sphere


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):

        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):

        center_string = "Center: " + "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
        radius_string = "Radius: " + self.radius
        height_string = "Height: " + self.height

        return (center_string + ", " + radius_string + ", " + height_string)

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):

        return (2 * math.pi * radius * height) + (2 * math.pi * (radius ** 2))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):

        return (math.pi * (radius ** 2) * height)

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):

        cylinder_hypot = math.sqrt((self.radius ** 2) + ((self.height / 2) ** 2))

        if (abs(p.x - self.x < self.radius)) and (abs(p.y - self.y < self.height / 2)) and (
        abs(p.z - self.z < cylinder_hypot)):
            return True

        else:
            return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        pass

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are in
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        pass

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        pass

    # determine if another Cylinder intersects this Cylinder
    # there is a non-zero volume of intersection
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        pass


def main():
    # read data from standard input

    # read the coordinates of the first Point p
    p_coords = input()

    # create a Point object
    p_coords = p_coords.split()

    for i in range(0, 3):
        p_coords[i] = int(float(p_coords[i]))

    px = (p_coords[0])
    py = (p_coords[1])
    pz = (p_coords[2])
    point_p = Point(px, py, pz)

    # read the coordinates of the second Point q
    q_coords = input()

    # create a Point object
    q_coords = q_coords.split()

    for i in range(0, 3):
        q_coords[i] = int(float(q_coords[i]))

    qx = (q_coords[0])
    qy = (q_coords[1])
    qz = (q_coords[2])
    point_q = Point(qx, qy, qz)

    # read the coordinates of the center and radius of sphereA
    sphereA_coords = input()

    # create a Sphere object
    sphereA_coords = sphereA_coords.split()

    for i in range(0, 4):
        sphereA_coords[i] = int(float(sphereA_coords[i]))

    sphereAx = sphereA_coords[0]
    sphereAy = sphereA_coords[1]
    sphereAz = sphereA_coords[2]
    sphereArad = sphereA_coords[3]
    sphereA = Sphere(sphereAx, sphereAy, sphereAz, sphereArad)

    # read the coordinates of the center and radius of sphereB
    sphereB_coords = input()

    # create a Sphere object
    sphereB_coords = sphereB_coords.split()

    for i in range(0, 4):
        sphereB_coords[i] = int(float(sphereB_coords[i]))

    sphereBx = sphereB_coords[0]
    sphereBy = sphereB_coords[1]
    sphereBz = sphereB_coords[2]
    sphereBrad = sphereB_coords[3]
    sphereB = Sphere(sphereBx, sphereBy, sphereBz, sphereBrad)

    # read the coordinates of the center and side of cubeA
    cubeA_coords = input()

    # create a Cube object
    cubeA_coords = cubeA_coords.split()

    for i in range(0, 4):
        cubeA_coords[i] = int(float(cubeA_coords[i]))

    cubeAx = cubeA_coords[0]
    cubeAy = cubeA_coords[1]
    cubeAz = cubeA_coords[2]
    cubeAside = cubeA_coords[3]
    cubeA = Cube(cubeAx, cubeAy, cubeAz, cubeAside)

    # read the coordinates of the center and side of cubeB
    cubeB_coords = input()

    # create a Cube object
    cubeB_coords = cubeB_coords.split()

    for i in range(0, 4):
        cubeB_coords[i] = int(float(cubeB_coords[i]))

    cubeBx = cubeB_coords[0]
    cubeBy = cubeB_coords[1]
    cubeBz = cubeB_coords[2]
    cubeBside = cubeB_coords[3]
    cubeB = Cube(cubeBx, cubeBy, cubeBz, cubeBside)

    # read the coordinates of the center, radius and height of cylA
    cylA_coords = input()

    # create a Cylinder object
    cylA_coords = cylA_coords.split()

    for i in range(0, 5):
        cylA_coords[i] = int(float(cylA_coords[i]))

    cylAx = cylA_coords[0]
    cylAy = cylA_coords[1]
    cylAz = cylA_coords[2]
    cylArad = cylA_coords[3]
    cylAheight = cylA_coords[4]

    cylA = Cylinder(cylAx, cylAy, cylAz, cylArad, cylAheight)

    # read the coordinates of the center, radius and height of cylB
    cylB_coords = input()

    # create a Cylinder object
    cylB_coords = cylB_coords.split()

    for i in range(0, 5):
        cylB_coords[i] = int(float(cylB_coords[i]))

    cylBx = cylB_coords[0]
    cylBy = cylB_coords[1]
    cylBz = cylB_coords[2]
    cylBrad = cylB_coords[3]
    cylBheight = cylB_coords[4]

    cylB = Cylinder(cylBx, cylBy, cylBz, cylBrad, cylBheight)

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    origin = Point(0, 0, 0)
    p_orig_dist = Point.distance(origin, point_p)
    q_orig_dist = Point.distance(origin, point_q)

    if (p_orig_dist > q_orig_dist):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

    # print if Point p is inside sphereA
    if (Sphere.is_inside_point(sphereA, point_p)):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

     # print if sphereB is inside sphereA
    if(Sphere.is_inside_sphere(sphereA, sphereB)):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    if (Sphere.is_inside_cube(sphereA, cubeA)):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    if(Sphere.is_inside_cyl(sphereA, cylA)):
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    #print if sphereA intersects with sphereB
    if(Sphere.does_intersect_sphere(sphereA, sphereB)):
        print("sphereA does intersect sphereB")
    else:
       print("sphereA does not intersect sphereB")

    # print if cubeB intersects with sphereB
    # if(Sphere.does_intersect_cube(sphereB, cubeB) == True):
    #   print("cubeB does intersect sphereB")
    # else:
    #   print("cubeB does not intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    # largest_circumscribed_cube = Sphere.circumscribe_cube(sphereA)
    # if(Cube.volume(largest_circumscribed_cube) > Cylinder.volume(cylA) == True):
    #   print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    # else:
    #   print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

    # print if Point p is inside cubeA
    if (Cube.is_inside_point(cubeA, point_p) == True):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    # if(Cube.is_inside_sphere(cubeA, sphereA)== True):
    #   print("sphereA is inside cubeA")
    # else:
    #   print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    # if(Cube.is_inside_cube(cubeA, cubeB) == True):
    #   print("cubeB is inside cubeA")
    # else:
    #   print("cubeB is not inside cubeA")

    # print if cylA is inside cubeA
    # if(Cube.is_inside_cylinder(cubeA, cylA) == True):
    #   print("cylA is inside cubeA")
    # else:
    #   print("cylA is not inside cubeA")

    # print if cubeA intersects with cubeB
    # if(Cube.does_intersect_cube(cubeA, cubeB) == True):
    #   print("cubeA does intersect cubeB")
    # else:
    #   print("cubeA does not intersect cubeB")

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    # if(Cube.intersection_volume(cubeA, cubeB) > Sphere.volume(sphereA) == True):
    #   print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    # else:
    #   print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    # largest_inscribed_sphere = Cube.inscribe_sphere(cubeA)
    # area_largest_inscribed_sphere = Sphere.area(largest_inscribed_sphere)
    # if(area_largest_inscribed_sphere > Cylinder.area(cylA) == True):
    #   print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    # else:
    #   print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

    # print if Point p is inside cylA
    if (Cylinder.is_inside_point(cylA, point_p) == True):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    # if(Cylinder.is_inside_sphere(cylA, sphereA) == True):
    #   print("sphereA is inside cylA")
    # else:
    #   print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    # if(Cylinder.is_inside_cube(cylA, cubeA) == True):
    #   print("cubeA is inside cylA")
    # else:
    #   print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    # if(Cylinder.is_inside_cylinder(cylA, cylB) == True):
    #   print("cylB is inside cylA")
    # else:
    #   print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    # if(Cylinder.does_intersect_cylinder(cylA, cylB) == True):
    #   print("cylB does intersect cylA")
    # else:
    #   print("cylB does not intersect cylA")


if __name__ == "__main__":
    main()
