import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('우리의 첫 앱이에요')

st.write('나는 이호준입니다')

st.button('hi')

data = np.linspace(1,100,1000)**2

df = pd.DataFrame()
df['data']=data
df['name']=[f'dot{i}' for i in range(data.shape[0])]

st.dataframe(df)
fig, ax = plt.subplots()
ax.plot(data)
st.pyplot