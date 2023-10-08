# Customer Support System: An email to the customer
🎯 Goal: Automatically generate an email and send it to the customer according to the comment from the customer

## Step1: Generate a customer's comment using ChatGpt
```
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
```


## Step2: Generate an email sent to the customer
1. Generate email subject

```
def generate_email_subject(self, customer_comment,language='English'):
    # Use ChatGPT to infer the email subject from the customer's comment
    prompt = f"Infer the email subject based on the customer's comment :\n{customer_comment}\nThe response should use language {language}. Word limit: 10."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,  # Adjust the max tokens as needed
        temperature=0.7
    )
    return response.choices[0].text.strip()
```

2. Generate the summary of the customer's comment

```
def generate_summary(self, customer_comment, language='English'):
    # Use ChatGPT to generate a summary of the customer's comment
    prompt = f"Summarize the following customer comment:\n{customer_comment}\nThe response should use language {language}."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=200,  # Adjust the max tokens as needed
        temperature=0.7
    )
    return response.choices[0].text.strip()
```

3. Sentiment analysis of the customer's comment

```
def analyze_sentiment(self, customer_comment, language='English'):
    # Use ChatGPT to analyze the sentiment of the customer's comment
    prompt = f"Analyze the sentiment of the following customer comment:\n{customer_comment}\nThe response should use language {language}."
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
```

4. Generate an email to be sent to the customer

```
def generate_email(self, comment, subject, summary, sentiment, language='English'):
    # Use ChatGPT to generate an email in the selected language
    # prompt = f"Compose an email in {language}:\nSubject: {subject}\n\nDear Customer,\n\nThank you for your comment. We have generated a response for you:\n\n{comment}\n\nSummary: {summary}\n\nSentiment Analysis: {sentiment}\n\nSincerely,\nYour Company"
    prompt = (f"Given the customer's comment: '{comment}', "
                    f"its summary: '{summary}', its sentiment: '{sentiment}', "
                    f"and the email subject: '{subject}',please craft an email response in 100 words or less. The response should use language {language}.")
    print("This is my email prompt:")
    print(prompt)
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=400,  # Adjust the max tokens as needed
        temperature=0.7
    )
    return response.choices[0].text.strip()
```


## Result
Test cases:

<img width="618" alt="Screenshot 2023-10-08 at 1 28 09 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/9f704673-a9af-44e0-9b7b-c118da331380">

Test case1: English -> English

<img width="1440" alt="Screenshot 2023-10-08 at 1 53 35 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/b5bb59a7-e547-43a9-b342-343e4cd02f2c">


Test case2: English -> Chinese

<img width="1440" alt="Screenshot 2023-10-08 at 1 49 25 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/fcb4361b-f514-4723-a18a-3ca2ff889b2a">


Test case3: Chinese -> English

<img width="1440" alt="Screenshot 2023-10-08 at 1 54 02 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/11a1eb1e-1c3d-4d8a-a6dc-c27485dd4531">


Test case4: Chinese -> Chinese

<img width="1440" alt="Screenshot 2023-10-08 at 1 48 38 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/af895402-0e3a-47b2-b0e7-66fa3ad63290">
