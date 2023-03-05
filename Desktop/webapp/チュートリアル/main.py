import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'start!'

latest_interation=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'

left_colum,right_colum=st.columns(2)
button=left_colum.button('右からむに文字を表示')
if button:
    right_colum.write('ここは右カラム')


expander1=st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2=st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')
expander3=st.expander('問い合わせ')
expander3.write('問い合わせ内容を書く')

