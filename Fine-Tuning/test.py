import openai

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


# Configure the model ID. Change this to your model ID.
model = "ada:ft-personal:drug-malady-data-2023-11-21-02-07-14"

# Let's use a drug from each class
drugs = [
    "A CN Gel(Topical) 20gmA CN Soap 75gm",  # Class 0
    "Addnok Tablet 20'S",  # Class 1
    "ABICET M Tablet 10's",  # Class 2
]

# Returns a drug class for each drug
for drug_name in drugs:
    prompt = "Drug: {}\nMalady:".format(drug_name)
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=1,
    )
    # Print the generated text
    drug_class = response.choices[0].text
    # The result should be 0, 1, and 2
    print(drug_class)