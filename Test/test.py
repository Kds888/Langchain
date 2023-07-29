import os 
from langchain.document_loaders import DataFrameLoader
import pandas as pd 
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings 

pinecone.init(api_key="YOUR API KEY HERE",environment="asia-southeast1-gcp-free")


# data = pd.read_csv('final_chat_df_without_index.csv') 

# loader = DataFrameLoader(data)
# raw_doc = loader.load()
# splitted_doc = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
# raw_doc= splitted_doc.split_documents(raw_doc)  
# # embeddings= OpenAIEmbeddings(openai_api_key=os.environ.get('OPENAI_API_KEY'))  
# # Pinecone.from_documents(raw_doc,embeddings,index_name='dc-chat') 
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA,ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
import pinecone
from langchain import OpenAI

pinecone.init(api_key="YOUR API KEY HERE",environment="asia-southeast1-gcp-free") 

# The only reason we have api's keys have been there is because of strem lit other wise we could make use of the 
# .env varibales

index_name = 'dc-chat'  

def run_llm(query,history):
    embeddings = OpenAIEmbeddings(openai_api_key='YOUR API KEY HERE')
    docsearch = Pinecone.from_existing_index(index_name=index_name,embedding=embeddings) 
    chat= ChatOpenAI(openai_api_key='YOUR API KEY HERE',verbose=True,temperature=0)
    #qa = RetrievalQA.from_chain_type(llm=chat,chain_type='stuff',retriever=docsearch.as_retriever()) # here we need to say that 
    # return_source_documents=True , it will return us the document from which the answer was generated. and we can extract the link from
    # this document
    # We are not making use of the retrievalqa as it won't have the history embedded in it.
    qa = ConversationalRetrievalChain.from_llm(llm=chat,retriever=docsearch.as_retriever()) 
    return qa({'question':query,"chat_history":history})   


gen_response = run_llm(query='Tell me about Artificial intelligence course',history=[]) 

print(gen_response) 