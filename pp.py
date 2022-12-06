from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")


#Init models (make sure you init ONLY once if you integrate this to your code)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

phrases = ["Who is president x?"]

for phrase in phrases:
    print("-"*100)
    print()
    print("Input_phrase: ", phrase)
    print()
    print("-"*100)
    para_phrases = parrot.augment(input_phrase=phrase)
    for para_phrase in para_phrases:
        print()
        print(para_phrase)
        print()