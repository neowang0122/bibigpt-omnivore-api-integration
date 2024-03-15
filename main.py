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

# TODO handle the multiple URLs 
user_input_url_list = user_input_url.split(",") 

# data to be sent to the api
data = {
    "url": user_input_url
}

headers = {
    "Content-Type": "application/json"
}

print("request sent\n") 
response = requests.post(bibigpt_subtitle_api, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    response_json = response.json()
    # print(response_json, "\n") 

    # Example response from the API 
    '''
    {'success': True, 'id': 'BV1ww411V7pT', 'service': 'bilibili', 'sourceUrl': 'https://www.bilibili.com/video/BV1ww411V7pT', 'htmlUrl': 'https://bibigpt.co/video/BV1ww411V7pT', 'costDuration': 153, 'remainingTime': 302852, 'detail': {'dbId': 'c99f66ba-4ad2-4c9e-ba60-8e3c127fefb1', 'id': 'BV1ww411V7pT', 'author': '淘沙博士', 'authorId': '289706107', 'embedId': '325520040', 'pageId': '1388652111', 'url': 'https://www.bilibili.com/video/BV1ww411V7pT', 'type': 'bilibili', 'title': '重磅数据出炉！经济“口红效应”显著，顺之者昌，逆之者亡！', 'chapters': [], 'cover': 'http://i2.hdslb.com/bfs/archive/27a4fd94a32b988db3d93673ef41fca51ac403a0.jpg', 'duration': 153, 'subtitlesArray': 
    '''

    # Extracting the desired information from the JSON response
    success = response_json.get('success')
    id = response_json.get('id')
    service = response_json.get('service')
    sourceUrl = response_json.get('sourceUrl')
    htmlUrl = response_json.get('htmlUrl')
    title = response_json.get('detail', {}).get('title')  # Accessing 'title' under 'detail'
    author = response_json.get('detail', {}).get('author')  # Accessing 'author' under 'detail'
    coverUrl = response_json.get('detail', {}).get('coverUrl')  # Accessing 'coverUrl' under 'detail'
    costDuration = response_json.get('costDuration')
    remainingTime = response_json.get('remainingTime')
    
    # Printing the extracted information
    print("Success:", success)
    print("ID:", id)
    print("Service:", service)
    print("Source URL:", sourceUrl)
    print("HTML URL:", htmlUrl)
    print("Title:", title)
    print("Author:", author)
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

