from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Lab Task: Static Analysis</h1><p>Visit /hello?name=yourname</p>"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    # Codacy is line par 'Security Issue' nikalega (XSS vulnerability)
    return render_template_string(f"<h1>Hello {name}!</h1>")

if __name__ == '__main__':
    app.run(debug=True)
