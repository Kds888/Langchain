# In this we will make use of the local database in our memory to set the vector database through existing libraries 
# instead of making use of pine cone 

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS # it will help us by providing similarity search for us to look for..
import os 
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


documents = PyPDFLoader(r'C:\Users\karan\Test\japji_sahib.pdf').load() # we see that it has already splitted the document for us in 42 parts
# # But ia m still going to use the text splitter 

# text_splitter = CharacterTextSplitter(chunk_asize=1200,chunk_overlap=100, separator='/n').split_documents(documents)
embeddings= OpenAIEmbeddings(openai_api_key=os.environ.get('OPENAI_API_KEY')) 
vectorstore=FAISS.from_documents(documents,embedding=embeddings) # this will make use of our RAM to store the embeddings and perform similarity search.
vectorstore.save_local('faiss_japji_sahib') 
vectorstore = FAISS.load_local('faiss_japji_sahib',embeddings) # we need embeddings for the secod time to convert back the vectors.
qa = RetrievalQA.from_chain_type(llm=OpenAI(),chain_type='stuff',retriever=vectorstore.as_retriever())
res = qa.run("How to earn enormous wealth in life?")
print(res) 
# Instead of pine cone I will be making use of the FIASS for similarity search. And this works well as well.


