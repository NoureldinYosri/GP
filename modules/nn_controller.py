#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:25:20 2017

@author: noureldin
"""

#import tensorflow as tf
import cv2,time,sys
from os import walk
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import sys,random
import matplotlib.pylab as plt

sys.path.insert(0, '../')
import SOM,utils
from logger import *

def assign_vals(labels):
    label_val = {}
    cur = 0
    for label in labels:
        label_val[label] = cur
        cur += 1
    return label_val

def read_data(path):
    """returns path X,Y of data where X[i] is an image and Y[i] is its label"""
    data = {}
    val = {"no":-1,"undetermined":0,"yes":1}
    print ("started reading data")
    start_time = time.time()
    labels = []
    for (dirpath, dirnames, filenames) in walk(path):
        labels.extend(dirnames)
        break
    label_val = assign_vals(labels)
    for (dirpath, dirnames, filenames) in walk(path):
        	label = utils.get_dirname(dirpath)
        	if label not in label_val: 
        		continue
        	data[label] = filenames
    X = []
    Y = []
    for label in data:
        for img_name in data[label]:
            path_to_img = utils.join_list([path, label, img_name])
            X.append(cv2.imread(path_to_img,0))
            Y.append(label_val[label])
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished reading data in %d min and %d seconds"%(minutes,seconds))
    X = np.array(X)
    Y = np.array(Y)
    return X,Y

def transform_data(imgs,labels,som,m,n):
    data = zip(imgs, labels)
    res_imgs = []
    res_labels = []
    surf = cv2.xfeatures2d.SURF_create(10000)
    print ("started transforming data")
    cnt = 0
    start_time = time.time()
    for img, label in data:
        kp, des = surf.detectAndCompute(img,None)
        if des is None: continue
        compressed = [0 for i in range(m*n)]
        for feature_description in des:
            cnt += 1
            activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64))
            for match in som.get_bmus(activation_map):
                compressed[match[0]*n + match[1]] += 1
        res_imgs.append(np.array(compressed,dtype = np.float32))
        res_labels.append(label)

    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished transforming %d features in %d min and %d seconds"%(cnt,minutes,seconds))
    return res_imgs, res_labels

def get_som(path,som_m,som_n,surf,mylogger):
    som = SOM.train(path,som_m,som_n,surf)
    mylogger.save(som, Log.SOM.value)
    return som

def get_clf(X,Y,hidden_layer_shape,mylogger):
    print ("start training MLP")
    start_time = time.time()
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=tuple(hidden_layer_shape), random_state=1)
    clf.fit(X,Y)
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished learning in %d min and %d seconds"%(minutes,seconds))
    mylogger.save(clf, Log.CLF.value)
    return clf    
   

def split(X,Y,testSize = 0.3):
    X_train, X_test, Y_train, Y_test =  \
									train_test_split(X, Y, test_size=0.3, random_state=42,stratify = Y)
    X_train = np.array(X_train,dtype = np.float32)
    X_test = np.array(X_test,dtype = np.float32)
    Y_train = np.array(Y_train,dtype = np.float32)
    Y_test = np.array(Y_test,dtype = np.float32)
    return X_train,Y_train,X_test,Y_test


def conduct_experiment(path,som_shape,hidden_layer_shape,surf_threshold,module_name):
    mylogger = logger(utils.join_parent('logger', 2),'working on %s with MLP and SOM is %s and %s hidden layer'%(module_name,str(som_shape),str(hidden_layer_shape)))
    X,Y = read_data(path)
    surf = cv2.xfeatures2d.SURF_create(surf_threshold)
    som = get_som(path,surf,som_shape[0],som_shape[1],mylogger)
    X,Y = transform_data(X,Y,som,som_shape[0],som_shape[1])
    mylogger.save(X, Log.IMGS.value)
    mylogger.save(Y, Log.LABELS.value)
    X_train,Y_train,X_test,Y_test = split(X,Y)
    clf = get_clf(X_train,Y_train,hidden_layer_shape,mylogger)
    train_acc = accuracy_score(Y_train, clf.predict(X_train))*100
    Y_predict = clf.predict(X_test)
    test_acc = accuracy_score(Y_test, Y_predict)*100
    baseline_acc = sum(Y_test == 1)*100.0/len(Y_test)
    print (Y_test[:10],Y_predict[:10])
    print ("training accuracy is %.10f, test accuracy is %.10f, baseline_acc is %.10f"%(train_acc,test_acc,baseline_acc))
    plt.hist(np.array(clf.predict(X_test)))
    plt.savefig('histogram.png')
    plt.show()
    error_matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            error_matrix[i][j] = sum(np.array(Y_test==(i-1)) * np.array(Y_predict==(j-1)))
    print (error_matrix)
    mylogger.save(clf,'MLP model training accuracy is %.10f, test accuracy is %.10f, baseline_acc is %.10f'%(train_acc,test_acc,baseline_acc) + "\n error matrix contains " + str(error_matrix) )    

    
if __name__ == "__main__":
    path = utils.join_parent("goal", 2)
    conduct_experiment(path,[20,20],[5,5],4000,"goal")