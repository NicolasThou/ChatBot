from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import copy as cp
from sklearn.preprocessing import LabelEncoder

path_VFR = '../data//CSV/Data_Base_VFR.csv'
path_IFR = '../data/CSV/Data_Base_IFR.csv'
path_MH = '../data//CSV/Data_Base_MH.csv'
path = '../data/CSV/Data_Base.csv'



"""=================== Test ==================="""

features_adjustable_test = [0, 1, 2, 3]  #features equal to 0 or 1
n_test = len(features_adjustable_test)


"""=================== VFR ==================="""

features_adjustable1 = [2, 4, 12, 14, 15, 18, 19, 21, 30, 31, 32, 34, 35, 36, 37, 38]  #features equal to 0 or 1
n1 = len(features_adjustable1) #2 puissance 16 donc 65536 possibilité

"""=================== IFR ==================="""

features_adjustable2 = [0, 4, 6, 12, 15, 23, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39]  #features equal to 0 or 1, or for the first item it can be equal to 2 or 3
n2 = len(features_adjustable2) #2 puissance 17 donc 131072 possibilité

"""=================== MH ==================="""

features_adjustable3 = [0, 12, 15, 23, 27, 32, 33, 34, 35, 36, 37, 38, 39]  #features equal to 0 or 1, or for the first item it can be equal to 3 or 4
n3 = len(features_adjustable3) #2 puissance 13 donc 8192 possibilité


def extract_data(path):
    """

    Extract the data from a CSV

    Argument :
    ==========
    path to the csv file

    Return :
    =======

    return the features Matrix X
    return the dependant variable Vector Y

    """

    data = pd.read_csv(path) #titre des colonnes ne sont pas considérées dans la matrice !
    X = data.iloc[:,1:].values
    Y = data.iloc[:,0].values
    return X,Y



X_VFR, Y_VFR = extract_data(path_VFR)
X_train_VFR = []

X_IFR, Y_IFR = extract_data(path_IFR)
X_train_IFR = []

X_MH, Y_MH = extract_data(path_MH)
X_train_MH = []

def binary_test(n, j, row, features_adjustable, categorie):
    """
    Function add all the row in a features matrix X_train, which is a global variable

    Argument:
    =========
    n length of features_adjustable
    j index in features_adjustable, always call the function with j = 0
    row is the list of make_row
    features_adjustable features which can be modify

    Return:
    =======
    No return
    Modify a global variable
    """

    if j == n:
        if categorie == 'VFR':
            print('VFR')
            a = cp.deepcopy(row)
            X_train_VFR.append(a)
            return
        elif categorie == 'IFR':
            #print('IFR')
            a = cp.deepcopy(row)
            X_train_IFR.append(a)
            return
        elif categorie == 'MH':
            #print('MH')
            a = cp.deepcopy(row)
            X_train_MH.append(a)
            return

    i = features_adjustable[j]

    """
    
    if i==0 and categorie =='VFR':
        row[i] = 2
        print('here1')
        binary2(n, j+1, row, features_adjustable, categorie)
        print('here2')
        row[i] = 3
        print('here3')
        binary2(n, j+1, row, features_adjustable, categorie)

    if i==0 and categorie =='MH':
        row[i] = 3
        binary2(n, j+1, row, features_adjustable, categorie)
        row[i] = 4
        binary2(n, j+1, row, features_adjustable, categorie)
    
    """

    print('add row[i] = 0 with i == '+str(i))
    row[i] = 0
    binary2(n, j+1, row, features_adjustable, categorie)
    print('add row[i] = 1 with i == '+str(i))
    row[i] = 1
    binary2(n, j+1, row, features_adjustable, categorie)


def binary2(n, j, row, features_adjustable, categorie):
    """
    Function add all the row in a features matrix X_train, which is a global variable

    Argument:
    =========
    n length of features_adjustable
    j index in features_adjustable, always call the function with j = 0
    row is the list of make_row
    features_adjustable features which can be modify

    Return:
    =======
    No return
    Modify a global variable
    """

    if j == n:
        if categorie == 'VFR':
            #print('VFR')
            a = cp.deepcopy(row)
            X_train_VFR.append(a)
            return
        elif categorie == 'IFR':
            #print('IFR')
            a = cp.deepcopy(row)
            X_train_IFR.append(a)
            return
        elif categorie == 'MH':
            #print('MH')
            a = cp.deepcopy(row)
            X_train_MH.append(a)
            return

    i = features_adjustable[j]
    row[i] = 0
    binary2(n, j+1, row, features_adjustable, categorie)
    row[i] = 1
    binary2(n, j+1, row, features_adjustable, categorie)

def IDU_IFR(a):
    """
    This function look at the list of list a. Then it replace every features of IDU to 2 or 3.
    Argument:
    =========
    a is a list of list, the X_train_IFR list.

    Return:
    =======
    return "a" with every feature of IDU with 2 or 3

    """
    for i in range(len(a)):
        if(a[i][0] == 0):
            a[i][0] = 2
        elif(a[i][0] == 1):
            a[i][0] = 3
    return a


def IDU_MH(a):
    """
    This function look at the list of list a. Then it replace every features of IDU to 3 or 4.
    Argument:
    =========
    a is a list of list, the X_train_VFR list.

    Return:
    =======
    return a with every feature of IDU with 3 or 4

    """
    for i in range(len(a)):
        if (a[i][0] == 0):
            a[i][0] = 3
        elif (a[i][0] == 1):
            a[i][0] = 4
    return a

def make_row(X, features_adjustable):
    """
    Return the first row of the categories of cockpit as a list
    It takes the first ndarray and transform in a list
    It makes every feature adjustable to 0

    Argument:
    =========
    X ndarray of features
    features_adjustable of the right cockpit categorie

    Return:
    =======
    List (the first row)

    """
    row = list(X[0])  # premier individu
    for i in features_adjustable:
        row[i] = 0
    return row

def make_data_test():
    row = list(X_VFR[0])  # premier individu
    for i in range(len(row)):
        row[i] = 0
    print('this is the initial row')
    print(row)
    print('enter the function binary_test')
    binary_test(n_test, 0, row, features_adjustable_test, 'VFR')
    a = cp.deepcopy(X_train_VFR) #we've had every row in X_train_VFR, and the copy to variable a
    a = np.array(a)
    return a

def make_data_VFR():
    row = make_row(X_VFR, features_adjustable1)
    binary2(n1, 0, row, features_adjustable1, 'VFR')
    a = cp.deepcopy(X_train_VFR) #we've had every row in X_train_VFR, and then copy to variable a
    print('number of row for the VFR is equal to ' + str(len(a)))
    return a

def make_data_IFR():
    row = make_row(X_IFR, features_adjustable2)
    binary2(n2, 0, row, features_adjustable2, 'IFR')
    a = cp.deepcopy(X_train_IFR) #we've had every row in X_train_IFR, and then copy to variable a
    print('number of row for the IFR data is equal to ' + str(len(a)))
    a = IDU_IFR(a)
    return a

def make_data_MH():
    row = make_row(X_MH, features_adjustable3)
    binary2(n3, 0, row, features_adjustable3, 'MH')
    a = cp.deepcopy(X_train_MH) #we've had every row in X_train_MH, and then copy to variable a
    print('number of row for the MH is equal to ' + str(len(a)))
    a = IDU_MH(a)
    return a

def make_data_X():
    a = make_data_VFR()
    b = make_data_IFR()
    c = make_data_MH()
    return np.array(a+b+c)



def make_data_Y():
    Y1 = list(Y_VFR)
    Y1 = Y1 * (2 ** 16)
    Y2 = list(Y_IFR)
    Y2 = Y2 * (2 ** 17)
    Y3 = list(Y_MH)
    Y3 = Y3 * (2 ** 13)
    return np.array(Y1+Y2+Y3)

def categorical_data(Y):
    """
    Encoding categorical data with sklearn
    Argument:
    ========
    Y vector with categorical data
    Return:
    =======
    return the Y transformed vector
    """
    labelencoder_y = LabelEncoder()
    Y = labelencoder_y.fit_transform(Y)
    return Y

Y_data = make_data_Y()
Y_data = categorical_data(Y_data)
X_data = make_data_X()
np.savez('../data/dataset', X=X_data, Y=Y_data) #On sauvegarde les résultats afin de ne pas faire tourner l'algorithme à chaque fois


if __name__ == "__main__":
    #print(X_data)
    print('Hello World')







