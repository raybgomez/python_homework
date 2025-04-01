# Task 1
def hello():
    return "Hello!"

hello()

# Task 2
def greet(name):
    return "Hello, "+name+"!"

greet('Lucy')

# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a % b
            case "power":
                return a ** b
            case _:
                return "Invalid Operation!"
    except ZeroDivisionError:
                return "You can't divide by 0!"
    except TypeError:
                return "You can't multiply those values!"
            
# Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "int":
                return int(value)
            case "str":
                return str(value)
            case _:
                return f"Invalid data type: {data_type}"
    except ValueError: 
        return f"You can't convert {value} into a {data_type}."
    
    #Task 5

    def grade(*args):
            try:
                average = sum(args) / len(args)
                match average:
                    case _ if average >= 90:
                        return "A"
                    case _ if average >= 80:
                        return "B"
                    case _ if average >= 70:
                        return "C"
                    case _ if average >= 60:
                        return "D"
                    case _:
                        return "F"
            except (TypeError, ZeroDivisionError):
                    return "Invalid data was provided"
       
    print(grade(90, 95, 75))
            
# Task 6
def repeat(string, count):
     result =""
     for _ in range(count):
          result += string
     return result

# Task 7
def student_scores(option, **kwargs):
     if option == "best":
          best_student = max(kwargs, key=kwargs.get)
          return best_student
     elif option == "mean":
          average_score = sum(kwargs.values()) / len(kwargs)
          return average_score
     else:
          return "Invalid Option"
     
#Task 8
def titleize(title):
     little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

     words = title.split()

     for i, word in enumerate(words):
          if i == o or i == len(words) - 1 or word.lower() not in little_words:
               words[i] = word.capitalize()
          else:
               words[i] = word.lower()

     return " ".join(words)

# Task 9
def hangman(secret, guess):
    result = ""

    for char in secret:
        if char in guess:
            result += char
        else:
             result += "_"

    return result

# Task 10

def pig_latin(sentence):
     vowels = "aeiou"
     words = sentence.split()
     pig_latin_words = []

     for word in words:
          if word.startswith('qu'):
               pig_latin_word = word[2:] + "quay"
          elif word[0] in vowels:
               pig_latin_word = word + "ay"
          else:
               consonant_cluster = ""
               while word and word[0] not in vowels:
                    consonant_cluster += word[0]
                    word = word[1:]
               pig_latin_word = word + consonant_cluster + "ay"

               pig_latin_words.append(pig_latin_word)

     return " ".join(pig_latin_words)

