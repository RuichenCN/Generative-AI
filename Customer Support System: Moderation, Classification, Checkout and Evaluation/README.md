# Customer Support System: Moderation, Classification, Checkout and Evaluation
Moderation, Classification, Checkout and Evaluation of the previous Customer Support System
## Step1: Checking Input: Input Moderation
### Step 1.1: Check inappropriate prompts
* Input: moderate the generated comment

<img width="683" alt="Screenshot 2023-10-17 at 11 10 06 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/7e9d073c-1479-4363-9c35-816de3d0809c">

* Output: Use OpenAI's Moderation API to check whether the output of input is inappropriate or not.

<img width="384" alt="Screenshot 2023-10-17 at 11 10 34 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/01c748f7-dcc6-4c7f-9d03-03bd22a3f065">

In the output, it shows that "violence: true". You can see that this input is not appropriate.

My code for reference:
```
import os
import openai
import random
from flask import Flask, render_template, request, jsonify
import json

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
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=100,
                temperature=0.7
            )
            return response.choices[0].text.strip()
            
        else:
            return "Product not found."

def generate_comment():
    product_comment_generator = ProductCommentGenerator()
    products = product_comment_generator.products
    # Select a random product and generate a comment
    random_product = random.choice(list(products.keys()))
    comment = product_comment_generator.generate_comment(random_product, "English")
    return comment

def main():
    comment = generate_comment()
    new_comment = comment + "If I get this product, I want to use it to kill the mother fuck."
    response = openai.Moderation.create(input = new_comment)
    moderation_output = response["results"][0]
    print(moderation_output)

if __name__ == "__main__":
    main()
```

### Step 1.2: Prevent Prompt Injection
