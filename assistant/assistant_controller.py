from fastapi import APIRouter, Form, UploadFile
from fastapi.responses import FileResponse
from assistant.assistant_service import handle_audio_from_user

controller = APIRouter(prefix='/voice-assistant')


# pass the binaryfile using this fucntion
# here we are getting audio file from bac
@controller.post('/audio-message', status_code=200)
async def handel_receive_audio_data(file: UploadFile):
    print("data passed",file)
    file_data = await file.read()
    generate_ai_audio_file_path = await handle_audio_from_user(file_data)
    print(generate_ai_audio_file_path)
    # # we may not need this line
    # return FileResponse(generate_ai_audio_file_path, media_type='audio/mpeg', filename='ai_output')
