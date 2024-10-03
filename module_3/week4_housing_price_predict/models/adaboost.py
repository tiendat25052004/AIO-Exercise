from sklearn.ensemble import AdaBoostRegressor


def train_adaboost(X_train, y_train, random_state=1):
    model = AdaBoostRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    return model
