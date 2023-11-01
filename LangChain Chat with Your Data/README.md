# LangChain Chat with Your Data
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
