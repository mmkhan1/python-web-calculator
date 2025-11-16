from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        number1 = float(request.form.get("number1"))
        number2 = float(request.form.get("number2"))
        operation = request.form.get("operation")

        try:
            if operation == "add":
                result = number1 + number2
            elif operation == "subtract":
                result = number1 - number2
            elif operation == "multiply":
                result = number1 * number2
            elif operation == "divide":
                result = number1 / number2
        except ZeroDivisionError:
            result = "Error: Cannot divide by zero"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
