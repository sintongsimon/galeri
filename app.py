import streamlit as st
from drive_service import get_drive_service
from gallery import load_gallery

st.set_page_config(layout="wide")

st.title("📷 My Google Drive Gallery")

FOLDER_ID = "YOUR_FOLDER_ID"

service = get_drive_service()

files = load_gallery(service, FOLDER_ID)

images = []
videos = []

for f in files:

    url = f"https://drive.google.com/uc?id={f['id']}"

    if "image" in f["mimeType"]:
        images.append(url)

    elif "video" in f["mimeType"]:
        videos.append(url)

st.subheader("Photos")

cols = st.columns(4)

for i, img in enumerate(images):

    with cols[i % 4]:
        if st.image(img, use_container_width=True):
            st.session_state["selected"] = img

if "selected" in st.session_state:

    st.image(st.session_state["selected"], width=900)

st.subheader("Videos")

for vid in videos:
    st.video(vid)
