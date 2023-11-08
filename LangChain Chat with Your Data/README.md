# LangChain Chat with Your Data
# Presentation
[Google Slides](https://docs.google.com/presentation/d/1G1ScJ2P_3Mb1r_MHyrQ3ffaDf-G_6tr56-9vbVJvfsY/edit#slide=id.g25f6af9dd6_0_0)
## Part1: Document Loading
### Step1: PDF
[2023 Catalog](https://www.sfbu.edu/sites/default/files/2022-12/2023Catalog.pdf)

Code for reference:

```
pip install langchain
pip install pypdf 
```


```
import openai
# Set your OpenAI API key
with open('api_key.txt', 'r') as file:
    openai.api_key = file.read().strip()

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("2023Catalog.pdf")
pages = loader.load()
page = pages[0]
print(page.page_content[0:500])
```
The result:

<img width="435" alt="Screenshot 2023-10-22 at 7 43 17 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/1e02811c-4310-4abf-a5ca-66994e6ce64d">

### Step2: Youtube
[San Francisco Bay University MBA Student Spotlight: John Odebode](https://www.youtube.com/watch?v=kuZNIvdwnMc)

Code for reference:

```
pip install yt_dlp
pip install pydub
```

```
brew install ffmpeg
```
```
# Step2: Youtube
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
url="https://www.youtube.com/watch?v=kuZNIvdwnMc"
save_dir="./docs/youtube/"

loader = GenericLoader(
    YoutubeAudioLoader([url],save_dir),
    OpenAIWhisperParser()
)

docs = loader.load()
print(docs[0].page_content[0:500])
```

The result:

<img width="612" alt="Screenshot 2023-10-22 at 8 00 50 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/5e63ab56-35b8-449b-811c-90061752ea62">

### Step3: URLs
[Student Insurance](https://www.sfbu.edu/admissions/student-health-insurance)

```
# Step3: URLs
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.sfbu.edu/admissions/student-health-insurance")
docs = loader.load()
print(docs[0].page_content[:500])
```

The result:

<img width="626" alt="Screenshot 2023-10-22 at 8 03 40 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/060df168-3b9e-4e47-8b86-442f5c691d0d">

## Part2: Vectorstores and Embedding
Steps: 

1. Load documents    
    The same steps as the previous part.
2. Split the documents into small, semantically meaningful chunks   

   ```
   from langchain.text_splitter import RecursiveCharacterTextSplitter
   text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1500,
        chunk_overlap = 150
    )
    splits = text_splitter.split_documents(docs)
   ```
3. Create an index for each chunk by embeddings  
    ```
    from langchain.embeddings.openai import OpenAIEmbeddings
    embedding = OpenAIEmbeddings()
    ```
   
4. Store these index in a vector stores for easy retrieval when answering questions
    
    ```
    from langchain.vectorstores import Chroma
    persist_directory = './docs/chroma/'
    
    # remove old database files if any
    # get_ipython().system('rm -rf ./docs/chroma')  
    
    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embedding,
        persist_directory=persist_directory
    )
    print(vectordb._collection.count())
    ```
5. Search answer of a question.

    ```
    question = "is there an email i can ask for help"
    docs = vectordb.similarity_search(question,k=3)
    print("The original answer: ")
    print("===================>")
    print(docs[0].page_content)
    print("===================>")
    vectordb.persist()
    ```
6. Edge Cases - Failure
    ```
    docs_mmr = vectordb.max_marginal_relevance_search(question,k=3)
    print("The diverse answer1: ")
    print("===================>")
    print(docs_mmr[0].page_content)
    print("===================>")
    print("The diverse answer2: ")
    print("===================>")
    print(docs_mmr[1].page_content)
    print("===================>")
    ```
    ```
    new_question = "What are the application requirements for the MSCS program at SFBU?"
    # docs = vectordb.similarity_search(
    #     question,
    #     k=3,
    #     filter={"source":
    #      "2023Catalog.pdf"}
    # )
    from langchain.llms import OpenAI
    from langchain.retrievers.self_query.base import SelfQueryRetriever
    from langchain.chains.query_constructor.base import AttributeInfo
    
    metadata_field_info = [
    
     AttributeInfo(
       name="source",
       description="The catalog the chunk is from, should \
          be `2023Catalog.pdf`",
       type="string",
       ),
    
     AttributeInfo(
       name="page",
       description="The page from the catalog",
       type="integer",
     ),
    
    ]
    
    document_content_description = "Lecture notes"
    llm = OpenAI(temperature=0)
    retriever = SelfQueryRetriever.from_llm(
        llm,
        vectordb,
        document_content_description,
        metadata_field_info,
        verbose=True
    )
    
    docs = retriever.get_relevant_documents(new_question)
    for d in docs:
        print(d.metadata)
    ```

My question: Is there an email i can ask for help?

The result:

<img width="613" alt="Screenshot 2023-10-22 at 11 32 38 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/17b0f487-f255-4560-8af1-71f90468acd0">

The diverse answer:

<img width="612" alt="Screenshot 2023-10-22 at 11 53 17 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/76071fed-c79f-4a17-960e-01315e97bd18">

<img width="620" alt="Screenshot 2023-10-22 at 11 53 35 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/e82c5acf-a18d-418e-b4f5-ae6894024f92">


The metadata:

<img width="301" alt="Screenshot 2023-10-22 at 11 45 32 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/ab8a6dd3-b42f-4515-b353-8d6fd080987a">

The End

## Part3: Chat
### Step 1: Overview of the workflow for RAG 
```
pip install panel
```
```

import os
import openai
import panel as pn  # GUI
pn.extension()

from dotenv import load_dotenv, find_dotenv
# read local .env file
_ = load_dotenv(find_dotenv()) 

openai.api_key  = os.environ['OPENAI_API_KEY']

import datetime
current_date = datetime.datetime.now().date()
if current_date < datetime.date(2023, 9, 2):
    llm_name = "gpt-3.5-turbo-0301"
else:
    llm_name = "gpt-3.5-turbo"
print(llm_name)
```
### Step 2: Load document and create VectorDB
```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
persist_directory = 'docs/chroma/'
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, 
                  embedding_function=embedding)
```
### Step 3: Similarity Search to select relevant chunks (splits)
```
question = "What are major topics for this class?"
docs = vectordb.similarity_search(question,k=3)
print("The length of docs is ", len(docs))
```
### Step 4: Create LLM
```
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name=llm_name, temperature=0)
llm.predict("Hello world!")
```
### Step 5: ConversationalRetrievalChain
#### Step 5.1: Create Memory 
```
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    # Set return messages equal true
    # - Return the chat history as a  list of messages 
    #   as opposed to a single string. 
    return_messages=True
) 
```

#### Step 5.2: QA with Conversational Retrieval Chain
```
from langchain.chains import ConversationalRetrievalChain

retriever=vectordb.as_retriever()
qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=retriever,
    memory=memory
)
```
#### Step 5.3: Test ConversationalRetrievalChain
##### Step 5.3.1: First Question
```
question = "Is probability a class topic?"
result = qa({"question": question})
print("The answer of first question is", result['answer'])
```
##### Step 5.3.2: Follow-up Question
```
question = "why are those prerequesites needed?"
result = qa({"question": question})
print("The answer of follow-up question is", result['answer'])
```
### Step 6: Create a chatbot that works on your documents
```
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
```
#### Step 6.1: Create a chatbot that works on your documents ---- Create Business Logic
```
def load_db(file, chain_type, k):
    # load documents
    loader = PyPDFLoader(file)
    documents = loader.load()
    # split documents
    text_splitter = RecursiveCharacterTextSplitter(
           chunk_size=1000, 
           chunk_overlap=150)
    docs1 = text_splitter.split_documents(documents)
    # define embedding
    embeddings = OpenAIEmbeddings()
    # create vector database from data
    db = DocArrayInMemorySearch.from_documents(docs1, 
           embeddings)
    # define retriever
    retriever = db.as_retriever(search_type="similarity", 
           search_kwargs={"k": k})
    # create a chatbot chain. Memory is managed externally.
    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model_name=llm_name, temperature=0), 
        chain_type=chain_type, 
        retriever=retriever, 
        return_source_documents=True,
        return_generated_question=True,
    )
    return qa 
```
```
import param
class cbfs(param.Parameterized):
    chat_history = param.List([])
    answer = param.String("")
    db_query = param.String("")
    db_response = param.List([])

    def __init__(self,  **params):
        super(cbfs, self).__init__( **params)
        self.panels = []
        self.loaded_file = "./2023Catalog.pdf"
        self.qa = load_db(self.loaded_file,"stuff", 4)

    def call_load_db(self, count):
        # init or no file specified :
        if count == 0 or file_input.value is None:  
            return pn.pane.Markdown(f"Loaded File: {self.loaded_file}")
        else:
            file_input.save("temp.pdf")  # local copy
            self.loaded_file = file_input.filename
            button_load.button_style="outline"
            self.qa = load_db("temp.pdf", "stuff", 4)
            button_load.button_style="solid"
        self.clr_history()
        return pn.pane.Markdown(
            f"Loaded File: {self.loaded_file}")
    
    def convchain(self, query):
        if not query:
            return pn.WidgetBox(pn.Row('User:', 
               pn.pane.Markdown("", width=600)), scroll=True)
        result = self.qa({"question": query, 
                          "chat_history": self.chat_history})
        self.chat_history.extend([(query, result["answer"])])
        self.db_query = result["generated_question"]
        self.db_response = result["source_documents"]
        self.answer = result['answer'] 
        self.panels.extend([
            pn.Row('User:', pn.pane.Markdown(query, width=600)),
            pn.Row('ChatBot:', pn.pane.Markdown(self.answer, 
               width=600, 
               style={'background-color': '#F6F6F6'}))
        ])
        inp.value = ''  #clears loading indicator when cleared
        return pn.WidgetBox(*self.panels,scroll=True)
    
    @param.depends('db_query ', )
    def convchain(self):
        if not self.db_query :
            return pn.Column(
                pn.Row(pn.pane.Markdown(f"Last question to DB:", 
            styles={'background-color': '#F6F6F6'})),
                pn.Row(pn.pane.Str("no DB accesses so far"))
            )
        return pn.Column(
            pn.Row(pn.pane.Markdown(f"DB query:", 
            styles={'background-color': '#F6F6F6'})),
            pn.pane.Str(self.db_query )
        )
    
    @param.depends('db_response', )
    def get_sources(self):
        if not self.db_response:
            return 
        rlist=[pn.Row(pn.pane.Markdown(f"Result of DB lookup:", 
            styles={'background-color': '#F6F6F6'}))]
        for doc in self.db_response:
            rlist.append(pn.Row(pn.pane.Str(doc)))
        return pn.WidgetBox(*rlist, width=600, scroll=True)
    
    @param.depends('convchain', 'clr_history') 
    def get_chats(self):
        if not self.chat_history:
            return pn.WidgetBox(
                  pn.Row(pn.pane.Str("No History Yet")), 
                   width=600, scroll=True)
        rlist=[pn.Row(pn.pane.Markdown(
            f"Current Chat History variable", 
            styles={'background-color': '#F6F6F6'}))]
        for exchange in self.chat_history:
            rlist.append(pn.Row(pn.pane.Str(exchange)))
        return pn.WidgetBox(*rlist, width=600, scroll=True)
    
    def clr_history(self,count=0):
        self.chat_history = []
        return 
```
#### Step 6.2: Create a web-based user interface
Front-end:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>San Francisco Bay University Service Bot</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        text-align: center;
      }

      h1 {
        color: #3498db;
      }

      form {
        margin-top: 20px;
      }

      input[type="text"] {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        width: 70%;
        font-size: 16px;
      }

      button[type="submit"] {
        padding: 10px 20px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
      }

      button[type="submit"]:hover {
        background-color: #2980b9;
      }

      h2 {
        margin-top: 20px;
        color: #3498db;
      }

      ul {
        list-style: none;
        padding: 0;
      }

      li {
        margin: 10px 0;
      }
    </style>
  </head>
  <body>
    <h1>San Francisco Bay University Service Bot</h1>

    <form method="POST" action="/submit_question">
      <input type="text" name="question" placeholder="Ask a question" />
      <button type="submit">Submit</button>
    </form>

    <!-- Add a "Start New Chat" button -->
    <form method="POST" action="/start_new_chat">
      <button type="submit">Start New Chat</button>
    </form>

    <div>
      <h2>Replies:</h2>
      <ul>
        {% for question, reply in replies.items() %}
        <li><strong>{{ question }}</strong>: {{ reply }}</li>
        {% endfor %}
      </ul>
    </div>
  </body>
</html>
```

Back-end:
```
from flask import Flask, render_template, request, redirect, url_for
from cbfs import cbfs

app = Flask(__name__)

# Sample data for replies (you can replace this with your chatbot logic)
replies = {}
c = cbfs()

@app.route('/')
def index():
    return render_template('index.html', replies=replies)

@app.route('/submit_question', methods=['POST'])
def submit_question():
    question = request.form.get('question')
    reply = c.convchain(question)  # Replace with your chatbot logic
    replies[question] = reply
    return index()

@app.route('/start_new_chat', methods=['POST'])
def start_new_chat():
    # Clear the conversation history to start a new chat
    c.clr_history()
    replies.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```
