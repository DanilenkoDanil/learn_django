import requests 

url = 'https://api.openai.com/v1/completions'

headers = {"Content-Type" : "application/json", "Authorization": "Bearer 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",
           "OpenAI-Organization" : "org-2igIgsJTyFbvyc4j7Wgnw2sG" }

data = {"model": "text-davinci-003",
        "prompt": "КАк дела?",
        "max_tokens": 200,
        "temperature": 0}

print(requests.post(url, headers=headers, json=data).text)

#key: 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