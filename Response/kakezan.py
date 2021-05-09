from flask import Flask, request

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時 --- (*1)
@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "GET":
        return """
        <html><body>
        <form action="/" method="POST">
        <input type="text" name="a"> ×
        <input type="text" name="b">
        <input type="submit" value="計算">
        </form>
        """
    else: # POST時
        a = int(request.form.get("a"))
        b = int(request.form.get("b"))
        r = a * b
        return """
        <html><body>
        答えは{}です。
        <form action="/" method="POST">
        <input type="text" name="a"> ×
        <input type="text" name="b">
        <input type="submit" value="計算">
        </form>
        """.format(str(r))
 
# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True)
