import pickle
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Process 12 integers.')
parser.add_argument('integers', metavar='N', type=int, nargs=12, help='an integer for the accumulator')
args = parser.parse_args()
#print(args.integers)

#X=np.array([39,0,2.0,105.0,194.0,0.0,2.0,178.0,1.0,1.0,1.0,10])
X=np.array(args.integers)
filename = 'finalized_model3.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print(loaded_model.predict(X.reshape(1,-1))[0])

#python test.py 39 0 2 105 194 0 2 178 1 1 1 10