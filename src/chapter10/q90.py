from transformers import MarianMTModel, MarianTokenizer
from transformers.models.marian.tokenization_marian import MarianTokenizer
def main():
    print("load_data")
    with open(
            "../../data/kyoto-train.en") as train_x, open(
            "../../data/kyoto-train.ja") as train_y, open(
            "../../data/kyoto-dev.en") as valid_x, open(
            "../../data/kyoto-dev.ja") as valid_y, open(
            "../../data/kyoto-test.en") as test_x, open(
            "../../data/kyoto-test.ja") as test_y:


        train_X = train_x.read()
        train_Y = train_y.read()
        valid_X = valid_x.read()
        valid_Y = valid_y.read()
        test_X = test_x.read()
        test_Y = test_y.read()

    print("make list of test")
    src_text = [sentence for sentence in test_X.split("\n")]


    print("translate")
    model_name = 'Helsinki-NLP/opus-mt-en-jap'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    print(tokenizer.supported_language_codes)

    model = MarianMTModel.from_pretrained(model_name)
    translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    print(len(tgt_text))

if __name__ == '__main__':
    main()