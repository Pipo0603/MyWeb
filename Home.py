import requests
import streamlit as st
from streamlit_lottie import st_lottie
import cv2
from PIL import Image


st.set_page_config( page_title="HELLO",page_icon="💁‍♂️",layout= "wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json() 
#------Xai Css --------

#======TIÊU DỀ========
st.subheader("ĐÂY LÀ WEBSIDE CỦA NHẬT")
st.write("Chúng tôi là sinh viên năm 3 - Ngành CNKT Cơ điện tử")
st.title("CHÀO MỪNG CÁC BẠN ĐẾN VỚI THẾ GIỚI CỦA CHÚNG MÌNH🤗")
st.markdown(
    """
    Đây là project từ môn học Thị giác máy và Học máy
    """
)
st.markdown(
    """
    **👈 Bây giờ, các bạn có thể xem bên trái để biết các tính năng của web nhé!
    """
)

# Set up some CSS
CSS = """
    img {
        border-radius: 50%;
        background-size: cover;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    }
"""

# Add the CSS to the page
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


# Add an image with the custom styles applied
image_1 = Image.open("image/1.jpg")
image_2 = Image.open("image/2.jpg")

col1, col2 = st.columns(2)
with col1:
   st.header("Lê Quang Nhật")
   st.image(image_1, width=250)
with col2:
   st.header("Nguyễn Đoàn Quang Nhật")
   st.image(image_2, width=250)

st.markdown(
    """
  
    ### NGƯỜI THỰC HIỆN: 
    - Họ và tên: Lê Quang Nhật                 - MSSV: 20146383
    - Họ và tên: Nguyễn Đoàn Quang Nhật        - MSSV: 20146384
    - Trường: ĐH Sư Phạm Kỹ Thuật TP. Hồ Chí Minh
    ### LIÊN HỆ:
    - Email: nhat0603pipo@gmail.com
    - FB: [Lê Quang Nhật](https://www.facebook.com/pipo0603)\\
          [Nguyễn Đoàn Quang Nhật](https://www.facebook.com/profile.php?id=100023607876987)
"""
)
#------Tao Contact Form-------
with st.container():
    st.write("---")
    st.header("TƯƠNG TÁC VỚI CHÚNG TÔI TẠI ĐÂY 🤝!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/nhat0603pipo@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Tên của bạn" required>
     <input type="email" name="email"placeholder=" Email của bạn" required>
     <textarea name = "message" placeholder="Ý kiến của mọi người về Webside!" required></textarea>
     <button type="submit">gửi</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()




