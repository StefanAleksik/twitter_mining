import sys
import json
import io

encoding = 'utf-8-sig'


def read_scores(sent_file):
    "Parse sentiment file, returns a {word: sentiment} dict"
    with io.open(sent_file, encoding=encoding) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def tweet_score(tweet, scores):
    "Returns the score for a tweet or 0 if it's not in AFINN-111.txt"
    return sum(scores.get(word, 0) for word in tweet.split())


def tweet_scores(tweet_file, scores):
    "Calculate scores for all tweets in tweet_file"
    with io.open(tweet_file, encoding=encoding) as f:
        tweets = (json.loads(line).get('text', '') for line in f)
        return [tweet_score(tweet, scores) for tweet in tweets]


if __name__ == '__main__':
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = read_scores(sent_file=sent_file)
    sys.stdout.writelines('{0}.0\n'.format(score)
                          for score in tweet_scores(tweet_file=tweet_file, scores=scores))