## Text Paraphrasing using Parrot

### Description

Generating text paaprasing by using the HuggingFace T5 based model called Parrot.Its a simple python based script which takes a list of text input and produces the multiple paraprased version text output.

### Stack

- Need a system with Python3
- Higher RAM and CPU count is recomonded
- HiggingFace token to access the model

### Modules

- Pandas
- Pytorch
- protobuf
- Jupyter Notebook(Optional)
- huggingface-hub

### Model Authentication

To authenticate huggingface for intialising the model

1. Get the Auth token from Huggigface setting under your profile
2. Run  ```python -c "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('YOUR_TOKEN_HERE')" ``` on your terminal.

### Author
botacct111@gmail.com

For more details : https://cicada.hashnode.dev/text-paraphrasing-using-parrot




