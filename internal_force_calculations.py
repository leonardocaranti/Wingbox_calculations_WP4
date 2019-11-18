# Required input: one list of internal forces and one list of their respective x-positions
# Given output: a list with four lists inside, the respective x-positions of the evaluated forces, shear forces,
# axial loads and the internal moments at the given x positions.

half_span = 28.74

def int_load(force_list, pos_list):

    def root_moment():
        bend_mom = 0
        for i in range(len(force_list)):
            bend_mom += force_list[i]*pos_list[i]
        return bend_mom

    def bending_moment(span_position):
        bend_mom = root_moment()
        for i in range(len(force_list)):
            if span_position >= pos_list[i]:
                bend_mom += force_list[i]*(span_position - pos_list[i])
            else:
                return bend_mom

    def shear_load(span_position):
        sh_load = 0
        for i in range(len(force_list)):
            if span_position >= pos_list[i] and pos_list[i] < 30:
                sh_load += force_list[i]
            else: return sh_load

    for i in range(len(pos_list)):
        pos_list[i], force_list[i] = float(pos_list[i]), float(force_list[i])
        if pos_list[i] > half_span:
            pos_list.pop(i)
            force_list.pop(i)

    tot_load = sum(force_list)
    force_list[0] = -tot_load

    sh_load, bend_mom = [],[]
    for i in range(len(force_list)):
        sh_load.append(shear_load(pos_list[i]))
        bend_mom.append(bending_moment(pos_list[i]))
        
    sh_load[-1], bend_mom[-1] = 0, 0

    return [pos_list], [sh_load], [bend_mom]
