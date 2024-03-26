from flask import Flask, render_template,request, jsonify,render_template_string
import json
import pandas as pd
import joblib
import flask
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# with open(f'mlmodels/housing-price-model.pkl', 'rb') as file1:
#     model = joblib.load(file1)
# with open(f'mlmodels/scaler.pkl', 'rb') as file2:
#     loaded_scaler = joblib.load(file2)

@app.route('/')
def home():
    return render_template ('index1.html')


@app.route('/action', methods=['POST','GET'])
def action():
    # with open('/templates/index1.html', 'r') as file:
    #     html_content = file.read()

    # Load in variables again because flask sucks
    zip_series = pd.read_csv('./csvfiles/zip_series.csv')
    city_series = pd.read_csv('./csvfiles/city_series.csv')
    unique_states_df = pd.read_csv('./csvfiles/unique_states_df.csv')   
    loaded_scaler = joblib.load('./mlmodels/scaler.pkl')
    model = joblib.load('./mlmodels/housing-price-model.pkl')

    #get user input variables from the form on website
    if flask.request.method == 'POST':
        Beds = request.form.get('Beds')
        Bath = request.form.get('Bath')
        Acre_lot = request.form.get('acre_lot')
        City = request.form.get('City')
        State = request.form.get('State')
        zipcode = request.form.get('zipcode')
        House_size = request.form.get('House_Size')

    #Store the data in a dictionart
    data = {
    "bed": [Beds],
    "bath": [Bath],
    "acre_lot": [Acre_lot],
    "city": [City],
    "state": [State],
    "zip_code": [zipcode],
    "house_size": [House_size]}

     # Convert the dictionary to JSON format
    usersearch_df = pd.DataFrame(data)
    usersearch_df.to_csv('csvfiles/Usersearch.csv', index=False, header=True)
    # convert state and city to title case
    usersearch_df['city'] = usersearch_df['city'].str.title()
    usersearch_df['state'] = usersearch_df['state'].str.title()
    
    # read in city and zip csv files
    zip_series = zip_series.copy(deep=True)
    city_series = city_series.copy(deep=True)

    # convert to a series
    city_series.set_index('Unnamed: 0', inplace=True)
    city_series = city_series['city']
    try:
        # convert to city count
        usersearch_df[['city']] = city_series.loc[usersearch_df['city'].iloc[0]]
    except:
        # if city not in training data, replace with 1
        city = usersearch_df['city'].iloc[0]
        print(f'Model has never seen “{city}” before. Estimate may be inaccurate.')
        usersearch_df['city'] = 1
    
    unique_states_df['city'] = unique_states_df['city'].apply(lambda x: int(x == 0))
    # add row to unique df
    new_df = pd.concat([unique_states_df, usersearch_df])

    # create encoder
    ohe = OneHotEncoder(handle_unknown='ignore', sparse_output= False).set_output(transform= 'pandas')
    ohetransform = ohe.fit_transform(new_df[['state']])
    new_df = pd.concat([new_df, ohetransform], axis=1).drop(['state'], axis=1)
    new_df = loaded_scaler.transform(new_df)
    prediction = model.predict([new_df[0]])[0]
    prediction = "${:,.2f}".format(prediction)

    return render_template('index1.html', result = f'The estimate price is "{prediction}".')
    # return render_template_string(html_content)

if __name__ == '__main__':
    app.run(port=5018, debug=True)