import tweepy, random, string, json
from flask import jsonify, Flask, request
import env_variables
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/post", methods=['POST', "GET"])
def post_a_tweet():
    #
    #  https://stackoverflow.com/questions/76810100/how-do-i-fix-403-forbidden-error-when-using-tweepy-to-access-the-twitter-api
    #
    # Authenticate to Twitter
    client = tweepy.Client(
    consumer_key=env_variables.api_key,
    consumer_secret=env_variables.api_key_secret,
    access_token=env_variables.access_token,
    access_token_secret=env_variables.access_token_secret
)

    data = request.get_json()
    print("print: ", data)

    lista = []
    for i in data.keys():
        #print(data[i])
        lista.append(data[i])

    #print(lista)

    timestamp = str(lista[0])
    source_ip = str(lista[1])
    country = str(lista[2])

    #print(timestamp, source_ip, country)

    code = get_random_string(8)
    
    try:
        # Post Tweet
        message = "### UPDATE FOR @ferna2909 ###, TIMESTAMP: {}, SOURCE_IP: {}, COUNTRY: {}, CODE: {}".format(timestamp, source_ip, country, code)
        client.create_tweet(text=message)
        return jsonify({ "status": 200, "message": message })

    except Exception as error: 
        return jsonify({ "status": 400, "error": error })

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)