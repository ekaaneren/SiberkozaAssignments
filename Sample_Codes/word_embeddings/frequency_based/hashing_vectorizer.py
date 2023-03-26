"""
A vectorizer which uses the hashing trick to find the token string name to feature integer index mapping.
"""

from sklearn.feature_extraction.text import HashingVectorizer


def hashing_vec(docs):
    h_vectorizer = HashingVectorizer(n_features=10000, norm=None, alternate_sign=False)
    X = h_vectorizer.fit_transform(docs)
    return X


def main():
    d = [
        "One Cent, Two Cents, Old Cent, New Cent: All About Money (Cat in the Hat's Learning Library",
        "Inside Your Outside: All About the Human Body (Cat in the Hat's Learning Library)",
        "Oh, The Things You Can Do That Are Good for You: All About Staying Healthy (Cat in the Hat's Learning Library)",
        "On Beyond Bugs: All About Insects (Cat in the Hat's Learning Library)",
        "There's No Place Like Space: All About Our Solar System (Cat in the Hat's Learning Library)"
    ]
    print(hashing_vec(d))

main()
