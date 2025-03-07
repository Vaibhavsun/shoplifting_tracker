import streamlit as st
import tempfile
import os
from saving_annotate_video import saving_annotated_video

st.title("ShopLifting Tracking and Detection")

uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

def save_uploaded_file(uploaded_file):
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

if uploaded_file:
    saved_video_path = save_uploaded_file(uploaded_file)



    if st.button("Process Video"):
        text=st.empty()
        text.write("Processing Video...")
        progress=st.progress(0)
        saving_annotated_video(saved_video_path,progress_bar=progress)
        text.write("Completed..")
        st.success("Video processed successfully!")
        with open('out.mp4', "rb") as f:
            st.download_button("Download Anotated Video", f, file_name="processed_video.mp4", mime="video/mp4")

        with open('out.csv', "rb") as f:
            st.download_button("Download CSV", f, file_name="data.csv", mime="text/csv")


