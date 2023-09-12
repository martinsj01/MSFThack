from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    # Fetch and process your social media insights here
    # You can pass them into your template as variables
    insights = fetch_insights()
    return render_template('dashboard.html', insights=insights)

def fetch_insights():
    # Placeholder function for fetching your insights
    # Replace this with your actual function
    return {}

if __name__ == '__main__':
    app.run(debug=True)
