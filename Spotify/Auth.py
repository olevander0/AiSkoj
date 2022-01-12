import requests
import datetime
import base64
client_id = '1682ad452d574bf983910acf8789b5e8'
client_secret = 'f4fc8deea17e4daab4db70cd72392b57'

# lookup for token for future requests

client_creds = f"{client_id}:{client_secret}"

client_creds_b64 = base64.b64encode(client_creds.encode())

token_url = 'https://accounts.spotify.com/api/token'
method = 'POST'

token_data = {
    "grant_type": "client_credentials"
}

token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}"
}

r = requests.post(token_url, data=token_data, headers=token_headers)
valid_request = r.status_code in range(200, 299)

if valid_request:
    token_response_data = r.json()
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in']
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now
