import speech_recognition as sr
from pydub import AudioSegment


def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(audio_file_path)
    wav_file = audio_file_path.replace(".mp3", ".wav")
    audio.export(wav_file, format="wav")

    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    finally:
        # Clean up the temporary WAV file
        import os
        os.remove(wav_file)






# Usage example
# if __name__ == "__main__":
#     audio_path = ""
#     transcribed_text = convert_audio_to_text(audio_path)
#     print("Transcribed Text:")
#     print(transcribed_text)
