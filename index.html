<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My API Frontend</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .container {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>API Test Interface</h1>
        <button onclick="getData()">Get Data</button>
        <div id="result" class="result">Results will appear here...</div>
    </div>

    <script>
        async function getData() {
            const resultDiv = document.getElementById('result');
            try {
                // Replace with your Railway API URL
                const response = await fetch('https://checkersgpt-production.up.railway.app/api/data', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        // Enable CORS from GitHub Pages
                        'Access-Control-Allow-Origin': '*'
                    }
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
            } catch (error) {
                resultDiv.innerHTML = `Error: ${error.message}`;
                console.error('Error:', error);
            }
        }
    </script>
</body>
</html>
