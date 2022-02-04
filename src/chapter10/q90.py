from transformers import MarianMTModel
from transformers.models.marian.tokenization_marian import MarianTokenizer
from sacrebleu import corpus_bleu

def bleu(predictions, references):
  references = [references]
  bleu_score = corpus_bleu(predictions, references,
                                     smooth_method="exp",
                                     smooth_value=0.0,
                                     force=False,
                                     lowercase=False,
                                     tokenize="ja-mecab",
                                     use_effective_order=False)
  return bleu_score.score

def main():
    print("load_data")
    # with open(
    #         "../../data/kyoto-train.en") as train_x, open(
    #         "../../data/kyoto-train.ja") as train_y, open(
    #         "../../data/kyoto-dev.en") as valid_x, open(
    #         "../../data/kyoto-dev.ja") as valid_y, open(
    #         "../../data/kyoto-test.en") as test_x, open(
    #         "../../data/kyoto-test.ja") as test_y:
    #
    #
    #     train_X = train_x.read()
    #     train_Y = train_y.read()
    #     valid_X = valid_x.read()
    #     valid_Y = valid_y.read()
    #     test_X = test_x.read()
    #     test_Y = test_y.read()

    with open(
            "../../data/mini.en") as train_x, open(
        "../../data/mini.ja") as train_y:
        train_X = train_x.read()
        train_Y = train_y.read()

    print("make list of test")
    src_text = [sentence for sentence in train_X.split("\n")][:-1]
    train_Y = [sentence for sentence in train_Y.split("\n")][:-1]


    print("translate")
    model_name = 'Helsinki-NLP/opus-mt-en-jap'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    translated = model.generate(**tokenizer.prepare_seq2seq_batch(src_text, return_tensors="pt"))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

    print(train_Y)

    bleu_score = bleu(tgt_text, train_Y)

    print(bleu_score)

if __name__ == '__main__':
    main()