import requests

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

headers = {
	"x-rapidapi-key": "701c7df520msh3aced452a67326ep1f26f2jsn40c63f9fb446",
	"x-rapidapi-host": "chatgpt-best-price.p.rapidapi.com",
	"Content-Type": "application/json"
}

def userinput(prompt):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    output = result['choices'][0]['message']['content']
    return output

while True:
    prompt = input('\nM: ')
    print(userinput(prompt))

    if prompt == 'Keluar':
        print('\nProgram telah berhenti, terimakasih telah menggunakan program kami ^_^')
        break