document.getElementById('generate-btn').addEventListener('click', async () => {
    // console.log(
    //     document.getElementById('password-size'),
    //     document.getElementById('uppercase'),
    //     document.getElementById('numbers'),
    //     document.getElementById('special')
    //   );

    const passwordSize = document.getElementById('password-size').value;
    const includeUppercase = document.getElementById('uppercase').checked;
    const includeNumbers = document.getElementById('numbers').checked;
    const includeSpecial = document.getElementById('special').checked;
  
    const response = await fetch('http://127.0.0.1:5000/generate-password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        password_size: parseInt(passwordSize),
        include_uppercase: includeUppercase,
        include_numbers: includeNumbers,
        include_special: includeSpecial,
      }),
    });
  
    const data = await response.json();
  
    document.getElementById('password').value = data.password || 'Error generating password!';
});

document.getElementById('copy-btn').addEventListener('click', () => {
    console.log("botão clicado");


    const passwordField = document.getElementById('password');
    if (passwordField.value) {
      passwordField.select();
      document.execCommand('copy');
      alert('Password copied to clipboard!');
    } else {
      alert('No password to copy!');
    }
});