import requests
    
def switcher(argument):
    switcher = {
        1: "English",
        2: "Luganda", 
        3: "Runyankole", 
        4: "Ateso", 
        5: "Lugbara",
        6: "Acholi"
    }
    return switcher.get(argument, None)


arg1 = input("""Enter the number of the language you want to translate from:
                 1. English
                 2. Luganda, 
                 3. Runyankole, 
                 4. Ateso, 
                 5. Lugbara
                 6. Acholi
                 \n""")
source_language = switcher(int(arg1))
arg2 = input("""Enter the number of the language you want to translate to :
                 1. English
                 2. Luganda, 
                 3. Runyankole, 
                 4. Ateso, 
                 5. Lugbara
                 6. Acholi
                 \n""")
target_language = switcher(int(arg2))
text_to_translate = input("Please input the text you want to translate\n")
if source_language != target_language and source_language is not None and source_language is not None:
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb21iYXRhbnQxMDEiLCJhY2NvdW50X3R5cGUiOiJGcmVlIiwiZXhwIjo0ODUxMjEwODExfQ.tovwVO_yfcSfO4hxhYHXRLe8MGeRKMeW5-7l5O1vOic"
    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
    "source_language": f"{source_language}",
    "target_language": f"{target_language}",
    "text": f"{text_to_translate}"
    }

    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

    if response.status_code == 200:
        translated_text = response.json()["text"]
        print("Translate text:", translated_text)
    else:
        print("Error:", response.status_code, response.text)
else:
    print(f"Wrong choice {source_language} and {target_language}")
    

 