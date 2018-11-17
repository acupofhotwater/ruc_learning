# classified data
from sklearn import datasets
digits = datasets.load_digits()
print("input shape", digits.data.shape)     #input shape
print("output shape", digits.target.shape)   #output shape

# feature_extraction

# train valid test
from sklearn.model_selection import train_test_split
Xtrain, x_test, Ytrain, y_test = train_test_split(digits.data,
                                        digits.target,
                                        test_size = 0.2,
                                        random_state = 33) # 
x_train, x_valid, y_train, y_valid = train_test_split(Xtrain,
                                        Ytrain,
                                        test_size = 0.2,
                                        random_state = 33)


# grid search
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, make_scorer
from sklearn.model_selection import GridSearchCV


# Define the model (with default hyperparameters)
clf = DecisionTreeClassifier(random_state=42)

# Fit the model
clf.fit(x_train, y_train)

# Make predictions using the unoptimized and model
train_predictions = clf.predict(x_train)
valid_predictions = clf.predict(x_valid)

print("The training F1 Score is", f1_score(y_train, train_predictions, average='micro') ) 
print("The validing F1 Score is", f1_score(y_valid, valid_predictions, average='micro') )


# grid
clf = DecisionTreeClassifier(random_state=42)

# TODO: Create the parameters list you wish to tune.
parameters = {'max_depth':[2,4,6,8,10],'min_samples_leaf':[2,4,6,8,10], 'min_samples_split':[2,4,6,8,10]}

# TODO: Make an fbeta_score scoring object.
scorer = make_scorer(f1_score, average='micro')

# TODO: Perform grid search on the classifier using 'scorer' as the scoring method.
grid_obj = GridSearchCV(clf, parameters, scoring=scorer)

# TODO: Fit the grid search object to the training data and find the optimal parameters.
grid_fit = grid_obj.fit(x_train, y_train)

# Get the estimator.
best_clf = grid_fit.best_estimator_
print(best_clf.best_params_)
# Fit the new model.
best_clf.fit(x_train, y_train)

# Make predictions using the new model.
best_train_predictions = best_clf.predict(x_train)
best_valid_predictions = best_clf.predict(x_valid)

# Calculate the f1_score of the new model.
print('The best clf training F1 Score is', f1_score(y_train, best_train_predictions, average='micro'))
print('The best clf validing F1 Score is', f1_score(y_valid, best_valid_predictions, average='micro'))