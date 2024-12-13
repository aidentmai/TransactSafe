import pandas as pd
from geopy.distance import geodesic
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Preprocessing Function
def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Feature engineering
    df['transaction_time'] = pd.to_datetime(df['trans_date_trans_time'])
    df['trans_hour'] = df['transaction_time'].dt.hour
    df['trans_day'] = df['transaction_time'].dt.weekday
    df['trans_year'] = df['transaction_time'].dt.year
    df['amt_ratio'] = df['amt'] / df.groupby('cc_num')['amt'].transform('mean')
    df['daily_transaction_count'] = df.groupby(['cc_num', 'trans_day'])['trans_num'].transform('count')

    # Drop unnecessary features
    df = df.drop(columns=['Unnamed: 0', 'trans_date_trans_time', 'transaction_time', 'trans_num', 'first', 'last',
                          'gender', 'street', 'zip', 'city_pop', 'job', 'dob', 'unix_time', 'merch_zipcode'])

    # Calculate user distance from merchant
    df['user_location_distance'] = df.apply(
        lambda row: geodesic((row['lat'], row['long']), (row['merch_lat'], row['merch_long'])).miles, axis=1
    )

    return df

# Train-Test Split Function
def split_and_encode(df):
    X = df.drop(columns=['is_fraud'])
    y = df['is_fraud']
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Label Encoding for categorical columns
    categorical_columns = ['merchant', 'category', 'city', 'state']
    label_encoded = {}
    for col in categorical_columns:
        le = LabelEncoder()
        X_train[col] = le.fit_transform(X_train[col])
        X_val[col] = le.transform(X_val[col])
        X_test[col] = le.transform(X_test[col])
        label_encoded[col] = le

    # Normalization
    scaler = StandardScaler()
    numerical_features = ['cc_num', 'amt', 'lat', 'long', 'merch_lat', 'merch_long', 'trans_hour', 'trans_day', 'trans_year', 'amt_ratio', 'daily_transaction_count', 'user_location_distance']
    X_train_numerical = scaler.fit_transform(X_train[numerical_features])
    X_val_numerical = scaler.transform(X_val[numerical_features])
    X_test_numerical = scaler.transform(X_test[numerical_features])

    return X_train, X_val, X_test, y_train, y_val, y_test, label_encoded
