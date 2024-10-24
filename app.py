from flask import Flask, request, jsonify
from ast_logic import create_rule_ast, evaluate_ast
from db import store_rule, get_rule
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule')
    rule_id = request.json.get('rule_id')

    ast = create_rule_ast(rule_string)
    store_rule(rule_id, ast)

    return jsonify({"message": "Rule created successfully!"})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    rule_id = request.json.get('rule_id')
    user_data = request.json.get('user_data')

    rule = get_rule(rule_id)
    ast = rule['ast']  # Load the AST from the database

    result = evaluate_ast(ast, user_data)  # Evaluate the AST against user data

    return jsonify({"eligible": result})

if __name__ == '__main__':
    app.run(port=5000,debug=True)