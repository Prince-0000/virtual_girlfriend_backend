from app.utils.file_utils import persist_binary_file_locally, create_unique_tmp_file
from app.transcoding.transcoding_service import convert_file_to_readable_mp3
from app.audio_handeling.audio_transcription_service import convert_audio_to_text
from app.chat.chat_service import handle_get_response_for_user
from app.audio_handeling.audio_generation_service import convert_text_to_audio


# get file path
def __get_transcode_audio_file_path(data: bytes) -> str:
    local_file_path = persist_binary_file_locally(data, file_suffix='user_audio.mp3')
    print("create unique_temp_file")
    local_output_file_path = create_unique_tmp_file(file_suffix='transcode_user_audio.mp3')

    # pass input and output file path
    convert_file_to_readable_mp3(
        local_input_file_path=local_file_path,
        local_ouput_file_path=local_output_file_path)

    return local_output_file_path


async def handle_audio_from_user(file: bytes)->str:

    print("handle  audio from user")
    transcode_user_audio_file_path = __get_transcode_audio_file_path(file)
    print("we recieved the audio_file_path",transcode_user_audio_file_path)
    # call stt
    transcription_content_text = convert_audio_to_text(transcode_user_audio_file_path)
    print(transcription_content_text)

    for_gf='you are going to act as my girlfriend and respond in 15 words max and act cute and caring reply in hindi, do not give me translation in english'
        #call chatgpt
    arg=for_gf+transcription_content_text
    ai_text_reply=handle_get_response_for_user(arg)
    # call tts
    generated_audio_ai = convert_text_to_audio(ai_text_reply)

    output_audio_local_file_path = persist_binary_file_locally(
        data=generated_audio_ai,
        file_suffix='ai_audio_reply.mp3'
    )
    return output_audio_local_file_path












    # text_content = transcription_content_text['text']
    #
    #
    # # tranfer the text from wisper to chatgpt
    # ai_reply = handle_get_response_for_user(text_content)
    # print(ai_reply)
    # generate_audio = convert_text_to_audio(ai_reply)