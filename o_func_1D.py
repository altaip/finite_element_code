import csv
import numpy as np
from S_1D import *



'''    
e_exx = data[:][1]
e_exy = data[:][2]
e_eyy = data[:][3]
e_sx = data[:][4]
e_sy = data[:][5]
'''

# Data should be in columns of time, exx,exy,eyy,sx,sy

def objective_function(x):
    # import stuff
    with open('data_s1_1.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        e_exx = []
        e_eyy = []
        e_sx = []
        e_sy = []
        for row in readCSV:
            x_strain = float(row[1])
            #y_strain = float(row[2])
            x_stress = float(row[2])
            #y_stress = float(row[4])
            e_exx.append(x_strain)
            #e_eyy.append(y_strain)
            e_sx.append(x_stress)
            #e_sy.append(y_stress)

        e_exx = np.array(e_exx)
        #e_eyy = np.array(e_eyy)
        e_sx = np.array(e_sx)
        #e_sy = np.array(e_sy)

        # Fitted constants


        mu = x[0]
        lamb = x[1]
        vf = x[2]
        alf1f = x[3]
        k1f = x[4]
        mf = x[5]

        '''
        vy = x[7]
        alf1f = x[8]
        k1f = x[9]
        mf=x[11]
        '''

        # getting stretch from strain
        stretch1 = np.add(np.array(e_exx),np.ones(np.size(e_exx)))
        # stretch2 = np.add(np.array(e_eyy),np.ones(np.size(e_eyy)))
        sx = np.array(e_sx) * stretch1
        # sy = np.array(e_sy) * stretch2 / stretch1
        sx_calc = np.zeros(np.size(stretch1))
        # sy_calc = np.zeros(np.size(stretch1))

        # actual math
        for i in range(len(stretch1)):
            sobj = S(stretch1[i])
            sx_calc[i] = sobj.S(mu, lamb, vf, alf1f, k1f, mf)
            # sy_calc[i] = sobj.S(vm, mu, lamb, alf1m, k1, alf2m, k2, vy, alf1f, k1f, mf11, mf12, mf21, mf22)[1][1]

        # The output of this function is NOT PKstrain. The output is the error between the data and the fitted curve
        resid = sx - sx_calc
        error = np.sqrt(np.matmul(resid.T, resid))

        return error
