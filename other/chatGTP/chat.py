import openai
openai.api_key="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"
model_engine = "text-davinci-003"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=input(),
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
#获取 ChatGPT 的回复
message = completions.choices[0].text
print(message)