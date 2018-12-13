from flask import Flask, abort, render_template, jsonify, request
import joblib

from api import make_prediction, make_prediction_over_n_days

app = Flask('TSA-app')

month_dictionary = {
                    'January': '1',
                    'February': '2',
                    'March': '3',
                    'April': '4',
                    'May': '5',
                    'June': '6',
                    'July': '7',
                    'August': '8',
                    'September': '9',
                    'October': '10',
                    'November': '11',
                    'December': '12' 
}

@app.route('/predict_multiple', methods=['POST'])
def do_prediction_multiple_days():
    if not request.json:
        abort(400)
    data = request.json
    data['Month_inc_date'] = month_dictionary[data['Month_inc_date']]

    response = make_prediction_over_n_days(data, 50)

    return jsonify(response)


@app.route('/', methods=['GET'])
def dropdown():
    featuredir = './featurelists'
    airports = sorted(joblib.load(f'{featuredir}/airports.joblib'))
    airlines = sorted(joblib.load(f'{featuredir}/airlines.joblib'))
    claim_types = sorted(joblib.load(f'{featuredir}/claim_types.joblib'))
    claim_sites = sorted(joblib.load(f'{featuredir}/claim_sites.joblib'))
    item_cats = sorted(joblib.load(f'{featuredir}/item_category.joblib'))
    days = list(range(1, 61))
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    return render_template('index.html', airports=airports, airlines=airlines,
                           claim_types=claim_types, claim_sites=claim_sites,
                           item_cats=item_cats, days=days, months=months)

   
app.run(debug=True)
