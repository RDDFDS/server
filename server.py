from flask import Flask, render_template_string
import os, platform, socket, psutil

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>System Info</title>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: consolas;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .container {
            border: 2px solid white;
            padding: 10px;
            text-align: left;
            max-width: 90vw;
            max-height: 90vh;
            overflow: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body>
    <div class='container'>
        <pre>{{ info }}</pre>
    </div>
</body>
</html>
"""

@app.route('/')
def system_info():
    info = {
        "username": "raphael00",
        "id": "9031901",
        "name": "Unknown",
        "system": platform.system(),
        "version": platform.version(),
        "architecture": platform.architecture(),
        "processor": platform.processor(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "local_sharing": os.path.expanduser("~"),
        "cpu_count": psutil.cpu_count(logical=True),
        "cpu_freq": psutil.cpu_freq().max,
        "total_memory": psutil.virtual_memory().total,
        "available_memory": psutil.virtual_memory().available,
        "disk_usage": psutil.disk_usage('/')._asdict()
    }
    return render_template_string(HTML_TEMPLATE, info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
