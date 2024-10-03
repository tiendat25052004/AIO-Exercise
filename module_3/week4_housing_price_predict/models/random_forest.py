from sklearn.ensemble import RandomForestRegressor


def train_random_forest(X_train, y_train, random_state=1):
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    return model
