from flask import Flask, jsonify
from flask import request
from flask_cors import CORS 
import sys
sys.path.append(r'c:\Users\mumer\Desktop\Anaconda\REST_API')
import notebook

app = Flask(__name__)

CORS(app)

@app.route('/api/my_function', methods=['GET'])
def api_my_function():
    result0 = list(notebook.avg_Estimated_Salary())
    result1 = list(notebook.avg_age_who_Exited())
    result2 = list(notebook.avg_age_who_Not_Exited())
    result3 = list(notebook.avg_Tenure())


    results_dict = {
        'avg_Estimated_Salary': result0,
        'avg_age_who_Exited': result1,
        'avg_age_who_Not_Exited': result2,
        'avg_Tenure': result3
    }

    # Convert the dictionary to JSON using jsonify
    return jsonify(results_dict)

if __name__ == '__main__':
    app.run(debug=True)
