# predict.py

import torch

from transformers import BertTokenizer, BertForSequenceClassification

import torch.nn.functional as f

tokenizer = BertTokenizer.from_pretrained("sarkararnab/toxic_bert_model")

model = BertForSequenceClassification.from_pretrained("sarkararnab/toxic_bert_model")

model.eval()

labels = ['non-toxic', 'toxic']

def predict_comment(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)
        probs = f.softmax(outputs.logits, dim=-1)

    non_toxic_prob = probs[0][0].item()
    toxic_prob = probs[0][1].item()

    label = "toxic" if toxic_prob >= 0.5 else "non-toxic"

    return {
        "label": label,
        "toxic_probability": round(toxic_prob, 4),
        "non_toxic_probability": round(non_toxic_prob, 4)
    }

