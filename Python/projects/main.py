import torch
from transformers import MarianMTModel, MarianTokenizer, Seq2SeqTrainer, Seq2SeqTrainingArguments, DataCollatorForSeq2Seq
from datasets import load_metric, load_dataset

# Step 1: Load a pre-trained model and tokenizer for English-to-Chinese translation
model_name = "Helsinki-NLP/opus-mt-en-zh"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Step 2: Load dataset for fine-tuning (use a custom or public dataset)
# For demonstration purposes, using the WMT dataset
dataset = load_dataset("wmt14", "zh-en", split="train")

# Step 3: Preprocess dataset
def preprocess_function(examples):
    inputs = examples["en"]
    targets = examples["zh"]
    model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
    labels = tokenizer(targets, max_length=128, truncation=True, padding="max_length").input_ids
    model_inputs["labels"] = labels
    return model_inputs

tokenized_datasets = dataset.map(preprocess_function, batched=True)

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# Step 5: Metrics for evaluation
metric = load_metric("sacrebleu")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    labels = [[label] for label in tokenizer.batch_decode(labels, skip_special_tokens=True)]
    return metric.compute(predictions=decoded_preds, references=labels)

# Step 6: Training arguments
training_args = Seq2SeqTrainingArguments(
    output_dir="./my_transformer_model",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=3,
    predict_with_generate=True,
    logging_dir='./logs',
    save_strategy="epoch"
)

# Step 7: Create trainer
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

# Step 8: Train the model
trainer.train()

# Step 9: Save the trained model and tokenizer
model.save_pretrained("./my_transformer_model")
tokenizer.save_pretrained("./my_transformer_model")

print("Model training and saving complete!")