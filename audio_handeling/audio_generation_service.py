# import boto3
#
# polly_client = boto3.client('polly')
#
#
# def convert_text_to_audio(text_content: str):
#     response = polly_client.synthesize_speech(
#         Engine='standard',
#         LanguageCode='en-US',
#         OutputFormat='mp3',
#         Text=text_content,
#         VoiceId='Brian'
#     )
#     return response


"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/OneDrive/Documents/neat-resolver-402713-4c84d4645c4b.json"
from google.cloud import texttospeech

# text_audio:str
# Instantiates a client


def convert_text_to_audio(transcription_content_text: str):
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text = transcription_content_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')



# if __name__=="__main__":
#     convert_text_to_audio()