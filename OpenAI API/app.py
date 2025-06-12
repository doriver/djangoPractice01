from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI()

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    gpt_text = None
    image_url = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            # 1. GPT-4 Turbo로 텍스트 생성
            chat_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "넌 이미지 설명을 잘 해주는 도우미야."},
                    {"role": "user", "content": f"'{prompt}'에 대한 설명을 최대한 짧게."}
                ],
                temperature=0.7,
                max_tokens=300
            )
            gpt_text = chat_response.choices[0].message.content
            # 2. DALL·E 3로 이미지 생성
            image_response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            image_url = image_response.data[0].url
        except Exception as e:
            gpt_text = f"오류 발생: {str(e)}"
    return render_template("index.html", prompt=prompt, gpt_text=gpt_text, image_url=image_url)
if __name__ == "__main__":
    app.run(debug=True)