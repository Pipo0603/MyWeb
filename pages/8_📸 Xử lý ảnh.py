import streamlit as st
import sys
import time
import tkinter
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs
import cv2
import numpy as np
import Chapter03 as c3
import Chapter04 as c4
import Chapter05 as c5
import Chapter09 as c9

st.set_page_config(page_title="Xử lý ảnh",page_icon="📷📸")

no = st.sidebar.selectbox('Chọn Chương ',['Chọn Chương','Chương 3','Chương 4','Chương 5','Chương 9'])
import base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/716398/pexels-photo-716398.jpeg?auto=compress&cs=tinysrgb&w=600");
background-size: 100%;
background-position: 30% 45%;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: 50% 45%;
background-size: 400%;
}}
[data-testid="stSidebarNav"] span {{
color:white;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
with st.spinner('XIN HÃY CHỜ MỘT TÍ...'):
    time.sleep(5)
st.success('ĐÃ SẴN SÀNG!')
st.markdown(page_bg_img, unsafe_allow_html=True
)
def main():
    st.title("Machine Vision")
    if (no=="Chương 3"):
        menu = ["Open", "OpenColor", "Save", "Exit"]
        choice = st.sidebar.selectbox("Select an action", menu)

        if choice == "Open":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 0)
                st.image(image, use_column_width=True)

        elif choice == "OpenColor":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 1)
                st.image(image, channels="BGR", use_column_width=True)

        elif choice == "Save":
            st.warning("This feature is not available in Streamlit.")

        elif choice == "Exit":
            st.stop()

        sub_choice = st.sidebar.selectbox('Mời bạn chọn phương thức xử lý ảnh chương 3',['No Action','Negative','Logarit','PiecewiseLinear','Histogram','HistEqual',
                    'HistEqualColor','LocalHist','HistStat','BoxFilter','LowpassGauss','Threshold',
                    'MedianFilter','Sharpen'])
        
        if sub_choice == "Negative":
            if "image" in locals():
                imgout = c3.Negative(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")

        elif sub_choice == "Logarit":
            if "image" in locals():
                imgout = c3.Logarit(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        elif sub_choice == "PiecewiseLinear":
            if "image" in locals():
                imgout = c3.PiecewiseLinear(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        elif sub_choice == "Histogram":
            if "image" in locals():
                imgout = c3.Histogram(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")

        elif sub_choice == "HistEqua":
            if "image" in locals():
                imgout = c3.equalizeHist(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")

        elif sub_choice == "HistEqualColor":
            if "image" in locals():
                imgout = c3.HistEqualColor(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        elif sub_choice == "LocalHist":
            if "image" in locals():
                imgout = c3.LocalHist(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")

        elif sub_choice == "HistStat":
            if "image" in locals():
                imgout = c3.HistStat(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        elif sub_choice == "BoxFilter":
            if "image" in locals():
                imgout = c3.blur(image,(21,21))
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")

        elif sub_choice == "LowpassGauss":
            if "image" in locals():
                imgout = c3.GaussianBlur(image,(43,43),7.0)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")

        elif sub_choice == "Threshold":
            if "image" in locals():
                imgout = c3.Threshold(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        elif sub_choice == "MedianFilter":
            if "image" in locals():
                imgout = c3.medianBlur(image, 7)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        elif sub_choice == "Sharpen":
            if "image" in locals():
                imgout = c3.Sharpen(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        elif sub_choice == "Gradient":
            if "image" in locals():
                imgout = c3.Gradient(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
    if (no=="Chương 4"):
        menu = ["Open", "OpenColor", "Save", "Exit"]
        choice = st.sidebar.selectbox("Select an action", menu)

        if choice == "Open":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 0)
                st.image(image, use_column_width=True)

        elif choice == "OpenColor":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 1)
                st.image(image, channels="BGR", use_column_width=True)

        elif choice == "Save":
            st.warning("This feature is not available in Streamlit.")

        elif choice == "Exit":
            st.stop()

        sub_choice = st.sidebar.selectbox('Mời bạn chọn phương thức xử lý ảnh chương 4',['No Action','Spectrum','FrequencyFilter','DrawNotchRejectFilter','RemoveMoire'])
        
        if sub_choice == "Spectrum":
            if "image" in locals():
                imgout = c4.Spectrum(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "FrequencyFilter":
            if "image" in locals():
                imgout = c4.FrequencyFilter(image)
                st.image(imgout, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "DrawNotchRejectFilter":
            if "image" in locals():
                imgout1 = c4.DrawNotchRejectFilter(image)
                st.image(imgout1, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "RemoveMoire":
            if "image" in locals():
                imgout1 = c4.RemoveMoire(image)
                st.image(imgout1, use_column_width=True)
            else:
                st.warning("Please open an image first.")
    if (no=="Chương 5"):
        menu = ["Open", "OpenColor", "Save", "Exit"]
        choice = st.sidebar.selectbox("Select an action", menu)

        if choice == "Open":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 0)
                st.image(image, use_column_width=True)

        elif choice == "OpenColor":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 1)
                st.image(image, channels="BGR", use_column_width=True)

        elif choice == "Save":
            st.warning("This feature is not available in Streamlit.")

        elif choice == "Exit":
            st.stop()

        sub_choice = st.sidebar.selectbox('Mời bạn chọn phương thức xử lý ảnh chương 5',['No Action','CreateMotionNoise','DenoiseMotion','DenoisestMotion'])
        
        if sub_choice == "CreateMotionNoise":
            if "image" in locals():
                imgout2 = c5.CreateMotionNoise(image)
                st.image(imgout2, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "DenoiseMotion":
            if "image" in locals():
                imgout2 = c5.DenoiseMotion(image)
                st.image(imgout2, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "DenoisestMotion":
            if "image" in locals():
                imgout2 = c5.DenoisestMotion(image)
                st.image(imgout2, use_column_width=True)
            else:
                st.warning("Please open an image first.")
    if (no=="Chương 9"):
        menu = ["Open", "OpenColor", "Save", "Exit"]
        choice = st.sidebar.selectbox("Select an action", menu)

        if choice == "Open":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 0)
                st.image(image, use_column_width=True)

        elif choice == "OpenColor":
            st.set_option('deprecation.showfileUploaderEncoding', False)
            file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
            if file:
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 1)
                st.image(image, channels="BGR", use_column_width=True)

        elif choice == "Save":
            st.warning("This feature is not available in Streamlit.")

        elif choice == "Exit":
            st.stop()

        sub_choice = st.sidebar.selectbox('Mời bạn chọn phương thức xử lý ảnh chương 9',['No Action','Erosion','Dilation','OpeningClosing','Boundary','HoleFill',
                                'HoleFillingMouse','ConnectedComponent','CountRice'])
        if sub_choice == "Erosion":
            if "image" in locals():
                imgout3 = c9.Erosion(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "Dilation":
            if "image" in locals():
                imgout3 = c9.Dilation(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "OpeningClosing":
            if "image" in locals():
                imgout3 = c9.OpeningClosing(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "Boundary":
            if "image" in locals():
                imgout3 = c9.Boundary(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "HoleFill":
            if "image" in locals():
                imgout3 = c9.HoleFill(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "HoleFillingMouse":
            if "image" in locals():
                imgout3 = c9.HoleFillingMouse(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "CountRice":
            if "image" in locals():
                imgout3 = c9.CountRice(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        if sub_choice == "ConnectedComponent":
            if "image" in locals():
                imgout3 = c9.ConnectedComponent(image)
                st.image(imgout3, use_column_width=True)
            else:
                st.warning("Please open an image first.")
        
if __name__ == "__main__":
    main()

