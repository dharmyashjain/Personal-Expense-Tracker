# Text File Word Analyzer
# Reads any .txt file and outputs word frequency stats,
# reading time estimate, and the most common meaningful words.
# Usage: python word_analyzer.py myfile.txt

import re
from pathlib import Path
from collections import Counter
import sys

# Common words we want to ignore so results show meaningful content words
STOP_WORDS = {
    "the","a","an","is","in","it","of","and","to","was",
    "that","for","on","are","with","as","at","be","this","by","from","or"
}

def analyze(filepath):
    # Read the file contents, ignoring any encoding errors
    text = Path(filepath).read_text(encoding="utf-8", errors="ignore")

    # Extract all lowercase words using regex
    words = re.findall(r"\b[a-z']+\b", text.lower())
    total = len(words)

    # Count sentences by looking for sentence-ending punctuation
    sentences = len(re.findall(r"[.!?]", text)) or 1

    # Filter out stop words and very short words for meaningful frequency count
    content = [w for w in words if w not in STOP_WORDS and len(w) > 2]
    freq = Counter(content)

    # Average adult reads ~200 words per minute
    reading_time = max(1, round(total / 200))

    # Print the summary stats
    print(f"\nFile: {filepath}")
    print(f"  Total words    : {total}")
    print(f"  Unique words   : {len(set(words))}")
    print(f"  Sentences      : {sentences}")
    print(f"  Avg word/sent  : {total // sentences}")
    print(f"  Reading time   : ~{reading_time} min")

    # Print top 10 content words with a simple bar chart
    print(f"\nTop 10 words (excluding stop words):")
    for word, count in freq.most_common(10):
        bar = "█" * min(count, 30)  # Cap bar length at 30 blocks
        print(f"  {word:15} {count:4}  {bar}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_analyzer.py <file.txt>")
    else:
        analyze(sys.argv[1])
