from flask import Flask, request, jsonify
from google import generativeai as genai

# إعداد مفتاح Gemini
genai.configure(api_key="AIzaSyDmU2uz14prsUgfEALGqJM-y8xVzo8IpZU")  # ← ضع مفتاحك هنا

app = Flask(__name__)

@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "الرجاء إرسال نص للتحليل"}), 400
    text = data["text"]

    print("Received text:", text)  # إضافة طباعة للنص المرسل

    if not text.strip():
        return jsonify({"error": "النص المرسل فارغ"}), 400

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"اقرأ هذا النص وحلله أو لخصه:\n{text}"
        )
        return jsonify({"result": response.text})

    except Exception as e:
        return jsonify({"error": f"حدث خطأ أثناء التحليل: {e}"}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
