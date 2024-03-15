'''
This is the main file to provide the features to request the user input and send it to bibigpt api. Once the response is received, it will send it to Omnivore.  
''' 


import requests
import openai
import json  

'''
API setup  
'''
# url for the bibigpt api
bibigpt_subtitle_api = "https://bibigpt.co/api/open/yNBgX86ao6JE/subtitle"
bibigpt_summary_api = "https://bibigpt.co/api/open/yNBgX86ao6JE"


# Asking the user to input the URL
user_input_url = input("Please enter the URL. For multiple URLs, separate them with a comma: ")
user_input_url_list = user_input_url.split(",") 

# data to be sent to the api
data = {
    "url": user_input_url
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(bibigpt_subtitle_api, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("request success\n") 
    response_json = response.json()
    # print(response_json, "\n") 

    # Extracting the desired information from the JSON response
    success = response_json.get('success')
    id = response_json.get('id')
    service = response_json.get('service')
    sourceUrl = response_json.get('sourceUrl')
    htmlUrl = response_json.get('htmlUrl')
    costDuration = response_json.get('costDuration')
    remainingTime = response_json.get('remainingTime')
    # Printing the extracted information
    print("Success:", success)
    print("ID:", id)
    print("Service:", service)
    print("Source URL:", sourceUrl)
    print("HTML URL:", htmlUrl)
    print("Cost Duration:", costDuration)
    print("Remaining Time:", remainingTime)
    print("\n") 

    # Extracting subtitlesArray
    subtitles = response_json.get('detail', {}).get('subtitlesArray', [])

    # Initializing an empty string for the transcript
    transcript = ""

    # Iterating over each subtitle in the array and appending it to the transcript string
    for subtitle in subtitles:
        text = subtitle.get('text', '')
        transcript += text + "\n"

    # Printing the formatted transcript
    print(transcript)

else:
    print("request failed.", response.status_code)

