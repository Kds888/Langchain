import requests
import os 

# print(os.environ['proxycurl'])

# def scrape_linkedin_profile(linkedin_profile_url):
#     # we will create this function such that later on the langchain will decide whetehr to scrape information using this 
#     # function or not 
   

#     api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
#     api_key = os.environ(['proxycurl'])
#     header_dic = {'Authorization': 'Bearer ' + api_key}

#     response = requests.get(api_endpoint,
#                         params={'url': linkedin_profile_url},
#                         headers=header_dic)
    
#     # cleaning the data to remove all the unnecesary content from the response
#     data=response.json()
#     data ={
#         k:v
#         for k,v in data.items()
#         if v not in([],"","",None) and k not in ['people_also_viewed','certifications']
#     }
    
#     if data.get('groups'):
#         for a in data.get('groups'):
#             a.pop("profile_pic_url")

#     return data 

def get_info_from_linkedin(profile_id): # currently we are making use pf profile Id but in order for this application to be successfull we need that
    # we can just give it a name and it returns us back with all the information that we are asking from the agent
    url = "https://linkedin-profiles-and-company-data.p.rapidapi.com/profile-details"

    payload = {
        "profile_id": f"{profile_id}",
        "profile_type": "personal",
        "contact_info": False,
        "recommendations": False,
        "related_profiles": False
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "YOUR API KEY HERE",
        "X-RapidAPI-Host": "linkedin-profiles-and-company-data.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    data=response.json()
    data ={
            k:v
            for k,v in data.items()
            if v not in([],"","",None) and k not in ['people_also_viewed','certifications']
        }
        
    if data.get('groups'):
        for a in data.get('groups'):
            a.pop("profile_pic_url")

    return data 
# Using rapid api , will need to learn high skilled web scraping tool.

