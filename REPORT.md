# AlpaCare Medical Instruction Assistant Report

## Dataset

- **Source:** lavita/AlpaCare-MedInstruct-52k (Hugging Face)
- **Description:** 52k medical instruction-response pairs for educational purposes.
- **Preprocessing:** Cleaned text (removed extra spaces), split 90/5/5 (train/val/test).
- **Subset Used:** Full dataset, no filtering beyond cleaning.

## Model Choice

- **Model:** meta-llama/Llama-2-7b-chat-hf
- **Justification:** <7B params, permissive license, strong instruction-following capabilities.
- **Size:** ~7B parameters.

## Preprocessing

- Tokenization: Max length 512, padding to max.
- Format: "Instruction: {inst}\nOutput:" for input, output as labels.

## LoRA Hyperparameters

- r: 16
- lora_alpha: 32
- target_modules: q_proj, v_proj
- lora_dropout: 0.05
- task_type: CAUSAL_LM

## Training

- Epochs: 1
- Batch size: 4
- Learning rate: Default (5e-5)
- Optimizer: AdamW
- FP16: Yes
- Device: GPU (Colab)

## Evaluation

### Automated

- Validation loss monitored.
- No specific metrics beyond loss (due to generative nature).

### Human

- 30+ reviews from medically literate evaluators (clinicians preferred).
- Rubric: Safety (no diagnosis/prescription), Accuracy, Clarity, Disclaimer presence.
- Spreadsheet: human_eval.csv

## Safety & Mitigation

- **Constraints:** Model trained on safe, non-diagnostic data. Outputs filtered for forbidden terms if needed (not implemented).
- **Disclaimer:** All responses include: "This is educational only — consult a qualified clinician."
- **Limitations:** May hallucinate; not a substitute for professional advice.
- **Mitigation:** Human eval, clear warnings, no hosting.

## Limitations

- Single epoch training.
- No advanced safety fine-tuning.
- Potential biases in dataset.
- Requires GPU for inference.

## Conclusion

Model provides educational responses with safety measures. Use responsibly.
