import ollama

#question = "What is capital of india"
question = input("Enter your question: ").strip()
chat_message = [{'role': 'user','content': question,},]
response = ollama.chat(model='llama3', messages=chat_message)
#print(response)
answer = response['message']['content']
print(f"Question : {question}")
print(f"  Answer : {answer}")