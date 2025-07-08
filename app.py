
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Get OpenAI API key from environment variable
openai.api_key = os.environ.get("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")

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    data = request.get_json()
    syllabus = data['syllabus']
    time_left = data['time_available']

    prompt = f"""
    You are an exam coach.
    A student has the following syllabus:

    {syllabus}

    They have {time_left} to revise.
    Create a detailed, daily/hourly smart study plan including:
    - Prioritized topics
    - Time allocations
    - Breaks
    - Tips
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful exam coach AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        plan = response['choices'][0]['message']['content'].strip()
        return jsonify({"plan": plan})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
