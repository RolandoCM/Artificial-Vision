# coding=utf-8
import itertools
from sklearn.metrics import confusion_matrix
from pandas_ml import ConfusionMatrix
from matplotlib import pyplot as plt
import numpy as np


def cnf_matrix( prediction, d_true):
    predictions = prediction
    Y = d_true
    matrix = open('matrix.txt','a')
    archive = raw_input('archivo .csv de frecuencias: ')
    len_des = np.loadtxt('descriptors/'+archive+'.csv') # corregir es variable archivo
    x = len_des[:]
    test_pred = np.array([])
    test_true = np.array([])
    tam = 0
    for i in x:
        test_pred = predictions[tam:tam+int(i)]
        test_true = d_true[tam:tam+int(i)]
        Agrupar(test_true, test_pred)
        tam += int(i)

    Agrupar(predictions, Y)
    # print s_pred
    # print s_true
    cm = ConfusionMatrix(s_true, s_pred)
    cm.print_stats()
    class_names = ["Nutella","Coffee-Mate", "Svetia", "Desodorante", "Desodorante-Spray", "Coffee"]
    cnf_matrix=confusion_matrix(s_true, s_pred)


    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=class_names, title='Confusion Matrix')
    plt.show()

def Agrupar(test_true, test_pred):
    act = []
    pre = []
    for i in test_pred:
        if i[0] == max(i):
            pre.append("0") # nutella
        elif i[1] == max(i):
            pre.append("1")# coffeemate
        elif i[2] == max(i):
            pre.append("2")#svetia
        elif i[3] == max(i):
            pre.append("3")#desodorante
        elif i[4] == max(i):
            pre.append("4")#desodorantespray
        elif i[5] == max(i):
            pre.append("5")#coffee
        else:
            pre.append("6")#ninguno
            print i
    for i in test_true:
        if i[0] == max(i):
            act.append("0")#nutella
        elif i[1] == max(i):
            act.append("1")#coffeemate
        elif i[2] == max(i):
            act.append("2")#svetia
        elif i[3] == max(i):
            act.append("3")#desodorante
        elif i[4] == max(i):
            act.append("4")#desodorantespray
        elif i[5] == max(i):
            act.append("5")#coffee
        else:
            act.append("6")#ninguno
    frecuencias_pred = []
    frecuencias_true = []
    for i in range(0,7):
            frecuencias_pred.append(pre.count(str(i)))
            frecuencias_true.append(act.count(str(i)))

    s_true.append(frecuencias_true.index(max(frecuencias_true)))
    s_pred.append(frecuencias_pred.index(max(frecuencias_pred)))
    # print len(pre)
    # print max(frecuencias_pred)

    # print frecuencias_pred

    #print predictions
    #print Y




def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Real Objects')
    plt.xlabel('Predicted Objects')

s_true = []
s_pred = []
act = []
pre = []