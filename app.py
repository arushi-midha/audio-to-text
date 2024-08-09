import streamlit as st
import speech_recognition as sr
import os

# Initialize the speech recognizer
r = sr.Recognizer()

# Set the title and description of the app
st.title("Audio To Text App")
st.write("Transcribe audio files to text")
st.write()
st.write()

# File uploader for audio files
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file is not None:
    # Display the audio file
    st.audio(audio_file, format="audio/wav")

    # Create a temporary audio file
    temp_audio_path = "temp_audio.wav"
    with open(temp_audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    # Use the speech recognizer to transcribe the audio
    with sr.AudioFile(temp_audio_path) as source:
        st.write("Transcribing the audio...")

        # Reduce background noise
        r.adjust_for_ambient_noise(source)

        # Listen to the audio file
        audio_text = r.listen(source, phrase_time_limit=30)

    try:
        # Recognize the audio using Google Speech Recognition
        text = r.recognize_google(audio_text)
        st.write("Transcription:")
        st.write(text)

        # Create a download button for the transcribed text
        txt_file_name = "transcription.txt"
        with open(txt_file_name, "w") as txt_file:
            txt_file.write(text)

        # Create a download link for the text file
        with open(txt_file_name, "rb") as f:
            st.download_button("Download as .txt", f, file_name=txt_file_name)

    except sr.RequestError:
        st.write("API is unreachable or unresponsive. Please check your internet connection.")
    except sr.UnknownValueError:
        st.write("Unable to recognize speech.")
    except Exception as e:
        st.write(f"An error occurred: {e}")
    finally:
        # Delete the temporary audio file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)


footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: lavender;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: grey;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p> </p>
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/arushi-midha" target="_blank">Arushi Midha</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)