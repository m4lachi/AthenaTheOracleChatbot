from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
import json

# Create Flask app
app = Flask(__name__)

print("Loaded key (first 8 chars):", os.getenv("OPENAI_API_KEY")[:8])


# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    # Serve the index.html file
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        user_question = data.get("question", "")

        if not user_question:
            return jsonify({"error": "No question provided"}), 400

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # small, fast model for workshop
            messages=[
                {"role": "system", "content": "You are Athena, goddess of wisdom, answering in a myth-inspired, helpful style. Keep your answers concise and under 3 sentences."},
                {"role": "user", "content": user_question}
            ]
        )

        answer = response.choices[0].message.content
        return jsonify({"answer": answer})

    except Exception as e:
        # Always return JSON instead of HTML error pages
        print("Error in /ask:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
