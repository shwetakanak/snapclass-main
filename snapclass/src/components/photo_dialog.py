import streamlit as st
from PIL import Image

@st.dialog("Capture or Upload Photo")
def add_photo_dialog():
    st.write("Add classroom photos to scan for attendance.")

    # Initialize session state
    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"

    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = []

    if "last_camera_photo" not in st.session_state:
        st.session_state.last_camera_photo = None

    # Tab buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Camera",
            type="primary" if st.session_state.photo_tab == "camera" else "tertiary",
            width="stretch",
        ):
            st.session_state.photo_tab = "camera"

    with col2:
        if st.button(
            "Upload Photos",
            type="primary" if st.session_state.photo_tab == "upload" else "tertiary",
            width="stretch",
        ):
            st.session_state.photo_tab = "upload"

    st.divider()

    # Camera
    if st.session_state.photo_tab == "camera":
        cam_photo = st.camera_input("Take Snapshot", key="dialog_cam")

        if (
            cam_photo is not None
            and cam_photo != st.session_state.last_camera_photo
        ):
            st.session_state.last_camera_photo = cam_photo

            image = Image.open(cam_photo).copy()
            st.session_state.attendance_images.append(image)

            st.success("Photo captured successfully!")

    # Upload
    elif st.session_state.photo_tab == "upload":
        uploaded_files = st.file_uploader(
            "Choose image files",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="dialog_upload",
        )

        if uploaded_files:
            for file in uploaded_files:
                image = Image.open(file).copy()
                st.session_state.attendance_images.append(image)

            st.success(f"{len(uploaded_files)} photo(s) uploaded successfully!")

    st.divider()

    # Preview
    if st.session_state.attendance_images:
        st.write(f"**Photos Added:** {len(st.session_state.attendance_images)}")

        cols = st.columns(3)
        for i, img in enumerate(st.session_state.attendance_images):
            with cols[i % 3]:
                st.image(img, use_container_width=True)

    # Done button
    if st.button("Done", type="primary", width="stretch"):
        st.rerun()