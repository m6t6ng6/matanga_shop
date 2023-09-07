import tweepy, random, string
from flask import jsonify, Flask, render_template
import env_variables

app = Flask(__name__)

@app.route("/post")
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

    code = get_random_string(8)
    
    try:
        # Post Tweet
        message = str("test 5" + ", codigo: " + code)
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