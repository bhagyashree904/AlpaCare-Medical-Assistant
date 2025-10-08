"""
data_loader.py — loads and preprocesses AlpaCare-MedInstruct dataset
"""

from datasets import load_dataset
from transformers import AutoTokenizer

def load_and_prepare_dataset(model_name="mistralai/Mistral-7B-Instruct-v0.1", max_length=512):
    """
    Loads lavita/AlpaCare-MedInstruct-52k and returns tokenized train/eval datasets.
    Adds disclaimer and instruction formatting.
    """
    print("🔹 Loading dataset...")
    dataset = load_dataset("lavita/AlpaCare-MedInstruct-52k")
    dataset = dataset["train"].train_test_split(test_size=0.1)
    train_data, eval_data = dataset["train"], dataset["test"]

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def format_example(example):
        return {
            "text": f"### Instruction:\n{example['instruction']}\n\n### Input:\n{example['input']}\n\n### Response:\n{example['output']}\n\nDisclaimer: This is educational only — consult a qualified clinician."
        }

    print("🔹 Formatting dataset...")
    train_data = train_data.map(format_example)
    eval_data = eval_data.map(format_example)

    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=max_length)

    print("🔹 Tokenizing dataset...")
    train_tokenized = train_data.map(tokenize, batched=True)
    eval_tokenized = eval_data.map(tokenize, batched=True)

    print("✅ Dataset ready!")
    return train_tokenized, eval_tokenized, tokenizer
