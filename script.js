document.getElementById('rule-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const rule = document.getElementById('rule').value;
    const rule_id = document.getElementById('rule_id').value;

    fetch('http://localhost:5000/create_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule, rule_id })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
});

document.getElementById('eval-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const rule_id = document.getElementById('eval-rule-id').value;
    const user_data = JSON.parse(document.getElementById('user-data').value);

    fetch('http://localhost:5000/evaluate_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule_id, user_data })
    })
    .then(response => response.json())
    .then(data => alert("Eligible: " + data.eligible))
    .catch(error => console.error('Error:', error));
});