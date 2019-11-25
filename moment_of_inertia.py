from math import *
from matplotlib import pyplot as plt

b_2 = 28.74

# Tip
rear_spar_h_tip = 0.2324
front_spar_h_tip = 0.2534
tip_dist = 0.891
theta_tip = atan((front_spar_h_tip-rear_spar_h_tip)*0.5/tip_dist)

# Root
rear_spar_h_root = 0.8606
front_spar_h_root = 0.9386
root_dist = 3.3
theta_root = atan((front_spar_h_root-rear_spar_h_root)*0.5/root_dist)

t0, t1 = 0.03, 0.01
stringer_height_0, stringer_height_1 = 0.16, 0.12
stringer_thickness_0, stringer_thickness_1 = 0.015, 0.01
cross_section_value = 3                                     # 1 corresponds to a cross section of skins only, 2 is skins + stringers on the top, 3 is stringers on top and bottom
no_stringers_top = 5                                        # Must be greater than 1 for code to work!
no_stringers_bott = 3                                       # Must be greater than 1 for code to work!


class beam:

    def __init__(self, h, l, x_coord, y_coord, beta):
        self.height = h
        self.length = l
        self.area = l*h
        self.centroid = [x_coord, y_coord]

        # Calculate moment of inertia around the centroid
        self.moi_xx = l*h/12*(l**2*(cos(beta))**2 + h**2*(sin(beta))**2)
        self.moi_yy = l*h/12*(l**2*(sin(beta))**2 + h**2*(cos(beta))**2) 
        self.moi_xy = l*h/12*cos(beta)*sin(beta)*(h**2 + l**2)

        self.x_coords = [x_coord + l/2*cos(beta) + h/2*sin(beta), x_coord + l/2*cos(beta) - h/2*sin(beta), x_coord -(l/2*cos(beta) + h/2*sin(beta)), x_coord -( l/2*cos(beta) - h/2*sin(beta))]
        self.y_coords = [y_coord + l/2*sin(beta) - h/2*cos(beta), y_coord + l/2*sin(beta) + h/2*cos(beta), y_coord -(l/2*sin(beta) - h/2*cos(beta)), y_coord -( l/2*sin(beta) + h/2*cos(beta))]
        self.x_coords.append(self.x_coords[0])
        self.y_coords.append(self.y_coords[0])

class stringer:

    # The coordinates of the position are related to the position of the corner
    def __init__(self, h, t, x_coord, y_coord, theta):
        self.height = h
        self.thickness = t
        self.area = (h-t)*t + h*t
        
        # Calculate moment of inertia around the centroid
        top_beam = beam(t, h-t, x_coord + h/2*cos(theta), y_coord + h/2*sin(theta), theta)
        bott_beam = beam(h, t, x_coord + h/2*sin(theta), y_coord - h/2*cos(theta), theta)
        self.centroid = [(top_beam.centroid[0]*top_beam.area + bott_beam.centroid[0]*bott_beam.area)/(top_beam.area+bott_beam.area), \
                         (top_beam.centroid[1]*top_beam.area + bott_beam.centroid[1]*bott_beam.area)/(top_beam.area+bott_beam.area)]
        self.moi_xx = top_beam.moi_xx + top_beam.area*(top_beam.centroid[1]-self.centroid[1])**2 + bott_beam.moi_xx + bott_beam.area*(bott_beam.centroid[1]-self.centroid[1])**2
        self.moi_yy = top_beam.moi_yy + top_beam.area*(top_beam.centroid[0]-self.centroid[0])**2 + bott_beam.moi_yy + bott_beam.area*(bott_beam.centroid[0]-self.centroid[0])**2
        self.moi_xy = top_beam.moi_xy + top_beam.area*(top_beam.centroid[0]-self.centroid[0])*(top_beam.centroid[1]-self.centroid[1]) \
                      + bott_beam.moi_xy + bott_beam.area*(bott_beam.centroid[0]-self.centroid[0])*(bott_beam.centroid[1]-self.centroid[1])

        self.x_coords = [x_coord, x_coord + h*cos(theta), x_coord + h*cos(theta) + t*sin(theta), x_coord + t*cos(theta) + t*sin(theta), x_coord + t*cos(theta) + h*sin(theta), x_coord + h*sin(theta)]
        self.y_coords = [y_coord, y_coord + h*sin(theta), y_coord + h*sin(theta) - t*cos(theta), y_coord - t*cos(theta) + t*sin(theta), y_coord + t*sin(theta) - h*cos(theta), y_coord - h*cos(theta)]
        self.x_coords.append(self.x_coords[0])
        self.y_coords.append(self.y_coords[0])

def param(initial_value, final_value, span_pos):
    return span_pos*(final_value-initial_value)/b_2 + initial_value

def initial_values(span_position):
    t, theta, dist, front_spar_h, rear_spar_h = param(t0, t1, span_position), param(theta_root, theta_tip,span_position), param(root_dist,tip_dist,span_position), param(front_spar_h_root, front_spar_h_tip, span_position), param(rear_spar_h_root, rear_spar_h_tip, span_position)
    stringer_height, stringer_thickness = param(stringer_height_0, stringer_height_1, span_position), param(stringer_thickness_0, stringer_thickness_1, span_position)
    return t, theta, dist, front_spar_h, rear_spar_h, stringer_height, stringer_thickness


def cross_section(value, span_position):
    t, theta, dist, front_spar_h, rear_spar_h, stringer_height, stringer_thickness = initial_values(span_position)

    up_sheet = beam(t, (dist - 2 * t) / cos(theta), 0, front_spar_h / 2 - (front_spar_h - rear_spar_h) / 4, -theta)
    down_sheet = beam(t, (dist - 2 * t) / cos(theta), 0, -(front_spar_h / 2 - (front_spar_h - rear_spar_h) / 4), theta)
    front_spar = beam(rear_spar_h + t, t, -dist / 2 + t / 2, 0, 0)
    rear_spar = beam(rear_spar_h - t, t, dist / 2 - t / 2, 0, 0)
    elements = [up_sheet, down_sheet, front_spar, rear_spar]

    if value == 1:
        elements = elements

    if value == 2:

        for i in range(no_stringers_top):
            if i < no_stringers_top-1:
                string = stringer(stringer_height, stringer_thickness, -(dist - 2*t)/2 + (dist - 2*t)/(no_stringers_top-1)*i, front_spar_h/2 - t - ((front_spar_h - rear_spar_h)/2)/(no_stringers_top-1)*i, 0)
                elements.append(string)
            else:
                string = stringer(stringer_height, stringer_thickness, -(dist - 2*t)/2 + (dist - 2*t)/(no_stringers_top-1)*i, front_spar_h/2 - t - ((front_spar_h - rear_spar_h)/2)/(no_stringers_top-1)*i, -pi/2)
                elements.append(string)

    if value == 3:

        for i in range(no_stringers_top):
            if i < no_stringers_top-1:
                string = stringer(stringer_height, stringer_thickness, -(dist - 2*t)/2 + (dist - 2*t)/(no_stringers_top-1)*i, front_spar_h/2 - t - ((front_spar_h - rear_spar_h)/2)/(no_stringers_top-1)*i, 0)
                elements.append(string)
            else:
                string = stringer(stringer_height, stringer_thickness, -(dist - 2*t)/2 + (dist - 2*t)/(no_stringers_top-1)*i, front_spar_h/2 - t - ((front_spar_h - rear_spar_h)/2)/(no_stringers_top-1)*i, -pi/2)
                elements.append(string)

        for i in range(no_stringers_bott):
            if i < no_stringers_bott-1:
                string = stringer(stringer_height, stringer_thickness, -(dist - 2*t)/2 + (dist - 2*t)/(no_stringers_bott-1)*i, -(front_spar_h/2 - t - ((front_spar_h - rear_spar_h)/2)/(no_stringers_bott-1)*i), pi/2)
                elements.append(string)
            else:
                string = stringer(stringer_height, stringer_thickness, -(dist - 2*t)/2 + (dist - 2*t)/(no_stringers_bott-1)*i, -(front_spar_h/2 - t - ((front_spar_h - rear_spar_h)/2)/(no_stringers_bott-1)*i), pi)
                elements.append(string)

    return elements


def centroid(span_position):
    elements = cross_section(cross_section_value, span_position)

    # Centroid calculations, to finish
    areas_dist_x = 0
    areas_dist_y = 0
    areas = 0
    for element in elements:
        areas_dist_x += element.area * element.centroid[0]
        areas_dist_y += element.area * element.centroid[1]
        areas += element.area

    centr_x, centr_y = areas_dist_x/areas, areas_dist_y/areas

    return centr_x, centr_y


def MOI(span_position):
    elements = cross_section(cross_section_value, span_position)
    
    moi_xx = 0
    moi_yy = 0
    moi_xy = 0
    for element in elements:
        moi_xx += element.moi_xx + element.area * (element.centroid[0]-centroid(span_position)[0])**2
        moi_yy += element.moi_yy + element.area * (element.centroid[1]-centroid(span_position)[1])**2
        moi_xy += element.moi_xy + element.area * (element.centroid[0]-centroid(span_position)[0])*(element.centroid[1]-centroid(span_position)[1])
        
    return moi_xx, moi_yy, moi_xy


def plot_cross_section(span_position):

    elements = cross_section(cross_section_value, span_position)
    for element in elements:
        if type(element) == stringer:
            colour = "blue"
        if type(element) == beam:
            colour = "blue"
        plt.plot(element.x_coords, element.y_coords, color = colour)

    centr = centroid(span_position)
    plt.axvline(x=centr[0], lw=1, ls='dashed', color = "black")
    plt.axhline(y=centr[1], lw=1, ls='dashed', color = "black")
    plt.title(label = "Cross-section at an x-coordinate of " + str(span_position) + "[m]")

    plt.show()

plot_cross_section(0)

def chord(span_position):
    chord0, chord1 = root_dist/0.4, tip_dist/0.4
    chord = span_position*(chord1-chord0)/b_2 + chord0
    return chord

    
def local_area(span_position):
    # Define cross section
    t, theta, dist, front_spar_h, rear_spar_h, stringer_height, stringer_thickness = initial_values(span_position)
    area = (front_spar_h+rear_spar_h)/2*dist
    return area


def max_distances(span_position):
    centr = centroid(span_position)
    t, theta, dist, front_spar_h, rear_spar_h, stringer_height, stringer_thickness = initial_values(span_position)
    x_max = (front_spar_h/2 + abs(centr[0]))*centr[0]/abs(centr[0])
    y_max = (dist/2 + abs(centr[1]))*centr[1]/abs(centr[1])

    return x_max, y_max

"""
# General values
spar_thickness = 0.03
b_2 = 28.74

# Tip
rear_spar_h_tip = 0.2324
front_spar_h_tip = 0.2534
tip_dist = 0.891

# Root
rear_spar_h_root = 0.8606
front_spar_h_root = 0.9386
root_dist = 3.3

# Calculate dimensions at given span
def dimens(span_position):

    rear_spar_h = span_position*(rear_spar_h_tip-rear_spar_h_root)/b_2 + rear_spar_h_root
    front_spar_h = span_position*(front_spar_h_tip-front_spar_h_root)/b_2 + front_spar_h_root
    dist = span_position*(tip_dist-root_dist)/b_2 + root_dist

    return [rear_spar_h, front_spar_h, dist]

# Centroid
def centroid(span_position):

    rear_spar_h, front_spar_h, dist = dimens(span_position)

    # Calculate centroid
    centr_y = (rear_spar_h*spar_thickness*dist + dist*spar_thickness*dist*0.5*2)/(rear_spar_h*spar_thickness + front_spar_h*spar_thickness + dist*spar_thickness*2)
    centr_z = 0

    return [centr_y, centr_z]


# Moment of inertia
def MOI(span_position):

    rear_spar_h, front_spar_h, dist = dimens(span_position)

    # Calcualte moment of inertia
    I_x = front_spar_h*spar_thickness*(centroid(span_position)[0])**2 + rear_spar_h*spar_thickness*(dist-centroid(span_position)[0])**2 + 2*dist*spar_thickness*(dist/2-centroid(span_position)[0])**2
    I_y = 2*dist*spar_thickness*((front_spar_h-rear_spar_h)/4+0.5*rear_spar_h)**2

    return [I_x,I_y]

# Local cross-sectional area
def local_area(span_position):

    rear_spar_h, front_spar_h, dist = dimens(span_position)

    area = (rear_spar_h+front_spar_h)/2*dist

    return area


print("Centroid location", centroid(0))
print()
print("Moments of inertia", MOI(0))
print("Area", local_area(0))
"""
