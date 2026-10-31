from flask import Flask, render_template, request, redirect

app = Flask(__name__)
expenses = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        amount = request.form.get("amount")
        category = request.form.get("category")

        if name and amount and category:
            try:
                amount = float(amount)
                expenses.append({
                    "name": name,
                    "amount": amount,
                    "category": category
                })
            except ValueError:
                pass

        return redirect("/")

    return render_template("index.html", expenses=expenses)


if __name__ == "__main__":
    app.run(debug=True)
