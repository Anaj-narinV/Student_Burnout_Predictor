import pandas as pd
import numpy as np
import random

rows = 1500
data = []

for _ in range(rows):
    study_hours = random.choice([random.randint(2, 12), None, "ten", "8hrs"])
    sleep_hours = random.choice([random.randint(3, 9), None, "six", "7h"])
    stress_level = random.choice([random.randint(1, 10), None, "high", "low"])
    screen_time = random.choice([random.randint(1, 10), None, "5hrs", "two"])
    
    burnout = random.choice(["High", "Medium", "Low", None, "HIGH", "low"])

    data.append([study_hours, sleep_hours, stress_level, screen_time, burnout])

df = pd.DataFrame(data, columns=[
    "study_hours", "sleep_hours", "stress_level", "screen_time", "burnout"
])

df.to_csv("raw_burnout_data.csv", index=False)

print("Raw dataset created!")