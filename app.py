from flask import Flask, request, jsonify
from flask_cors import CORS 
import notebook
app = Flask(__name__)

CORS(app, origins="*")


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
