import pandas as pd
import numpy as np
data = [
    {"Name": "Aminata", "Country": "Finland", "City": "Helsinki"},
    {"Name": "Papa", "Country": "UK", "City": "London"},
    {"Name": "Aisha", "Country": "Sweden", "City": "Stockholm"},
    {"Name": "Shmuunu", "Country": "Ireland", "City": "Dublin"}
]
df = pd.DataFrame(data)
print(df)
