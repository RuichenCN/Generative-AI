import os
import openai
import random
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Set your OpenAI API key
with open('api_key.txt', 'r') as file:
    openai.api_key = file.read().strip()

class Product:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class ProductCommentGenerator:
    def __init__(self):
        self.products = {}
        self.load_products()

    def load_products(self):
        try:
            with open('products.json', 'r') as file:
                self.products = json.load(file)
        except FileNotFoundError:
            print("Products file not found. Make sure you have a 'products.json' file with your product data.")

    def generate_comment(self, product_name, language='English'):
        product = self.products.get(product_name)
        if product:
            # You can adjust the prompt as needed for your specific use case
            prompt = f"Generate a 100-word comment about the {product_name}:\n{product['description']}\nThe response should use language {language}."
            print("This is my comment prompt:")
            print(prompt)
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=100,
                temperature=0.7
            )
            return response.choices[0].text.strip()
            
        else:
            return "Product not found."

class ChatGPTApp:
    def __init__(self):
        self.product_comment_generator = ProductCommentGenerator()

    def generate_email_subject(self, customer_comment,language='English'):
        # Use ChatGPT to infer the email subject from the customer's comment
        prompt = f"Infer the email subject based on the customer's comment :\n{customer_comment}\n\
            The response should use language {language}. Word limit: 10."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100,  # Adjust the max tokens as needed
            temperature=0.7
        )
        return response.choices[0].text.strip()

    def generate_summary(self, customer_comment, language='English'):
        # Use ChatGPT to generate a summary of the customer's comment
        prompt = f"Summarize the following customer comment:\n{customer_comment}\n\
            The response should use language {language}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200,  # Adjust the max tokens as needed
            temperature=0.7
        )
        return response.choices[0].text.strip()

    def analyze_sentiment(self, customer_comment, language='English'):
        # Use ChatGPT to analyze the sentiment of the customer's comment
        prompt = f"Analyze the sentiment of the following customer comment:\n{customer_comment}\n\
            The response should use language {language}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=30,  # Limit the response to a single token (positive, negative, neutral)
            temperature=0.7
        )
        sentiment = response.choices[0].text.strip().lower()

        if "positive" in sentiment:
            return "Positive"
        elif "negative" in sentiment:
            return "Negative"
        else:
            return "Neutral"

    def generate_email(self, comment, subject, summary, sentiment, language='English'):
        # Use ChatGPT to generate an email response
        prompt = (f"Given the customer's comment: '{comment}', "
                        f"its summary: '{summary}', its sentiment: '{sentiment}', "
                        f"and the email subject: '{subject}',please craft an email response \
                            in 100 words or less. The response should use language {language}.")
        print("This is my email prompt:")
        print(prompt)
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=400,  # Adjust the max tokens as needed
            temperature=0.7
        )
        return response.choices[0].text.strip()

selected_language = "English"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_comment', methods=['POST'])
def generate_comment():
    global selected_language
    chatGptApp = ChatGPTApp()
    selected_language = request.form.get('language')
    print("This is language1:")
    print(selected_language)

    products = chatGptApp.product_comment_generator.products
    # Select a random product and generate a comment
    random_product = random.choice(list(products.keys()))
    comment = chatGptApp.product_comment_generator.generate_comment(random_product, selected_language)
    return jsonify({'comment': comment})

@app.route('/generate_email', methods=['POST'])
def generate_email():
    global selected_language
    chatGptApp = ChatGPTApp()
    comment = request.form.get('comment')
    # selected_language = request.form.get('language')
    print("This is language2:")
    print(selected_language)
    # Use the generated comment to infer the email subject
    email_subject = chatGptApp.generate_email_subject(comment, selected_language)

    # Use the generated comment to generate a summary
    summary = chatGptApp.generate_summary(comment, selected_language)

    # Use the generated comment to analyze sentiment
    sentiment = chatGptApp.analyze_sentiment(comment, selected_language)

    # Generate an email in the selected language
    email = chatGptApp.generate_email(comment, email_subject, summary, sentiment, selected_language)
    print("This is my email content:")
    print(email)
    return jsonify({'reply': email, 'subject': email_subject})

if __name__ == '__main__':
    app.run(debug=True)