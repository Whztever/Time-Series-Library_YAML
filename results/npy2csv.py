import numpy as np
## 设置全部数据，不输出省略号
import sys
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_raw = pd.read_csv("Two_stage_processed_Elia_data_original_for_prediction.csv")
df_data = df_raw["OT"].values
print(np.mean(df_data))
print(np.std(df_data))
df_data = df_data.reshape(len(df_data), 1)
scaler.fit(df_data)

np.set_printoptions(threshold=sys.maxsize)
path = './Transformer-orin/'
print('Target:' + path)
# path处填入npy文件具体路径
print(np.load(path + "pred.npy")[1])
pred = scaler.inverse_transform(np.load(path + "pred.npy")[1])
true = scaler.inverse_transform(np.load(path + "true.npy")[1])
print(pred)
print(true)
# 将npy文件的数据格式转化为csv格式
pred_to_csv = pd.DataFrame(data=pred)
true_to_csv = pd.DataFrame(data=true)
result = pred_to_csv.join(true_to_csv,lsuffix='_pred', rsuffix='_true',how='inner')
# 存入具体目录下的np_to_csv.csv 文件
result.to_csv(path + 'pred_1:10.csv')
