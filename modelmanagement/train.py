# Run the following train.py from the notebook to generate a cancer classifier model 
from sklearn.svm import SVC
import pickle

# indicator1, NF1, cellprofiling
X = [[362, 160, 88], [354, 140, 86], [320, 120, 76], [308, 108, 47], [332, 130, 80], [380, 180, 94], [350, 128, 78],
     [354, 140, 80], [318, 110, 74], [342, 150, 84], [362, 170, 86]]

Y = ['positive', 'positive', 'negative', 'negative', 'positive', 'positive', 'negative', 'negative', 'negative', 'positive', 'positive']

clf = SVC()
clf = clf.fit(X, Y)

print('Predicted value:', clf.predict([[380, 140, 86]]))
print('Accuracy', clf.score(X,Y))

print('Export the model to output/trainedModel.pkl')
f = open('output/trainedModel.pkl', 'wb')
pickle.dump(clf, f)
f.close()

print('Import the model from output/trainedModel.pkl')
f2 = open('output/trainedModel.pkl', 'rb')
clf2 = pickle.load(f2)

X_new = [[308, 108, 70]]
print('New Sample:', X_new)
print('Predicted class:', clf2.predict(X_new))
