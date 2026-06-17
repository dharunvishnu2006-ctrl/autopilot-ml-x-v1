import pandas as pd
from src.profiler import profile

df = pd.read_csv("data/sample_orders.csv")
report = profile(df)
print(report)