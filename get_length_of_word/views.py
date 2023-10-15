from django.http import HttpResponse

def get_length_of_word(request, word):
    # Filter the word to include only alphabetic characters
    filtered_word = ''.join(char for char in word if char.isalpha())
    length = len(filtered_word)
    response_text = {f'the length: {length}'}
    return HttpResponse(response_text)
