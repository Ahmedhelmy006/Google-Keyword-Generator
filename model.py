from rake_nltk import Rake

def extract_keywords(product_name):
    r = Rake()
    r.extract_keywords_from_text(product_name)
    keywords = r.get_ranked_phrases()
    return ', '.join(keywords)
