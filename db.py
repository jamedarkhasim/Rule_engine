
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['rule_engine_db']
rules_collection = db['rules']

def store_rule(rule_id, ast):
    rule_data = {
        "rule_id": rule_id,
        "ast": ast_to_dict(ast)  # Store the AST as a dictionary
    }
    rules_collection.insert_one(rule_data)

def get_rule(rule_id):
    return rules_collection.find_one({"rule_id": rule_id})

def ast_to_dict(node):
    if not node:
        return None
    return {
        "node_type": node.node_type,
        "value": node.value,
        "left": ast_to_dict(node.left),
        "right": ast_to_dict(node.right)
    }