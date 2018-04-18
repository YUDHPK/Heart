# Classification  of heart  disease by labeling the predicted values
# in various classes, namely 0 for absence and 1 to 4 for presence and also try  
# to check the model performance by comparing it against other Classifiers

from numpy import genfromtxt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle
from sklearn import model_selection
from sklearn.svm import SVC
																																																																									 
#Loading and pruning the data
dataset = genfromtxt('data4.csv',dtype = int, delimiter=',')
#print(dataset)
X = dataset[:,0:11]  #Feature Set
y = dataset[:,12]   #Label Set
no_of_rows=11111
#Method to plot the graph for reduced Dimesions
def plot_2D(data, target, target_names):
	 colors = cycle('rgbcmykw')
	 target_ids = range(len(target_names))
	 plt.figure()
	 for i, c, label in zip(target_ids, colors, target_names):
		 plt.scatter(data[target == i, 0], data[target == i, 1], c=c, label=label)
	 plt.legend()
	# plt.savefig('Reduced_PCA_Graph')

# Classifying the data using a Linear SVM and predicting the probability of disease belonging to a particular class
modelSVM = LinearSVC(C=0.001)
pca = PCA(n_components=5, whiten=True).fit(X)#6
X_new = pca.transform(X)

# calling plot_2D
target_names = ['0','1','2','3','4']
plot_2D(X_new, y, target_names)

#Applying cross validation on the training and test set for validating our Linear SVM Model
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_new, y, test_size=0.4, train_size=0.6)
modelSVM = modelSVM.fit(X_train, y_train)
print("Testing Linear SVC values using Split")
print(modelSVM.score(X_test, y_test)*100 , "%" )	#returns the mean accuracy on the given test data and labels

# prediction score based on X_new
modelSVMRaw = LinearSVC(C=0.001)
modelSVMRaw = modelSVMRaw.fit(X_new, y)
cnt = 0
for i in modelSVMRaw.predict(X_new):			#performs classification on X_new
	if i == y[i]:
	   cnt = cnt+1
#print "Score without any split"
#print float(cnt)/no_of_rows*100 , "%"


#Applying the Principal Component Analysis on the data features
modelSVM2 = SVC(C=0.001,kernel='rbf')
#Applying cross validation on the training and test set for validating our non Linear SVM Model
X_train1, X_test1, y_train1, y_test1 = model_selection.train_test_split(X_new, y, test_size=0.4, train_size=0.6)
modelSVM2 = modelSVM2.fit(X_train1, y_train1)
print("Testing with RBF using split")
print(modelSVM2.score(X_test1, y_test1)*100 , "%")

modelSVM2Raw = SVC(C=0.001,kernel='rbf')
modelSVM2Raw = modelSVM2Raw.fit(X_new, y)
cnt1 = 0
for i in modelSVM2Raw.predict(X_new):
		if i == y[i]:
		   cnt1 = cnt1+1
#print "RBF Score without split"
#print float(cnt1)/no_of_rows*100 , "%"


#Using Stratified K Fold
skf = model_selection.StratifiedKFold(n_splits=2)					#divide into n splits and train and test in batches
for train_index, test_index in skf.split(X_new, y, groups=None):
   # print("TRAIN:", train_index, "TEST:", test_index)
	X_train3, X_test3 = X[train_index], X[test_index]
	y_train3, y_test3 = y[train_index], y[test_index]
modelSVM3 = SVC(C=0.001,kernel='rbf')
modelSVM3 = modelSVM3.fit(X_train3, y_train3)
print("Testing using stratified with K folds")
print(modelSVM3.score(X_test3, y_test3)*100 , "%")

modelSVM3Raw = SVC(C=0.001,kernel='rbf')
modelSVM3Raw = modelSVM3Raw.fit(X_new, y)
cnt2 = 0
for i in modelSVM3Raw.predict(X_new):
		if i == y[i]:
		   cnt2 = cnt2+1
#print "Stratified K Fold score on X_New"
#print float(cnt2)/no_of_rows*100 , "%"