
from langchain.serpapi import SerpAPIWrapper
import os 

# we are going to define a fucntion which may get called multiple times to look for the details of a person, for example if it is not able to look for 
# the name of the person for the first_time, the llm will keep on calling that function till we get what we want.
def get_profile_id(text):
    serpapi_api_key = os.environ['SERP_API_KEY'] # it will get the serp api key that it required for searching the web
    search = SerpAPIWrapper(serpapi_api_key=serpapi_api_key) # this api Tries to clean the data that is given to it automatically for us to be processed by the llm.
    # There is some problem with the SERPAPI return results that we have 
    res = search.run(f"{text}") 
    return res 


