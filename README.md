# Tokenization

## How to use 

1. Create and Activate virtual env
    ```language=python
    python -m venv .venv
    .venv/Scripts/activate
    ```
2. Install Libraries
   ```language=bash
   pip install -r requirements.txt
   ```
3. Run the below commands to train your first BPE
   ```language=bash
   python train_bpe.py
   ```
4. Compare to OpenAI tokenizer
   ```language=bash
   python compare_to_open_ai.py
   ```

### Papers 
- [A formal perspective on Byte-Pair Encoding](https://arxiv.org/pdf/2306.16837)
- [BloombergGPT: A Large Language Model For Finance](https://arxiv.org/pdf/2303.17564)
- [Neural Machine Translation with Byte-Level Subwords](https://arxiv.org/pdf/1909.03341)

### References

- Sebastian Raschka
  - [BPE From Scratch](https://sebastianraschka.com/blog/2025/bpe-from-scratch.html)

- OpenAI Educational Tiktoken
  - [Tiktoken](https://github.com/openai/tiktoken/blob/main/tiktoken/_educational.py)

- Original OpenAI GPT2
  - [GPT2](https://github.com/openai/gpt-2/blob/master/src/encoder.py)

- HuggingFace Tokenizer
