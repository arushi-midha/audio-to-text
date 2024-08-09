# Audio To Text App

This Streamlit-based web application allows users to upload audio files and transcribe them into text using Google's Speech Recognition API. The app supports `.wav` and `.mp3` audio formats and provides a clean interface for uploading, transcribing, and downloading the resulting text file.

## How It Works

1. **File Upload**:
    - The user uploads an audio file in either `.wav` or `.mp3` format.
    - The uploaded file is displayed using Streamlit's audio player.

2. **Transcription**:
    - The audio file is temporarily saved and processed.
    - Google's Speech Recognition API is used to transcribe the audio to text.
    - Background noise is reduced using the `adjust_for_ambient_noise` method.

3. **Download Transcription**:
    - The transcribed text is displayed on the page.
    - Users can download the transcribed text as a `.txt` file.

4. **Cleanup**:
    - The temporary audio file is deleted after processing to save space.

## Live Link

