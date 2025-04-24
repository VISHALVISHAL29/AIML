import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("screen_time.csv")

# Encode categorical variables
label_encoders = {}
categorical_columns = ['Gender', 'Screen Time Type', 'Day Type']
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and target
X = df[['Age', 'Gender', 'Screen Time Type', 'Day Type', 'Sample Size']]
y = df['Average Screen Time (hours)']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train KNN Regressor
k = 5
knn_regressor = KNeighborsRegressor(n_neighbors=k)
knn_regressor.fit(X_train, y_train)

# Predictions
y_pred = knn_regressor.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Streamlit Web App
st.title("KNN Regression for Screen Time Prediction")
st.write(f"Mean Squared Error: {mse}")
st.write(f"R-squared Score: {r2}")

# Scatter Plot
st.subheader("Actual vs Predicted Screen Time")
fig1, ax1 = plt.subplots()
sns.scatterplot(x=y_test, y=y_pred, ax=ax1)
ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
ax1.set_xlabel("Actual Screen Time (hours)")
ax1.set_ylabel("Predicted Screen Time (hours)")
st.pyplot(fig1)

# Residual Distribution
st.subheader("Residual Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(y_test - y_pred, bins=20, kde=True, ax=ax2)
ax2.set_xlabel("Residuals")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# Correlation Matrix
st.subheader("Feature Correlation Matrix")
fig3, ax3 = plt.subplots(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax3)
st.pyplot(fig3)
