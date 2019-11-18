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

def chord(span_position):
    chord0, chord1 = root_dist/0.4, tip_dist/0.4
    chord = span_position*(chord1-chord0)/b_2 + chord0
    return chord

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


"""
print("Centroid location", centroid(0))
print()
print("Moments of inertia", MOI(0))
print("Area", local_area(0))
"""
