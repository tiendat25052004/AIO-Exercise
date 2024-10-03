from sklearn.tree import DecisionTreeRegressor


def train_decision_tree(X_train, y_train, random_state=1):
    model = DecisionTreeRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    return model
