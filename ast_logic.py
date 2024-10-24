import re

class Node:
    def _init_(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # "operator" or "operand"
        self.value = value
        self.left = left
        self.right = right

def parse_condition(condition):
    match = re.match(r"(\w+)\s*([><=]+)\s*(\d+)", condition)
    if match:
        key, operator, value = match.groups()
        return {"key": key, "operator": operator, "value": int(value)}

def create_rule_ast(rule_string):
    if "AND" in rule_string:
        left, right = rule_string.split(" AND ", 1)
        return Node(node_type="operator", value="AND", left=create_rule_ast(left), right=create_rule_ast(right))
    elif "OR" in rule_string:
        left, right = rule_string.split(" OR ", 1)
        return Node(node_type="operator", value="OR", left=create_rule_ast(left), right=create_rule_ast(right))
    else:
        return Node(node_type="operand", value=parse_condition(rule_string))

def evaluate_ast(node, data):
    if node.node_type == "operand":
        condition = node.value
        key = condition["key"]
        operator = condition["operator"]
        value = condition["value"]
        user_value = data.get(key)
        
        if operator == ">":
            return user_value > value
        elif operator == "<":
            return user_value < value
        elif operator == "=":
            return user_value == value
    elif node.node_type == "operator":
        if node.value == "AND":
            return evaluate_ast(node.left, data) and evaluate_ast(node.right, data)
        elif node.value == "OR":
            return evaluate_ast(node.left, data) or evaluate_ast(node.right, data)