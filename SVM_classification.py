import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
df = pd.read_csv("screen_time.csv")

# Encode categorical variables
label_encoders = {}
categorical_columns = ['Gender', 'Screen Time Type', 'Day Type']
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Convert continuous target variable into categories (Classification Task)
df['Screen Time Category'] = pd.qcut(df['Average Screen Time (hours)'], q=3, labels=['Low', 'Medium', 'High'])

# Features and target
X = df[['Age', 'Gender', 'Screen Time Type', 'Day Type', 'Sample Size']]
y = df['Screen Time Category']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train SVM Classifier
svm_clf = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_clf.fit(X_train, y_train)

# Predictions
y_pred = svm_clf.predict(X_test)

# Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Streamlit Web App
st.title("SVM Classification for Screen Time Prediction")
st.write(f"**Accuracy:** {accuracy:.2f}")

# Display Confusion Matrix
st.subheader("Confusion Matrix")
fig1, ax1 = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Low', 'Medium', 'High'], yticklabels=['Low', 'Medium', 'High'])
ax1.set_xlabel("Predicted Label")
ax1.set_ylabel("True Label")
st.pyplot(fig1)

# Display Classification Report
st.subheader("Classification Report")
st.text(class_report)

# Visualize Distribution of Screen Time Categories
st.subheader("Screen Time Category Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(x=df['Screen Time Category'], palette='viridis', ax=ax2)
st.pyplot(fig2)

