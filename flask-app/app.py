from flask import Flask

# Create a Flask web app
app = Flask(__name__)

# Define a route and a function to handle it
@app.route('/')
def hello_world():
    return 'Hi Payal. This is your first docker file.'

# Run the app on IP '0.0.0.0' and port 5000 if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

