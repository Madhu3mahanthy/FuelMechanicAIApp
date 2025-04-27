// Handle fuel request form submission
document.getElementById('fuel-request-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const location = document.getElementById('location').value;
    const fuelType = document.getElementById('fuel-type').value;
    const amount = document.getElementById('amount').value;
    
    // Send data to server (Flask backend)
    fetch('http://localhost:5000/fuel_request', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, location, fuel_type: fuelType, amount })
    })
    .then(response => response.json())
    .then(data => alert(data.message));
});
