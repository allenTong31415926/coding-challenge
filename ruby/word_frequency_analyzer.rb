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

class WordFrequencyAnalyzer
  def self.call(text)
    new(text).analyze_word_frequency
  end

  def initialize(text)
    @text = text
    @word_frequency = {}
  end

  def analyze_word_frequency
    @text.split(' ').map do |raw_word|
      # remove punctuation, downcase and strip
      word = raw_word.gsub(/[^a-z0-9\s]/i, '').downcase.strip

      @word_frequency[word] ||= 0
      @word_frequency[word] += 1
    end

    build_output
  end

  private

  def build_output
    sorted_word_frequency = @word_frequency.sort_by { |word, frequency| frequency }.reverse.to_h
    {
      top3_words: sorted_word_frequency.keys.first(3),
      word_counts: sorted_word_frequency
    }
  end
end