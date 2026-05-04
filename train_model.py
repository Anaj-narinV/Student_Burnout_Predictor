import pandas as pd

df = pd.read_csv("/Student_Burnout_Predictor/clean_burnout_data.csv")

df = pd.read_csv("clean_burnout_data.csv")

X = df[['study_hours','sleep_hours','stress_level','screen_time']]
y = df['burnout']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

from sklearn.metrics import classification_report
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# prediction
sample = pd.DataFrame([[8,5,7,6]], 
                      columns=['study_hours','sleep_hours','stress_level','screen_time'])

pred = model.predict(sample)
print("Prediction:", pred[0])

# save model
import pickle
pickle.dump(model, open("/Student_Burnout_Predictor/burnout_model.pkl", "wb"))