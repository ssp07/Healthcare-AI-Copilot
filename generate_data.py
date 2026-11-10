import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

patients = []

for patient_id in range(1, 101):

    age = random.randint(20,80)

    gender = random.choice([
        "Male",
        "Female"
    ])

    for report in range(5):

        report_date = (
            datetime.today()
            - timedelta(days=report*90)
        ).strftime("%Y-%m-%d")

        patients.append({
            "patient_id": patient_id,
            "report_date": report_date,
            "age": age,
            "gender": gender,
            "glucose": random.randint(70,180),
            "cholesterol": random.randint(130,300),
            "hdl": random.randint(25,80),
            "ldl": random.randint(50,180),
            "blood_pressure": random.randint(90,170),
            "vitamin_d": random.randint(10,60),
            "hemoglobin": round(
                random.uniform(10,18),
                1
            )
        })

df = pd.DataFrame(patients)

df.to_csv(
    "patient_reports.csv",
    index=False
)

reference = pd.DataFrame({
    "metric":[
        "glucose",
        "cholesterol",
        "hdl",
        "ldl",
        "vitamin_d",
        "hemoglobin"
    ],
    "min_normal":[
        70,
        125,
        40,
        0,
        30,
        12
    ],
    "max_normal":[
        100,
        200,
        100,
        100,
        100,
        17
    ]
})

reference.to_csv(
    "medical_reference.csv",
    index=False
)

print("Healthcare datasets created.")