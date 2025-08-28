from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = request.form['gender']
        seniorcitizen = int(request.form['seniorcitizen'])
        partner = request.form['partner']
        dependents = request.form['dependents']

        # Example simple rule-based prediction, replace with your model code
        if seniorcitizen == 1 and partner == "No":
            prediction = "Churn Likely"
        else:
            prediction = "Churn Unlikely"

        return render_template('home.html', prediction=prediction)
    except Exception as e:
        return render_template('home.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
