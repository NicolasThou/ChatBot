import numpy as np
import copy as cp

data = np.load('../data/dataset.npz')
X = data['X']
Y = data['Y']

#Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

#Model Random Forest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
classifier.fit(X_train, Y_train)

#Prediction
Y_predict = classifier.predict(X_test)

#Confusion Matrix
from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(Y_test, Y_predict)
#print(matrix)


#k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier, X = X_train, y = Y_train, cv = 10)
#print(accuracies)
#print(accuracies.mean())
#print(accuracies.std())


data.close()

def predictToString(number):
    """
    Return the string of the corresponding cockpit
    """
    if number == 1:
        return 'Light VFR'
    elif number == 0:
        return 'Light IFR'
    elif number == 2:
        return 'Medium and Heavy'

def predict(list):
    """
    predict the parameter which is a list
    Argument :
    =========
    list of features for the input of classfier

    Return :
    =======
    return the NUMBER output which is the prediction classification
    """
    list = np.array([list])
    a = classifier.predict(list)
    return a[0]


if __name__ == "__main__":
    liste_test = [4,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0]
    liste = [4,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0]
    #print(len(liste_test))
    number = predict(liste)
    #print(predictToString(number))