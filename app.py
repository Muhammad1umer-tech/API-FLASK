from flask import Flask, jsonify
from flask_cors import CORS 
import notebook
app = Flask(__name__)

CORS(app)

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

        # Convert the dictionary to JSON using jsonify
        return jsonify(results_dict)

    except Exception as e:
        # Handle the exception and return an error response
        error_message = str(e)
        return jsonify({'error': error_message}), 500  # You can choose an appropriate HTTP status code for the error

if __name__ == '__main__':
    app.run(debug=True)
