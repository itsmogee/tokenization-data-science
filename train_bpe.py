import os
import urllib.request

from simple_bpe_tokenizer import SimpleBpeTokenizer

if not os.path.exists("the-verdict.txt"):
    url = ("https://raw.githubusercontent.com/rasbt/"
           "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
           "the-verdict.txt")
    file_path = "the-verdict.txt"
    urllib.request.urlretrieve(url, file_path)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    text = f.read()


tokenizer = SimpleBpeTokenizer()
# Question: 
tokenizer.train(text, vocab_size=1000, allowed_special={"<|endoftext|>"})

# print(tokenizer.vocab)
print(len(tokenizer.vocab))


print(len(tokenizer.bpe_merges))


input_text = "Jack embraced beauty through art and life."
token_ids = tokenizer.encode(input_text)
print(token_ids)

for token_id in token_ids:
    print(f"{token_id} -> {tokenizer.decode([token_id])}")
