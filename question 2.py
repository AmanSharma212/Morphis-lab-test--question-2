from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    """Runs the 'top' command and returns its output."""
    try:
        return subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER", "codespace")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = get_top_output().replace("\n", "<br>")

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
    <h4>TOP output:</h4>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
