from openai import OpenAI

client = OpenAI(api_key="!", base_url="http://localhost:11434/v1")

messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-r1:1.5b",
    messages=messages,
    stream=True
)

reasoning_content = ""
content = ""
flag = False
for chunk in response:
    if '</think>' in chunk.choices[0].delta.content:
        chunk.choices[0].delta.reasoning_content = chunk.choices[0].delta.content
        chunk.choices[0].delta.content = ''
        flag = False
    if '<think>' in chunk.choices[0].delta.content or flag:
        flag = True
        chunk.choices[0].delta.reasoning_content = chunk.choices[0].delta.content
        chunk.choices[0].delta.content = ''
    print(chunk)
