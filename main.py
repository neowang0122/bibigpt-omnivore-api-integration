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
    print("request success") 
    response_json = response.json()
    # print(response_json) 
    
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



# # Send the formatted text to OpenAI API for summarization with bullet points
# headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {openai_api_key}'}
# data = {
#     'prompt': formatted_text,
#     'max_tokens': 200,
#     'top_p': 1,
#     'frequency_penalty': 0,
#     'presence_penalty': 0
# }

# response = requests.post(openai_url, headers=headers, json=data)
# summary = response.json()['choices'][0]['text']

# # Print the summarized content with bullet points
# summary = summary.replace('\n', '• ')
# print(summary)