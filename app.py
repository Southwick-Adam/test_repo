import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

def loadBikes():
    load_dotenv()
    apiKey = os.getenv('bike_key')
    contract = 'Dublin'
    apiRequest = requests.get(f'https://api.jcdecaux.com/vls/v1/stations?contract={contract}&apiKey={apiKey}')
    print(apiRequest.status_code)
    f = open("test_repo/dockInfo.json", "w")
    f.write(apiRequest.text)
    f.close()

if __name__ == "__main__":
    app.run(debug=True)
    loadBikes()
