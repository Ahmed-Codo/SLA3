from flask import Flask, request, jsonify
from openai import OpenAI

# إعداد الاتصال بـ OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_case():
    data = request.get_json()
    case_text = data.get("text", "")

    # إرسال النص إلى نموذج DeepSeek
    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {"role": "user", "content": f"ما الحكم القانوني أو نوع القضية في النص التالي: {case_text}"}
        ]
    )

    result = completion.choices[0].message.content
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
