from sklearn.preprocessing import OrdinalEncoder, StandardScaler
import pandas as pd

def preprocess_data(df):
    # Xử lý categorical data
    categorical_cols = df.select_dtypes(include=['object']).columns.to_list()
    ordinal_encoder = OrdinalEncoder()
    encoded_categorical_cols = ordinal_encoder.fit_transform(
        df[categorical_cols])

    encoded_categorical_df = pd.DataFrame(
        encoded_categorical_cols, columns=categorical_cols)
    numerical_df = df.drop(categorical_cols, axis=1)
    encoded_df = pd.concat([numerical_df, encoded_categorical_df], axis=1)

    # Chuẩn hóa dữ liệu
    normalizer = StandardScaler()
    dataset_arr = normalizer.fit_transform(encoded_df)

    # Tách X và y
    X, y = dataset_arr[:, 1:], dataset_arr[:, 0]
    return X, y
