# Required input: one list of internal forces and one list of their respective x-positions
# Given output: a list with four lists inside, the respective x-positions of the evaluated forces, shear forces,
# axial loads and the internal moments at the given x positions.

def int_load(force_list, pos_list):

    def bending_moment(span_position):
        bend_mom = 0
        for i in range(len(force_list)):
            if pos_list[i] < span_position:
                bend_mom += force_list[i]*pos_list[i]
            else: return bend_mom

    def axial_load(span_position):
        ax_load = 0
        for i in range(len(force_list)):
            if pos_list[i] < span_position:
                ax_load += force_list[i]
            else: return ax_load

    def shear_load(span_position):
        sh_load = 0
        for i in range(len(force_list)):
            if pos_list[i] < span_position:
                sh_load += force_list[i]
            else: return sh_load

    sh_load, ax_load, bend_mom = [], [], []
    for i in range(len(force_list)):
        sh_load.append(shear_load(pos_list[i]))
        ax_load.append(axial_load(pos_list[i]))
        bend_mom.append(bending_moment(pos_list[i]))

    return [[pos_list],
            [sh_load],
            [bend_mom],
            [ax_load]]