import streamlit as st
from PIL import Image 

st.subheader("Thư giãn bằng 1 đoạn nhạc:")
st.audio("ThePromise-HoaTau.mp3")

image_1 = Image.open("image/1.jpg")

col1, col2 = st.columns(2)
with col1:
   st.header("Lê Quang Nhật")
   st.image(image_1, width=250)

st.markdown(
    """
    ### LIÊN HỆ:
    - Email: nhat0603pipo@gmail.com
    - FB: [Lê Quang Nhật](https://www.facebook.com/pipo0603)
    - Kênh Youtube: [PIPO](https://bit.ly/pipoyoutube)
    - Link GitHub: [pipo0603](https://github.com/Pipo0603)
    - SĐT: 0886820603
"""
)
#------Tao Contact Form-------
with st.container():
    st.write("---")
    st.header("TƯƠNG TÁC VỚI MÌNH TẠI ĐÂY 🤝!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/nhat0603pipo@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Tên của bạn" required>
     <input type="email" name="email"placeholder="Email của bạn" required>
     <textarea name = "message" placeholder="Nơi tương tác..." required></textarea>
     <button type="submit">gửi</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()