import pandas as pd
import numpy as np

df = pd.read_csv("/Student_Burnout_Predictor/raw_burnout_data.csv")

print(df.head())

def clean_hours(x):
    try:
        return float(str(x).replace("hrs", "").replace("h", ""))
    except:
        return np.nan

df['study_hours'] = df['study_hours'].apply(clean_hours)
df['sleep_hours'] = df['sleep_hours'].apply(clean_hours)
df['screen_time'] = df['screen_time'].apply(clean_hours)

def clean_stress(x):
    if str(x).lower() == "high":
        return 9
    elif str(x).lower() == "low":
        return 3
    else:
        try:
            return float(x)
        except:
            return np.nan

df['stress_level'] = df['stress_level'].apply(clean_stress)

df = df.dropna()

print(df.info())
print(df.head())

df.to_csv("clean_burnout_data.csv", index=False)

