import numpy as np

def words_in_same_sentence(sentence, word1, word2):
    """
    Check if two words exist in the same sentence within a NumPy array of strings.

    Parameters:
        array (np.ndarray): A NumPy array of strings (sentences).
        word1 (str): The first word to check.
        word2 (str): The second word to check.

    Returns:
        bool: True if both words exist in the same sentence; otherwise False.
    """
    if word1 in sentence and word2 in sentence:
        return True
    return False

def word_in_subreddit(sentence, word1, word2):
    """
    Check if two words exist in the same sentence within a NumPy array of strings.

    Parameters:
        array (np.ndarray): A NumPy array of strings (sentences).
        word1 (str): The first word to check.
        word2 (str): The second word to check.

    Returns:
        bool: True if both words exist in the same sentence; otherwise False.
    """
    if word1 in sentence:
        return True
    return False


# Load .npz file
def check_words_in_same_sentence(npz_path, word1, word2):
    # Load the .npz file
    count = 0
    sentences = []
    with np.load(npz_path, allow_pickle=True) as data:
        for key in data.files:
            for sentence in data[key]:
                # Use the function to check for words
                
                #if words_in_same_sentence(sentence, word1, word2):
                if word1 in sentence and word2 in sentence:
                    count +=1
                    sentences.append(sentence)
    
    print(f"{word1} and {word2} appear in the same sentence {str(count)} times")

    print("the sentences are \n")
    for sentence in sentences:
        print(f"{sentence} \n")
    return count, sentences


def check_word_in_subreddit(npz_path, word1):
    # Load the .npz file
    count = 0
    sentences = []
    with np.load(npz_path, allow_pickle=True) as data:
        for key in data.files:
            for sentence in data[key]:
                # Use the function to check for words
                #if words_in_same_sentence(sentence, word1, word2):
                if word1 in sentence:
                    count +=1
                    sentences.append(sentence)
    
    print(f"Word '{word1}' appears in this subreddit {str(count)} times")
    print("The sentences are:\n")
    for sentence in sentences:
        print(f"{sentence} \n")
    return count, sentences


# Example usage
npz_file_path = "/Users/odysseaslazaridis/Documents/GitHub/NewsGuessr/data/worldnews.npz"
word_to_check_1 = "gay"
word_to_check_2 = "shit"
array_key_to_check = "sentences"  # Adjust this key to match your .npz structure

# Check if the words exist in the same sentence
count, sentences = check_words_in_same_sentence(npz_file_path, word_to_check_1,word_to_check_2)
#count, sentences = check_word_in_subreddit(npz_file_path, word_to_check_1)
