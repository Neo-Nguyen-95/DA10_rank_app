import streamlit as st
import pandas as pd
from business import HLRanking

#%% I. Introduction & Usage
st.title("Ứng Dụng Đánh Giá Kết Quả Học Tập Theo Thông Tư 22/2021/TT-BGDĐT")
st.write("Ứng dụng hỗ trợ các thầy cô đánh giá kết quả học tập của học sinh một cách \
nhanh chóng và hiệu quả.")

st.sidebar.markdown("""
                    ### Cách sử dụng:
                        
                    - Sử dụng app để xuất file đánh giá kết quả
                        
                    - Tự kiểm tra lại tính chính xác
                    
                    ### Nguyên lí đánh giá kết quả học tập (KQHT):
                        
                    - Tốt: Tất cả các môn có ĐTB ≥ 6,5, ít nhất 06 môn có ĐTB ≥ 8,0.
                    
                    - Khá: Tất cả các môn có ĐTB ≥ 5,0, ít nhất 06 môn có ĐTB ≥ 6,5.
                    
                    - Đạt: Tất cả các môn có ĐTB ≥ 3,5, ít nhất 06 môn có ĐTB ≥ 5,0.
                    
                    - Chưa Đạt: còn lại.
                    
                    ### Nguyên lí xét danh hiệu:
                    
                    - Học sinh giỏi: KQHT loại Tốt.
                    
                    - Học sinh xuất sắc: KQHT loại Tốt & 6 môn có ĐTB ≥ 9,0.
                    
                    - Còn lại không xét danh hiệu khen thưởng.
                    """)

st.markdown("""            
            ### I. Chuẩn bị
            Chuẩn bị file tương tự giống như file mẫu bên dưới và 
            upload lên hệ thống.
            
            Các cột cần có là:
                
            |STT | Mã định danh | Họ và tên | (Ngày sinh) | (Giới tính) | Môn học x 8|
            |- | - | - | - | - | - |
            |... | ... | ... | ... | ... | ... |
            |*Cần* | *Để trống nếu không có* | *Cần* | *Có hoặc không* | *Có hoặc không* | *Đủ 8 môn* |

            
            Dưới đây là file mẫu, thầy cô có thể tham khảo.
            """)

sample = pd.read_excel('data_sample.xlsx')
st.dataframe(sample)

#%% II. Upload File 
st.markdown("""
            ### II. Tải file
            """)


# File uploader
uploaded_file = st.file_uploader("Chọn file và thả vào đây!", type=["xlsx", "xls"])

#%% III. Analysis
if uploaded_file is not None:
    try:
        # Reading the uploaded file
        data = pd.read_excel(uploaded_file)
        data.iloc[:, 1] = data.iloc[:, 1].astype(str)

        # Displaying the data
        st.markdown("""
                    ### III. Kết quả phân tích
                    Data của thầy/cô:
                        
                        """)
                        
        st.write(data.head())
        
        
        left, buff, right = st.columns([10, 1, 4])
        with left:
            "**Kết quả xếp loại học lực:**"
            lower_xs = st.number_input("Nhập điểm tối thiểu để xét danh hiệu xuất sắc:",
                                       value=6.5)
            hlr = HLRanking(data, lower_xs=lower_xs)
            st.dataframe(hlr.get_rank())
        with right:
            "**Thống kê:**"
            "Kết quả học tập"
            st.write(hlr.get_stat_KQHT())
            
            "Danh hiệu"
            st.write(hlr.get_stat_DH())
            
        
        csv_data = hlr.get_rank().to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="Tải về file CSV",
            data=csv_data,
            file_name='Xep_loai_hoc_luc.csv',
            mime='text/csv',
        )
        
    except:
        pass
    
st.sidebar.markdown("""
                    ---
            Developed by Neo @ 2025.
            
            Nếu phát hiện lỗi tính toán, hãy báo cho tôi qua zalo nhé.
            
            Phone: không chín bảy hai ba bốn hai năm một tám.
            """)


