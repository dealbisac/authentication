# File to put the custom helper function here.

# A function to generate the random string
import random
import string


def get_string(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    return final_string

# new function to generate the random username
def generate_random_username():
    # List of animal names (100 animals)
    animal_names = ['lion', 'tiger', 'elephant', 'zebra', 'giraffe', 'monkey', 'eagle', 'hawk', 'sparrow', 'parrot',
                    'dog', 'cat', 'horse', 'rabbit', 'hamster', 'turtle', 'goldfish', 'kangaroo', 'koala', 'penguin',
                    'panda', 'gorilla', 'dolphin', 'whale', 'cheetah', 'leopard', 'jaguar', 'rhinoceros', 'buffalo',
                    'hippopotamus', 'crocodile', 'snake', 'frog', 'butterfly', 'dragonfly', 'owl', 'peacock', 'polarbear',
                    'elephantseal', 'armadillo', 'albatross', 'antelope', 'baboon', 'beaver', 'bison', 'booby', 'capybara',
                    'chameleon', 'chinchilla', 'cockatoo', 'cougar', 'dingo', 'echidna', 'falcon', 'firefly', 'flamingo',
                    'gecko', 'gerbil', 'gnat', 'gorilla', 'grizzlybear', 'hedgehog', 'hornet', 'hyena', 'ibex', 'iguana',
                    'impala', 'jellyfish', 'kookaburra', 'lemur', 'lynx', 'macaw', 'marmoset', 'meerkat', 'nematode',
                    'ocelot', 'orangutan', 'otter', 'panther', 'peafowl', 'platypus', 'quokka', 'quokka', 'raccoon',
                    'rat', 'redpanda', 'reindeer', 'scorpion', 'seagull', 'sloth', 'snowleopard', 'starfish', 'tapir',
                    'toucan', 'wallaby', 'walrus', 'weasel', 'whippet', 'wombat', 'yak', 'yeti', 'zebu']

    # List of adjectives (more than 100 adjectives)
    adjectives = ['happy', 'funny', 'fierce', 'lively', 'playful', 'bright', 'joyful', 'vibrant', 'courageous', 'gentle',
                  'creative', 'energetic', 'charming', 'confident', 'dynamic', 'graceful', 'harmonious', 'inspiring',
                  'passionate', 'optimistic', 'radiant', 'sociable', 'tenacious', 'upbeat', 'whimsical', 'zealous',
                  'affectionate', 'brilliant', 'dazzling', 'ecstatic', 'effervescent', 'exuberant', 'magnetic', 'mirthful',
                  'pizzazz', 'resilient', 'serendipitous', 'stellar', 'synergetic', 'vivacious', 'zestful', 'ambitious',
                  'buoyant', 'captivating', 'daring', 'delightful', 'effortless', 'enchanting', 'ethereal', 'genuine',
                  'illustrious', 'innovative', 'majestic', 'noble', 'outgoing', 'precious', 'radiant', 'sensational',
                  'spectacular', 'tranquil', 'unwavering', 'wholesome', 'youthful', 'zesty', 'adaptable', 'blissful',
                  'captivating', 'dashing', 'effervescent', 'exquisite', 'graceful', 'intriguing', 'mesmerizing',
                  'phenomenal', 'quizzical', 'ravishing', 'spellbinding', 'thrilling', 'unforgettable', 'wondrous',
                  'charismatic', 'effortless', 'enchanting', 'inspirational', 'magnificent', 'picturesque', 'radiant']

    # Select a random name, adjective, and digit
    random_name = random.choice(animal_names)
    random_adjective = random.choice(adjectives)
    random_digit = random.randint(0, 9)

    # Combine and limit the length to a maximum of 8 characters
    username = f"{random_name}{random_adjective}{random_digit}".lower()[:10]

    return username


