// Handle login form submission
document.getElementById('login-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;

  const data = { username, password };

  fetch('http://localhost:5000/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert('Login successful!');
      showTab('fuelRequest'); // Go to fuel request form after login
    } else {
      alert('Login failed: ' + data.message);
    }
  })
  .catch(error => console.error('Error:', error));
});

// Handle signup form submission
document.getElementById('signup-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const username = document.getElementById('signup-username').value;
  const password = document.getElementById('signup-password').value;

  const data = { username, password };

  fetch('http://localhost:5000/signup', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert('Signup successful!');
      showTab('login'); // Go to login form after signup
    } else {
      alert('Signup failed: ' + data.message);
    }
  })
  .catch(error => console.error('Error:', error));
});

// Handle fuel request form submission
document.getElementById('fuel-request-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const vehicleType = document.getElementById('vehicle-type').value;
  const currentFuel = document.getElementById('current-fuel').value;
  const desiredDistance = document.getElementById('desired-distance').value;

  const data = { vehicle_type: vehicleType, current_fuel_level: currentFuel, desired_distance: desiredDistance };

  fetch('http://localhost:5000/predict_fuel', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    alert(data.message); // Show response message
  })
  .catch(error => console.error('Error:', error));
});

// Handle mechanic request form submission
document.getElementById('mechanic-request-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const issue = document.getElementById('mechanic-issue').value;

  const data = { issue };

  fetch('http://localhost:5000/mechanic_request', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    alert(data.message + ' Mechanic: ' + data.mechanic.name);  // Show mechanic info
  })
  .catch(error => console.error('Error:', error));
});

// Handle logout form submission
document.getElementById('logout-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const username = document.getElementById('logout-username').value;

  const data = { username };

  fetch('http://localhost:5000/logout', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert('Logout successful!');
      showTab('login'); // Show login form after logout
    } else {
      alert('Logout failed: ' + data.message);
    }
  })
  .catch(error => console.error('Error:', error));
});

function showTab(tabName) {
  // Show the specific form
  const forms = ['login', 'signup', 'fuelRequest', 'mechanicRequest', 'logout'];
  forms.forEach(form => {
    document.getElementById(form + '-container').style.display = (form === tabName) ? 'block' : 'none';
  });
}
