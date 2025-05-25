import torch
import re
from transformers import AutoTokenizer, BartForConditionalGeneration

def text_summarizer_after_ft(text, max_length, min_length, num_beams, length_penalty, no_repeat_ngram_size):
    model_name = "facebook/bart-base"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")
    inputs = tokenizer(text, return_tensors="pt", max_length=2048, truncation=True)
    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_length,
            min_length=min_length,
            num_beams=num_beams,
            length_penalty=length_penalty,
            no_repeat_ngram_size=no_repeat_ngram_size if no_repeat_ngram_size > 0 else None,
            early_stopping=True
        )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    pattern = r"(reported by|reports the|according to) [A-Z][a-z]+(?: [A-Z][a-z]+)*"
    return re.sub(pattern, " ", summary)
