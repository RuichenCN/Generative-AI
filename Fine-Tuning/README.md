# Fine-Tuning
Use 2000 Drug Examples

# Presentation
[Google Slides](https://docs.google.com/presentation/d/17-WJJTaLRmYUY3kiCEqtwezybcOfWXHTspdmqlbb1a0/edit#slide=id.g25f6af9dd6_0_0)

# Implementation
## Step 1 Preparing the Data and Launching the Fine Tuning
run "app.py" and then you will get these files:

<img width="218" alt="Screenshot 2023-11-20 at 5 38 23 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/b1fbd23d-2294-4d73-8183-1a67c3eaaf92">



## Step 2 Command to Prepare Data

```
openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl
```

The data can be divided into two parts: one for training, the other for validation
- [Recommended] Would you like to split into training and validation set? [Y/n]:


## Step 3 Command to Train the Model

Use the provided command to train the model using fine_tunes.create.

```
# Export your OpenAI key
export OPENAI_API_KEY="xxxxxxxxxxxx"

openai api fine_tunes.create \
   -t "drug_malady_data_prepared_train.jsonl" \
   -v "drug_malady_data_prepared_valid.jsonl" \
   --compute_classification_metrics \
   --classification_n_classes 3 \
   -m ada \
   --suffix "drug_malady_data"
```
Note:  
- The CLI is also able to detect the number of classes used in the dataset.
  - I recommend that you specify the accurate number of classes used in the dataset
- You can specify the model.
  - We are going to use ada, it’s cheap and works great for our use case.
- You can also add a suffix to the fine-tuned model name, we will use drug_malady_data.
- The result is something like
  ada:ft-learninggpt:drug-malady-data-2023-02-21-20-36-07

## Step 4 Checking Job Progress


If the client disconnects during fine-tuning, use the following command to check job progress.

```
openai api fine_tunes.follow -i <JOB ID>
```
      
The output will display progress information and queue numbers.


## Step 5 Completion of Fine-Tuning

When the fine-tuning job is completed, you'll receive an output like this:

```
Created fine-tune: <JOB ID>
Fine-tune costs $0.03
Fine-tune enqueued

Fine-tune is in the queue. Queue number: 31
Fine-tune is in the queue. Queue number: 30
Fine-tune is in the queue. Queue number: 29
Fine-tune is in the queue. Queue number: 28
[...]
[...]
[...]
Fine-tune is in the queue. Queue number: 2
Fine-tune is in the queue. Queue number: 1
Fine-tune is in the queue. Queue number: 0
Fine-tune started
Completed epoch 1/4
Completed epoch 2/4
Completed epoch 3/4
Completed epoch 4/4
Uploaded model: <MODEL ID>
Uploaded result file: <FILE ID>
Fine-tune succeeded

Job complete! Status: succeeded
```

## Step 6 Testing the Fine-Tuned Model
Try out your fine-tuned model using "test.py"

<img width="447" alt="Screenshot 2023-11-20 at 7 47 19 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/6581a9fb-d683-49c8-9194-6a87638dc6c5">


# End
