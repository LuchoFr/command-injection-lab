
from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

HTML= """
<!doctype html>
<html>
<head>
    <title>Command Ijenction Incoming!</title>
</head>
<body>
    <h1>km0d3 Ping Tool Lab - Please insert your ip and ill pin you</h1>

    <form method="POST">
        <label>IP o dominio:</label>
        <input name="target" placeholder="127.0.0.1">
        <button type="submit">Ping</button>
    </form>

    {% if command %}
        <h2>Comando ejecutado:</h2>
        <pre>{{ command }}</pre>
    {% endif %}

    {% if output %}
        <h2>Resultado:</h2>
        <pre>{{ output }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    command = None
    output = None

    if request.method == "POST":
        target = request.form.get("target", "")

        # VULNERABLE A PROPÓSITO:
        # Estamos concatenando input del usuario dentro de un comando de shell.
	#De esta manera si colocaramos un pin y luego un ";" podriamos concatenar comandos
        command = f"ping -c 4 {target}"

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr

    return render_template_string(
        HTML,
        command=command,
        output=output
    )

if __name__ == "__main__":
    app.run(debug=True)

