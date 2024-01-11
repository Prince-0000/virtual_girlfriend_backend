import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/devanshyadav/Downloads/neat-resolver-402713-4c84d4645c4b.json"
from google.cloud import texttospeech

# text_audio:str
# Instantiates a client


def convert_text_to_audio(transcription_content_text: str):
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text = transcription_content_text)
    # radhika
    voice=texttospeech.VoiceSelectionParams(
        language_code="en-IN", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    #buddy
    #chaacha
    # voice = texttospeech.VoiceSelectionParams(
    #     language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    # )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=6,
        speaking_rate=0.93
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    print("binaryyy",type(response))
    return response.audio_content




    # # The response's audio_content is binary.
    # with open("output.mp3", "wb") as out:
    #     # Write the response to the output file.
    #     out.write(response.audio_content)
    #     # print (".",response.audio_content)
    #     print('Audio content written to file "output.mp3"')



# if __name__=="__main__":
#     convert_text_to_audio()