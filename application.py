from flask import Flask, request, render_template
import utils
import config


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def index():
    user_data = request.form

    prediction = utils.get_prediction(user_data)

    return render_template('result.html', data=prediction)


if __name__ == '__main__':
    app.run('0.0.0.0', port= config.PORT_NUMBER, debug=True)