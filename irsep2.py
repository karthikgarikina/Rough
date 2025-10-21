# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download NLTK data files (only needed once)
nltk.download('punkt')
nltk.download('stopwords')

# Define a preprocessing function
def preprocess_text(text):
    # Step 1: Convert text to lowercase
    text = text.lower()
    
    # Step 2: Tokenize text into words
    words = word_tokenize(text)
    
    # Step 3: Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Step 4: Apply stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    
    return stemmed_words

# Input text
text = "Machine learning algorithms are revolutionizing the world of artificial intelligence."

# Print outputs
print("Original Text:", text)
processed = preprocess_text(text)
processed_text = ' '.join(processed)
print("Processed Text:", processed_text)
print("Preprocessed Words:", processed)

