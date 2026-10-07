import pandas as pd

df = pd.read_csv("people.csv")
df = pd.read_csv("people.csv", usecols=["First Name", "Email"])'
df = pd.read_csv("people.csv", na_values=["N/A", "Unknown"])


digits = datasets.load_digits()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(f'X train size: {X_train.shape}')
print(f'X test size: {X_test.shape}')
print(f'y train size: {y_train.shape}')
print(f'y test size: {y_test.shape}')



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

reg = linear_model.LogisticRegression(max_iter=10000, random_state=0)
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

print(f"Logistic Regression model accuracy: {metrics.accuracy_score(y_test, y_pred) * 100:.2f}%")


train_data = pd.read_csv('/kaggle/input/competitions/titanic/train.csv')
train_data.head()