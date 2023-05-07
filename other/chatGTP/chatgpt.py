import openai

class chatgpt():
    def __init__(self,openai_key) -> None:
        openai.api_key = openai_key
        self.answer=list()
    
    def to_prompt(self,prompt):
        self.answer.append({'role':'user','content':prompt})
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.answer
        )
        print("答："+completions["choices"][0]['message']['content'])
        self.answer.append({'role':'assistant','content':completions["choices"][0]['message']['content']})
if __name__=="__main__":
    # 设置 API Key
    chatgpt=chatgpt("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")

    # 设置请求参数
    while True:
        chatgpt.to_prompt(input("问："))