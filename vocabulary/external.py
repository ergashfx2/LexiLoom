import requests

def get_word(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

    headers = {
        "X-RapidAPI-Key": "dca4c33f80msh0328ccaea04015fp1e3963jsnc8748ca75e0b",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'results' in data:
        results = data['results']
        details = []

        for result in results:
            detail = {
                'definition': result.get('definition', ''),
                'partOfSpeech': result.get('partOfSpeech', ''),
                'synonyms': result.get('synonyms', []),
                'antonyms': result.get('antonyms', []),
                'examples': result.get('examples', []),
            }
            details.append(detail)

        return {'word': word, 'details': details}

    # If 'results' is not present in the response
    return {'word': word, 'details': []}


word_definitions = {
    "Happy": "Feeling or showing pleasure or contentment.",
    "Blue": "Having a color like that of a clear sky.",
    "Cat": "A small domesticated carnivorous mammal.",
    "Jump": "To push oneself off a surface and into the air using the muscles in one's legs.",
    "Red": "Having a color resembling that of blood or a ripe tomato.",
    "Run": "Move at a speed faster than a walk, never having both or all the feet on the ground at the same time.",
    "Big": "Of considerable size, extent, or intensity.",
    "Sun": "The star around which the earth orbits.",
    "Eat": "Put (food) into the mouth and chew and swallow it.",
    "Small": "Of a size that is less than normal or usual.",
    "Dog": "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice.",
    "Cold": "At or having a low or relatively low temperature or one lower than normal or expected.",
    "Read": "Look at and comprehend the meaning of (written or printed matter) by mentally interpreting the characters or symbols of which it is composed.",
    "Hot": "Having a high degree of heat or a high temperature.",
    "Play": "Engage in activity for enjoyment and recreation rather than a serious or practical purpose.",
    "Water": "A colorless, transparent, odorless, tasteless liquid that forms the seas, lakes, rivers, and rain and is the basis of the fluids of living organisms.",
    "Sleep": "A condition of body and mind that typically recurs for several hours every night, in which the nervous system is relatively inactive, the eyes closed, the postural muscles relaxed, and consciousness practically suspended.",
    "Friend": "A person with whom one has a bond of mutual affection, typically one exclusive of sexual or family relations.",
    "Sing": "Make musical sounds with the voice, especially words with a set tune.",
    "Rain": "Moisture condensed from the atmosphere that falls visibly in separate drops.",
    "Walk": "Move at a regular and fairly slow pace by lifting and setting down each foot in turn, never having both feet off the ground at once."
}



word_synonyms_dict = {
    'happy': 'joyful, content, pleased, satisfied, elated',
    'sad': 'unhappy, mournful, melancholy, depressed, gloomy',
    'beautiful': 'attractive, stunning, gorgeous, lovely, charming',
    'strong': 'powerful, robust, sturdy, vigorous, resilient',
    'smart': 'intelligent, clever, bright, sharp, wise',
    'kind': 'compassionate, generous, considerate, benevolent, sympathetic',
    'angry': 'irate, furious, indignant, enraged, incensed',
    'brave': 'courageous, fearless, valiant, heroic, bold',
    'calm': 'serene, tranquil, composed, relaxed, peaceful',
    'friendly': 'amiable, affable, sociable, cordial, genial',
    'funny': 'humorous, comical, witty, laughable, entertaining',
    'creative': 'innovative, imaginative, original, resourceful, inventive',
    'successful': 'accomplished, prosperous, triumphant, victorious, thriving',
    'diligent': 'hardworking, industrious, persevering, dedicated, conscientious',
    'patient': 'tolerant, enduring, forbearing, unperturbed, calm'
}
