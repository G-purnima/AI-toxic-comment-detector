from flask import Flask, request, jsonify, render_template

from predict import predict_comment
import os

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Text input is missing"}), 400

    print("🔍 Received text:", data["text"])
    result = predict_comment(data["text"])

    toxic_prob = float(result.get("toxic_probability", 0.0))


    # 🔥 Severity + Moderation logic (YOUR FEATURE)
    if toxic_prob < 0.30:
        severity = "Clean"
        action = "Allow comment"
    elif toxic_prob < 0.50:
        severity = "Mild"
        action = "Hide comment"
    elif toxic_prob < 0.75:
        severity = "Moderate"
        action = "Warn user"
    else:
        severity = "Severe"
        action = "Block & report user"

    # Add new fields to response
    result["severity"] = severity
    result["moderation_action"] = action

    print("✅ Sending result with features:", result)
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render uses dynamic port
    app.run(debug=True, host='0.0.0.0', port=port)





