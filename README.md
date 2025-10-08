# AlpaCare Medical Instruction Assistant

A fine-tuned LLM for educational medical instruction responses, built with safety constraints.

## Overview

This project fine-tunes a Llama-2-7B-Chat model on the AlpaCare-MedInstruct-52k dataset using LoRA/PEFT. The assistant provides general medical information for educational purposes only.

**Important Safety Notice:** This model does not diagnose, prescribe, or make clinical decisions. All outputs include a disclaimer. Consult qualified clinicians for medical advice.

## Setup

1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. For fine-tuning: Open `notebooks/colab-finetune.ipynb` in Google Colab.
4. For inference: Run `inference_demo.ipynb` in Colab or locally (with GPU).

## Files

- `data_loader.py`: Loads and preprocesses the dataset.
- `notebooks/colab-finetune.ipynb`: Fine-tuning notebook.
- `inference_demo.ipynb`: Inference demo with samples.
- `requirements.txt`: Dependencies.
- `REPORT.md`: Detailed report.
- `human_eval.csv`: Template for human evaluations.

## Model

- Base: meta-llama/Llama-2-7b-chat-hf
- Fine-tuned with LoRA (r=16, alpha=32)
- Dataset: lavita/AlpaCare-MedInstruct-52k (90/5/5 split)

## Safety

- No diagnostic outputs.
- No prescriptions/dosages.
- Disclaimers in all responses.
- Human evaluation required (30+ reviews).

## License

Permissive (Llama-2 license). No public hosting of model.
