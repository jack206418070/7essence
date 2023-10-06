from flask import Flask, render_template


app = Flask(
    __name__,
    static_folder='public',
    static_url_path='/'
)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

app.run(port=5525)