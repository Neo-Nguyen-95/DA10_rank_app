import streamlit as st
import pandas as pd
from business import HLRanking

sample = pd.read_excel('data_sample.xlsx')
hlr = HLRanking(sample)
hlr.get_rank()
hlr.get_stat()

#%% APP
# Title of the app
st.title("Ứng Dụng Xếp Loại Học Lực")
st.markdown("""
            *Lưu ý: chỉ sử dụng để đối chiếu kết quả.*
            """)

st.markdown("""
            Chuẩn bị file tương tự giống như file mẫu bên dưới và 
            upload lên hệ thống.
            """)

sample = pd.read_excel('data_sample.xlsx')
st.write(sample)
 
# Sidebar for user input
st.sidebar.header("Upload Your Excel File")


# File uploader
uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Reading the uploaded file
        data = pd.read_excel(uploaded_file)
        data.iloc[:, 1] = data.iloc[:, 1].astype(str)

        # Displaying the data
        st.subheader("Data của thầy/cô:")
        st.write(data.head())
        
        st.subheader("Kết quả xếp loại học lực:")
        
        hlr = HLRanking(data)
        
        left, buff, right = st.columns([7, 1, 2])
        with left:
            st.dataframe(hlr.get_rank())
        with right:
            st.write(hlr.get_stat())
            
        
        csv_data = hlr.get_rank().to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name='Xep_loai_hoc_luc.csv',
            mime='text/csv',
        )
            
    except:
        pass


