import streamlit as st
import  pandas as pd
data={
    "task":["Extract","Transform","Load"],
    "status":["Complete","Progress","Pending"]
}
df=pd.DataFrame(data)
st.write("ETL STATUS",df)