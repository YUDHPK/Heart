from numpy import genfromtxt
from itertools import cycle
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.svm import LinearSVC
from sklearn import model_selection
from sklearn.svm import SVC
import pickle

print()
dataset = genfromtxt('s2data3.csv',dtype = int, delimiter=',')
X=dataset[:,0:-1]
y=dataset[:,-1]
n=len(X) #get the total no. of rows
print("Original Dataset size :",len(X),"x",len(X[0]))
#Method to plot the graph for reduced Dimesions
# def plot_2D(data, target, target_names):
# 	colors = cycle('rgbcmykw')
# 	target_ids = range(len(target_names))
# 	plt.figure()
# 	for i, c, label in zip(target_ids, colors, target_names):
# 		plt.scatter(data[target == i, 0], data[target == i, 1], c=c, label=label)
# 	plt.legend()
# 	#plt.show()
# 	plt.savefig('Reduced_PCA_Graph.png')

#target_names = ['0','1','2','3','4']
#Replacing 0-2 by 0 label and 3-4 by 1 label
for index, item in enumerate(y):
	if item <3:
		y[index] = 0
	else:
		y[index] = 1
#print y
target_names = ['0', '1']

pca = PCA(n_components=8, whiten=True).fit(X)#6
X_new = pca.transform(X)
print("Dataset size after PCA :",len(X_new),"x",len(X_new[0]))
# plot_2D(X_new, y, target_names)

print()
# Classifying the data using a Linear SVM and predicting the probability of disease belonging to a particular class
#Raw no split
modelSVMRaw = LinearSVC(C=0.001)
modelSVMRaw = modelSVMRaw.fit(X_new, y)
print("LinearSVC (without split)",end=" : ")
print(modelSVMRaw.score(X_new,y)*100,"%")

# splitting data into training and testing parts
modelSVM=LinearSVC(C=0.001)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_new, y, test_size=0.35, train_size=0.65,random_state=1)
modelSVM = modelSVM.fit(X_train, y_train)
#Applying cross validation on the training and test set for validating our Linear SVM Model
print("Training accuracy Linear SVM (Split)",end=" : ")
print(modelSVM.score(X_train, y_train)*100 , "%")
print("Testing accuracy Linear SVM (Split)",end=" : ")
print(modelSVM.score(X_test, y_test)*100 , "%" )	#returns the mean accuracy on the given test data and labels


print()
# Classifying the data using a SVM using RBF kernel and predicting the probability of disease belonging to a particular class
#Raw no split
modelSVMRaw1 = SVC(C=0.001,kernel="rbf")
modelSVMRaw1 = modelSVMRaw1.fit(X_new, y)
print("SVM RBF (without split)",end=" : ")
print(modelSVMRaw1.score(X_new,y)*100,"%")

# splitting data into training and testing parts
modelSVM1=SVC(C=0.001,kernel="rbf")
X_train1, X_test1, y_train1, y_test1 = model_selection.train_test_split(X_new, y, test_size=0.35, train_size=0.65,random_state=1)
modelSVM1 = modelSVM1.fit(X_train1, y_train1)
#Applying cross validation on the training and test set for validating our SVM Model using RBF kernel
print("Training accuracy SVM RBF (Split)",end=" : ")
print(modelSVM1.score(X_train1, y_train1)*100 , "%")
print("Testing accuracy SVM RBF (Split)",end=" : ")
print(modelSVM1.score(X_test1, y_test1)*100 , "%" )	#returns the mean accuracy on the given test data and labels

print()
#Using Stratified K Fold #divide into n splits and train and test in batches
skf = model_selection.StratifiedKFold(n_splits=4)					
for train_index, test_index in skf.split(X_new, y, groups=None):
   # print("TRAIN:", train_index, "TEST:", test_index)
	X_train2, X_test2 = X[train_index], X[test_index]
	y_train2, y_test2 = y[train_index], y[test_index]
modelSVM2=SVC(C=0.001,kernel="sigmoid")
modelSVM2=modelSVM2.fit(X_train2,y_train2)

#Applying cross validation on the training and test set for validating our SVM Model using 3rd degree polynomial kernel
print("Training accuracy SVM sigmoid kernel (Split)",end=" : ")
print(modelSVM2.score(X_train2, y_train2)*100 , "%")
print("Testing accuracy SVM sigmoid kernel (Split)",end=" : ")
print(modelSVM2.score(X_test2, y_test2)*100 , "%" )	#returns the mean accuracy on the given test data and labels

#filename = 'finalized_model_sigmoid.sav'
#pickle.dump(modelSVM2, open(filename, 'wb'))

print()