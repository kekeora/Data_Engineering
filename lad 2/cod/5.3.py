import pandas as pd
import json
import os
import msgpack

data = pd.read_csv("E:/pythonProject/lad 2/data/economy.csv", low_memory=False)

selected_columns = ['match_id', 'event_id', 'team_1', 'team_2', 'best_of', '_map', '1_t1']
data_subset = data[selected_columns]

data_subset.loc[:, 'match_id'] = pd.to_numeric(data_subset['match_id'], errors='coerce')
data_subset.loc[:, 'event_id'] = pd.to_numeric(data_subset['event_id'], errors='coerce')
data_subset.loc[:, 'best_of'] = pd.to_numeric(data_subset['best_of'], errors='coerce')

data_subset = data_subset.dropna(subset=['match_id', 'event_id', 'best_of'])


numeric_columns = ['match_id', 'event_id', 'best_of']

numeric_stats = {
    'max': data_subset[numeric_columns].max().to_dict(),
    'min': data_subset[numeric_columns].min().to_dict(),
    'mean': data_subset[numeric_columns].mean().to_dict(),
    'sum': data_subset[numeric_columns].sum().to_dict(),
    'std': data_subset[numeric_columns].std().to_dict(),
}


categorical_columns = ['team_1', 'team_2', '_map']
categorical_freq = {}
for col in categorical_columns:
    categorical_freq[col] = data_subset[col].value_counts().to_dict()


results = {
    'numeric_stats': numeric_stats,
    'categorical_freq': categorical_freq
}

with open("E:/pythonProject/lad 2/result/analysis_results.json", "w", encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)


data_subset.to_csv("E:/pythonProject/lad 2/result/data_subset.csv", index=False)
data_subset.to_json("E:/pythonProject/lad 2/result/data_subset.json", orient='records', lines=True)
data_subset.to_pickle("E:/pythonProject/lad 2/result/data_subset.pkl")


with open("E:/pythonProject/lad 2/result/data_subset.msgpack", "wb") as msgpack_file:
    msgpack.pack(data_subset.to_dict(orient='records'), msgpack_file)


file_sizes = {
    'csv': os.path.getsize("E:/pythonProject/lad 2/result/data_subset.csv"),
    'json': os.path.getsize("E:/pythonProject/lad 2/result/data_subset.json"),
    'pkl': os.path.getsize("E:/pythonProject/lad 2/result/data_subset.pkl"),
    'msgpack': os.path.getsize("E:/pythonProject/lad 2/result/data_subset.msgpack"),
}

print("Размеры файлов:")
for format, size in file_sizes.items():
    print(f"{format.upper()}: {size / (1024 * 1024):.2f} MB")