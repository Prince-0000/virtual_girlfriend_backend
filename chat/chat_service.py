from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from project_config import setup_app_config


# import the keys using app_config

setup_app_config()
llm = ChatOpenAI(temprature=1.0)

chat_memory = ConversationBufferMemory()


def handle_get_response_for_user(user_prompt: str)->str:
    conversation = ConversationChain(
        llm=llm,
        vebrose=False,
        memory=chat_memory
    )

    result = conversation.predict(input=user_prompt)
    print("result>>",result)
    return result


# take user input
def run():
    while True:
        user_prompt=input("ask something>>")

        if user_prompt=='0':
            break
        #     else call the function
        handle_get_response_for_user(user_prompt)



if __name__ == "__main__":
    run()