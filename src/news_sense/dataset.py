from datasets import load_dataset


def load_news_dataset():
    """
    Download and return the AG News dataset.
    """
    return load_dataset("sh0416/ag_news")
