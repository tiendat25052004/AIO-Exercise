from preprocessing.data_loader import load_data
from preprocessing.data_preprocessing import preprocess_data
from sklearn.model_selection import train_test_split
from models.decision_tree import train_decision_tree
from models.random_forest import train_random_forest
from evaluation.metrics import evaluate_model

# Tải dữ liệu
df = load_data('module_3\week4\data\Housing.csv')

# Xử lý và tách dữ liệu
X, y = preprocess_data(df)
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=1, shuffle=True)

# Huấn luyện và đánh giá Decision Tree
dt_model = train_decision_tree(X_train, y_train)
print("Decision Tree Evaluation:")
evaluate_model(dt_model, X_val, y_val)

# Huấn luyện và đánh giá Random Forest
rf_model = train_random_forest(X_train, y_train)
print("Random Forest Evaluation:")
evaluate_model(rf_model, X_val, y_val)
