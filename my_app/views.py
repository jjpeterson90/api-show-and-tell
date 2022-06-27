from django.shortcuts import render
import requests, json

# Create your views here.
def index(request):
    
    test_api_url = "https://api.gfycat.com/v1/gfycats/meeksadannashummingbird"
    
    TOKEN = get_token()
    print(TOKEN)
    
    api_call_headers = { 'Authorization': 'Bearer ' + TOKEN }
    api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
    
    json_response = api_call_response.json()
    print(json_response)
    
    url = json_response['gfyItem']['content_urls']['100pxGif']['url']
    print(url)
    data = { 'url' : url }
    
    return render(request, 'my_app/index.html', data)

def get_token():
    TOKEN_URL = "https://api.gfycat.com/v1/oauth/token"
    CLIENT_ID = 'x' # received after signing up with an account
    CLIENT_SECRET = 'x' # received after signing up with account
    
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{"client_id":"x", "client_secret": "x", "grant_type": "client_credentials"}'

    token_response = requests.post(TOKEN_URL, headers=headers, data=data)
    
    mytoken = token_response.json()
    
    print(mytoken)
    
    token = mytoken['access_token']
    
    return token