import os
import urllib.request


from simple_bpe_tokenizer import SimpleBpeTokenizer

def download_file_if_absent(url, filename):
    if not os.path.exists(filename):
        try:
            with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Failed to download {filename}. Error: {e}")
    else:
        print(f"{filename} already exists")

files_to_download = {
    "https://openaipublic.blob.core.windows.net/gpt-2/models/124M/vocab.bpe": "vocab.bpe",
    "https://openaipublic.blob.core.windows.net/gpt-2/models/124M/encoder.json": "encoder.json"
}

for url, filename in files_to_download.items():
    download_file_if_absent(url, filename)

tokenizer_gpt2 = SimpleBpeTokenizer()
tokenizer_gpt2.load_vocab_and_merges_from_openai(
    vocab_path="encoder.json", bpe_merges_path="vocab.bpe"
)

len(tokenizer_gpt2.vocab)


input_text = "Jack embraced beauty through art and life."
token_ids = tokenizer_gpt2.encode(input_text)
print(token_ids)
print(tokenizer_gpt2.decode(token_ids))