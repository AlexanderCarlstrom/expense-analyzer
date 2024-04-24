from read_excel import read_excel
from langchain_community.llms import Ollama

with open('prompt.txt', 'r') as file:
    prompt = file.read()

categories = ['groceries', 'food', 'travel', 'home', 'services', 'clothes', 'tech', 'entertainment', 'other']


transactions = read_excel('./transactions.xlsx')
unique = set([t.description for t in transactions])

prompt = prompt.format(', '.join(categories), '\n'.join(unique))

llm = Ollama(model='gemma')
response = llm.invoke(prompt)
print(response)
