from sklearn.datasets import load_boston
boston = load_boston()

X_full, y_full = boston.data, boston.target

#
#
#n_samples = X_full.shape[0]
#print(n_samples)
#
#n_features = X_full.shape[1]
#print(n_features)