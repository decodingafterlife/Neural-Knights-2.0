# server.py

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def run_test_script():
    result = subprocess.run(['python', 'test.py'], capture_output=True, text=True)
    output = result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
