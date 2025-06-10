import ollama
response = ollama.chat(model='mistral', messages=[
    {"role": "user", "content": "What is Retrieval-Augmented Generation?"}
])
print(response['message']['content'])
