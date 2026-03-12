#!/usr/bin/env python3

import http.server
import socketserver
import os #This allows us to read Environment Variables

#!/usr/bin/env python3

import os # HARD RULE: Needed for getenv
import http.server
import socketserver

# --- THE DYNAMIC PART ---

# SOFT CHOICE: 'APP_COLOR' is the key. 'navy' is the default value.
# HARD RULE: os.getenv must be used to read from the environment.
my_color = os.getenv("APP_COLOR", "navy")

# SOFT CHOICE: 'html_content' is just a variable name. 
# SOFT CHOICE: You can change the CSS/HTML inside the triple quotes.
# HARD RULE: {my_color} must be inside the f-string to work.
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Amazon Service</title>
    <style>
        body {{ font-family: sans-serif; background-color: {my_color}; color: white; text-align: center; padding: 50px; }}
        .btn {{ background-color: #febd69; color: black; padding: 10px 20px; border-radius: 4px; cursor: pointer; }}
    </style>
</head>
<body>
    <h1>Amazon Search Engine</h1>
    <p>Environment: <span style="font-weight:bold;">{my_color.upper()}</span></p>
    <input type="text" placeholder="Search...">
    <button class="btn">Search</button>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

# --- THE SERVER PART ---

PORT = 80
Shashi_Logic = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Shashi_Logic) as httpd:
    print(f"Server is LIVE with color: {my_color}")
    httpd.serve_forever()
