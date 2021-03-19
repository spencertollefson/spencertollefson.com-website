import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder, StandardScaler

# from sklearn.externals import joblib
# model = joblib.load(open('./stat_models/catboost_month_incident_12.06.2018.joblib', 'rb'))
model = joblib.load(open('./web_app/stat_models/catboost_month_incident_20181206_updated_pkl_v_on_20210319.joblib', 'rb'))



def make_prediction(features):
    '''
    :param features: dictionary like 'example' above
    :return: 2 pair dict of binary outcome (compensate and not compensate) and the probablity
    '''
    X = pd.DataFrame(data=features, index=[0])

    categorical = ['airport_code', 'airline', 'claim_type', 'claim_site', 'Month_inc_date']
    continuous = ['days_waited_to_file_claim']

    trans_dir = './stat_models/transformers'
    enc = joblib.load(f'{trans_dir}/onehotencode.joblib')
    onehotarray = enc.transform(X[categorical])

    ss = joblib.load(f'{trans_dir}/standardscaler.joblib')
    continuousarray = ss.transform(X[continuous])

    mlb = joblib.load(f'{trans_dir}/item_category.joblib')
    onehot_itemcategories = mlb.transform(X['item_category'].str.replace(' ', '').str.split(pat=';'))

    X = np.concatenate((onehotarray, continuousarray, onehot_itemcategories), axis=1)

    prob_receive_compensation = model.predict_proba(X)[0, 1]

    result = prob_receive_compensation

    # result = {
    #     'compensation': int(prob_receive_compensation > 0.5),
    #     'prob_receive_compensation': prob_receive_compensation
    # }

    return result

def make_prediction_over_n_days(features, n_days):
    local_features = features.copy()
    results = []
    for day_num in range(1, n_days + 1):
        local_features['days_waited_to_file_claim'] = day_num
        results.append(make_prediction(local_features))

    result_array = np.array(results)
    max_index = np.argmax(result_array)

    max_prob = str(round(result_array[max_index], 3) * 100)[:4] + '%'

    response = {
        'max_prob': max_prob,
        'best_day': int(max_index + 1),
        'probs': results
    }
    print(response)
    return response


example = {
  'airport_code': 'SEA',  # str
  'airline': 'Delta Air Lines',    # str
  'claim_type': 'PropertyLoss',    # str
  'claim_site': 'Checkpoint',  # str
  'item_category': 'Clothing',  # str
  'days_waited_to_file_claim': 7,  # int
  'Month_inc_date': '1'  # int (1-12)
}

if __name__ == '__main__':
    print(make_prediction_over_n_days(example, 7))
