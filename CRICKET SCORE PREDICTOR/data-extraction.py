import numpy as np
import pandas as pd
from yaml import safe_load
import os
from tqdm import tqdm

filenames = []
for file in os.listdir('data'):
    filenames.append(os.path.join('data', file))

df_list = []
counter = 1

for file in tqdm(filenames):
    with open(file, 'r') as f:
        df = pd.json_normalize(safe_load(f))
        df['match_id'] = counter
        df_list.append(df)  
        counter += 1

final_df = pd.concat(df_list, ignore_index=True)

print(final_df)
backup = final_df.copy()
print(final_df)