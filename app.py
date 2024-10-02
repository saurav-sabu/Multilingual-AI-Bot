import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

def main():
    st.title("MultiLingual Bot")

    if st.button("Ask me"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)

            audio_file = open("speech.mp3","rb") 
            audio_data = audio_file.read()

            st.text_area(label="Response:",value=response,height=350)
            st.audio(audio_data)
            st.download_button(label="Download Speech",
                               data=audio_data,
                               file_name="speech.mp3",
                               mime="audio/mp3")


if __name__ == "__main__":
    main()

