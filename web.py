import streamlit as st
import face_detect as fd
import cv2

'''st.write('hi')
st.sidebar.header('User Input Features')
SMILES_input = "NCCCC\nCCC\nCN"
SMILES = st.sidebar.text_area("SMILES input", 'fff')'''


st.title("Webcam Application")
run = st.checkbox('Run')

FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)

while run:
    ret, frame = cam.read()
    #contour_bymp(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #fd.contour_faces(frame)
    fd.contour_bymp(frame)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
