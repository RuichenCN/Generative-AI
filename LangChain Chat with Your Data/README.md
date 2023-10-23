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