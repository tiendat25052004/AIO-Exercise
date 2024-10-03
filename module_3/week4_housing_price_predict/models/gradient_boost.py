from sklearn.ensemble import GradientBoostingRegressor


def train_gradient_boost(X_train, y_train, random_state=1):
    model = GradientBoostingRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    return model
