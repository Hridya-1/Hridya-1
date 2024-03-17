function checkPasswordStrength() {
  var password = document.getElementById("password").value;
  
  $.ajax({
      url: '/generate_password',
      type: 'GET',
      data: { password: password },
      success: function(response) {
          document.getElementById("result").innerText = response.strength;
      },
      error: function(xhr, status, error) {
          console.error('Error:', error);
      }
  });
}