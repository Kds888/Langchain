# I will be adding the explanation of as to what is vector based database so as to understand it much better
# we are building an application where it can react with the documnets given to it, we would implement it by making use of embeddings
# so we take the document we convert it into vector embeddings and then we take in the query we convert it into embeddings and 
# then we find the chunks of the documnet that are similar to that query and then we send it to the the LLM the context and the query 
# to answer our given question, it is very similar to what we do in question_answering task. 
import os 
from langchain.document_loaders import TextLoader
# so basically we just take the data and add some meta data to it and return this as a list, we can see this in the langchain files or by oopnening 
# textloader from above in python, the main task of this is to make the data more ingestible to the LLM's 
from langchain.text_splitter import CharacterTextSplitter
# We need this to process the text in the documnet as there is a lot of data that we have in the documnet and therefore inorder to process that data 
# we can't send the entire dataset to the LLM as then it will not process it but we can send the data partially within the context length window.
# we have context window approach here when we split the text so as to not miss the answer in a given context window and it will be mentioned in the 
# chunk overlap_ parameter. remeber how we handle the context windows in the Question-Answering part.
from langchain.embeddings.openai import OpenAIEmbeddings
# just to convert the text into vectors making use of OPEN AI,the best part in langchain is that all we need to do is to change the interface 
from langchain.vectorstores import Pinecone
# just a place to store this embeddings in a vector format and we may need to add more vectors to it 
from langchain import VectorDBQA,OpenAI
# vector dbqa is just a chain that is designed for document asnwering, it basically retrievs the relevant document from the vector databse given 
# the input query, after that we decode the given data again into the words and then send it to the llm for question_answering.
import pinecone

pinecone.init(api_key="YOUR API KEY HERE",environment="asia-southeast1-gcp-free") 

loader = TextLoader(r"C:\Users\karan\Test\vdb.txt")
document=loader.load() # when we print the document we can see that we have a list of the  and the meta data attached to the end of the documnet and 
# we can see that within the list we have a tuple with page COntent data and the metadata , whereas the meta data is a dictionery with sourcse as key.
text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0) # due to this we can see that our answers may not be good as to 
# the fact that we have only the 
texts = text_splitter.split_documents(document)
#print(len(texts)) # basically we have splitted the text into 7 parts with no over lap
# we now need to move towards the OPEN AI embeddings
embeddings= OpenAIEmbeddings(openai_api_key=os.environ.get('OPENAI_API_KEY')) 
docsearch = Pinecone.from_documents(texts,embeddings,index_name='test-doc-1')# currently revoked index_name # this will basically takes the chunks of the data and make use if openai embeddings to
# comeback to us with the text converted to embedings,


# The vectorDBQA will be deprecated in the upcomming months

QA = VectorDBQA.from_chain_type(llm = OpenAI(),chain_type='stuff',vectorstore = docsearch)
Query = "What is a vector database ? give me a 15 word answer for a beginer  "
result = QA({'query':Query})
# The result will have the answer documnet of vector Database.
