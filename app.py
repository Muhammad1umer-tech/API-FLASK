from flask import Flask, request, jsonify
from flask_cors import CORS 
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import keras
import notebook
app = Flask(__name__)

CORS(app)

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def api_post():
    try:
        request_data = request.get_json()

        user_data = {}

        user_data['CreditScore'] = int(request_data.get("CreditScore", 0))
        user_data['Age'] = int(request_data.get("Age", 0))
        user_data['Tenure'] = float(request_data.get("Tenure", 0))
        user_data['Balance'] = float(request_data.get("Balance", 0))

        user_data['HasCrCard'] = float(request_data.get("HasCrCard", 0))
        user_data['IsActiveMember'] = float(request_data.get("IsActiveMember", 0))
        user_data['EstimatedSalary'] = float(request_data.get("EstimatedSalary", 0))


        gen = request_data.get("Gender", "")

        if(gen  == 'Male'):
            user_data['Male'] = 1 
            user_data['Female'] = 0 
        
        if(gen == 'Female'):
            user_data['Male'] = 0 
            user_data['Female'] = 1


        if(int(request_data.get("NumOfProducts", 0) == 1)):
            user_data['NumOfProducts_1'] = 1 
            user_data['NumOfProducts_2'] = 0 
            user_data['NumOfProducts_3'] = 0 
            user_data['NumOfProducts_4'] = 0 

        elif(int(request_data.get("NumOfProducts", 0) == 2)):
            user_data['NumOfProducts_1'] = 0
            user_data['NumOfProducts_2'] = 1 
            user_data['NumOfProducts_3'] = 0 
            user_data['NumOfProducts_4'] = 0 

        elif(int(request_data.get("NumOfProducts", 0) == 3)):
            user_data['NumOfProducts_1'] = 0
            user_data['NumOfProducts_2'] = 0 
            user_data['NumOfProducts_3'] = 1 
            user_data['NumOfProducts_4'] = 0 

        elif(int(request_data.get("NumOfProducts", 0) == 4)):
            user_data['NumOfProducts_1'] = 0
            user_data['NumOfProducts_2'] = 0 
            user_data['NumOfProducts_3'] = 0 
            user_data['NumOfProducts_4'] = 1 
           
       

        geo = request_data.get("Geography", "") 
        if(geo == 'France'):
            user_data['France'] = 1
            user_data['Spain'] = 0
            user_data['Germany'] = 0 

        elif(geo == 'Spain'):
            user_data['France'] = 0 
            user_data['Spain'] = 1
            user_data['Germany'] = 0 
         
        elif(geo  == 'Germany' ):
            user_data['France'] = 0 
            user_data['Spain'] = 0
            user_data['Germany'] = 1 
       

        new_row_df = pd.DataFrame([user_data])

        model = keras.models.load_model('new_model.h5')
        df = pd.read_csv("New_df.csv")
        scaler = MinMaxScaler()

        df_scaled = scaler.fit_transform(df)

        single_test_scaled = scaler.transform(new_row_df)
        pre = model.predict(single_test_scaled)

        if(pre>=0.5):
            return jsonify("1")
        else:
            return jsonify("0")

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/', methods=['GET'])
def api_my_function():
    try:
        result0 = list(notebook.avg_Estimated_Salary())
        result1 = list(notebook.avg_age_who_Exited())
        result2 = list(notebook.avg_age_who_Not_Exited())
        result3 = list(notebook.avg_Tenure())

        results_dict = {
            'avg_Estimated_Salary1': result0,
            'avg_age_who_Exited': result1,
            'avg_age_who_Not_Exited': result2,
            'avg_Tenure': result3
        }

        return jsonify(results_dict)

    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500 

if __name__ == '__main__':
    app.run(debug=True)
