import streamlit as st

@st.cache_data(ttl=300)
def load_gallery(service, folder_id):

    results = service.files().list(
        q=f"'{folder_id}' in parents",
        fields="files(id,name,mimeType)"
    ).execute()

    return results.get("files", [])
