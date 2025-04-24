# Write a Ruby class WordFrequencyAnalyzer that analyzes a given paragraph and returns:
# * The top 3 most frequent words (case-insensitive, ignore punctuation).
# * The count of each word in descending order of frequency.

# Example:
#
# text = "The quick brown fox jumps over the lazy dog. The fox is quick and smart!"

# WordFrequencyAnalyzer.call(text)

# expected output:
# {
#   top_3: ["the", "quick", "fox"],
#   word_counts: {
#     "the" => 3,
#     "quick" => 2,
#     "fox" => 2,
#     "jumps" => 1,
#     "over" => 1,
#     "lazy" => 1,
#     "dog" => 1,
#     "is" => 1,
#     "and" => 1,
#     "smart" => 1
#   }
# }

import re
from collections import Counter

class WordFrequencyAnalyzer:
    # instance method implementation
    # def __init__(self, text):
    #     self.text = text

    # def analyze(self):
    #     # Normalize text: lowercase and remove punctuation
    #     words = re.findall(r'\b\w+\b', self.text.lower())
        
    #     # Count frequency
    #     word_counts = Counter(words)
        
    #     # Get top 3 most common words
    #     top_3 = [word for word, _ in word_counts.most_common(3)]

    #     return {
    #         'top_3': top_3,
    #         'word_counts': dict(word_counts)
    #     }

    # class method implementation
    @classmethod
    def analyze(cls, text):
        # Normalize text: lowercase and remove punctuation
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Count frequency
        word_counts = Counter(words)
        
        # Get top 3 most common words
        top_3 = [word for word, _ in word_counts.most_common(3)]

        # Sort word_counts by count in descending order
        sorted_word_counts = dict(sorted(
            word_counts.items(),
            key=lambda x: -x[1]
        ))

        return {
            'top_3': top_3,
            'word_counts': sorted_word_counts
        }
