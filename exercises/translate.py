import requests
list1 = ['English','Luganda', 'Runyankole','Ateso','Lugbara','Acholi']
list_1 = ", ".join(list1)
source_language = input(f"Enter the language you want to translate from  eg ({list_1}):\n")
list2 = [n for n in list1 if n != source_language]
list_2 = ", ".join(list2)
if(source_language in list1):
    target_language = input(f"Enter the language you want to translate to eg ({list_2}) ; \n")
    if(target_language in list2):
        text_to_translate = input("Please input the text you want to translate\n")
        if source_language != target_language and source_language is not None and source_language is not None and text_to_translate is not None:
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
    else:
        print("Wrong Choice")
    
else:
    print("Wrong Choice")


 