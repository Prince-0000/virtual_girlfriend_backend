#
# import openai
# # take audio file path and convert it to text
#
# def convert_audio_to_text(local_input_file:str):
#
#     transcription_text=openai.Audio.transcribe("wisper-1",open(local_input_file,'rb'))
#     print(transcription_text)
#     return transcription_text


import requests


def convert_audio_to_text(local_input_file: str):
    url = "https://whisper-speech-to-text1.p.rapidapi.com/speech-to-text"

    # Construct the payload with the file
    boundary = "011000010111000001101001"
    payload = f"-----{boundary}\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n\r\n-----{boundary}--\r\n\r\n"

    headers = {
        "content-type": f"multipart/form-data; boundary=---{boundary}",
        "X-RapidAPI-Key": "ab3e8f8e23msh1ded437a84d1376p1bf0afjsn812f87a92240",
        "X-RapidAPI-Host": "whisper-speech-to-text1.p.rapidapi.com"
    }

    with open(local_input_file, 'rb') as file_data:
        response = requests.post(url, data=payload, headers=headers, files={'file': file_data})

    if response.status_code == 200:
        return response.json()
    else:
        # Handle the error or return an error message
        return {"error": "An error occurred during the request."}


# # Usage
# local_audio_file = "path_to_your_audio_file.wav"
# result = convert_audio_to_text(local_audio_file)
# print(result)
