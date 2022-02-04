from transformers import MarianMTModel
from transformers.models.marian.tokenization_marian import MarianTokenizer
def main():
    with open(
            "/home/n_noguchi/b3/NLP/nlp100knock/data/kyoto-train.en") as train_x, open(
            "/home/n_noguchi/b3/NLP/nlp100knock/data/kyoto-train.ja") as train_y, open(
            "/home/n_noguchi/b3/NLP/nlp100knock/data/kyoto-dev.en") as valid_x, open(
            "/home/n_noguchi/b3/NLP/nlp100knock/data/kyoto-dev.ja.txt") as valid_y, open(
            "/home/n_noguchi/b3/NLP/nlp100knock/data/kyoto-test.en") as test_x, open(
            "/home/n_noguchi/b3/NLP/nlp100knock/data/kyoto-test.ja.txt") as test_y:


        train_X = train_x.read()
        train_Y = train_y.read()
        valid_X = valid_x.read()
        valid_Y = valid_y.read()
        test_X = test_x.read()
        test_Y = test_y.read()

    src_text = [sentence for sentence in test_X.split("\n")]

    model_name = 'Helsinki-NLP/opus-mt-en-jap'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    translated = model.generate(**tokenizer.prepare_seq2seq_batch(src_text, return_tensors="pt"))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    print(len(tgt_text))

if __name__ == '__main__':
    main()