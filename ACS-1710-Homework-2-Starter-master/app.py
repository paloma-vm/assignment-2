from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

# @app.route('/froyo')
# def choose_froyo():
#     """Shows a form to collect the user's Fro-Yo order."""
#     return """
#     <form action='/froyo_results' method="GET">
#         What is your favorite Fro-Yo flavor? <br/>
#         <input type='text' name='flavor'><br/>
#         What are your favorite Fro-Yo toppings? <br/>
#         <input type='text' name='toppings'><br/>
#         <input type='submit' value='Submit!'>
#     </form>
#     """

# refactor fro-yo to render template
@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')


# @app.route('/froyo_results')
# def show_froyo_results():
#     """Shows the user what they ordered from the previous page."""
#     users_froyo_flavor = request.args.get('flavor')
#     users_froyo_toppings = request.args.get('toppings')
#     return f'You ordered {users_froyo_flavor} flavored Fro-Yo with {users_froyo_toppings} on top!'

# refactor fro-yo results to render template
@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
            'users_froyo_flavor': request.args.get('flavor'),
            'users_froyo_toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)
    


@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action='/favorites_results' method="GET">
        What is your favorite color? <br/>
        <input type='text' name='color'><br/>
        What is your favorite animal? <br/>
        <input type='text' name='animal'><br/>
        What is your favorite city? <br/>
        <input type='text' name='city'><br/>
        <input type='submit' value='Submit!'>
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fave_color = request.args.get('color')
    users_fave_animal = request.args.get('animal')
    users_fave_city = request.args.get('city')

    return f"Wow, I didn't know {users_fave_color} {users_fave_animal}s lived in {users_fave_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action='/message_results' method="POST">
        What is your secret message? <br/>
        <input type='text' name='message'><br/>
        <input type='submit' value='Submit!'>
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    alphabetized_message = sort_letters(users_message)
    return f'{alphabetized_message}'

# @app.route('/calculator')
# def calculator():
#     """Shows the user a form to enter 2 numbers and an operation."""
#     return """
#     <form action="/calculator_results" method="GET">
#         Please enter 2 numbers and select an operator.<br/><br/>
#         <input type="number" name="operand1">
#         <select name="operation">
#             <option value="add">+</option>
#             <option value="subtract">-</option>
#             <option value="multiply">*</option>
#             <option value="divide">/</option>
#         </select>
#         <input type="number" name="operand2">
#         <input type="submit" value="Submit!">
#     </form>
#     """

# refactor calulator to render template
@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

# @app.route('/calculator_results')
# def calculator_results():
#     users_operand1 = request.args.get('operand1')
#     users_operation = request.args.get('operation')
#     users_operand2 = request.args.get('operand2')

#     """Shows the user the result of their calculation."""
    # if users_operation == "add":
    #     users_answer = int(users_operand1) + int(users_operand2)
    #     # return f'{users_operand1} + {users_operand2} = {users_answer}'
   
    # elif users_operation == "subract":
    #     users_answer = int(users_operand1) - int(users_operand2)

    # elif users_operation == "multiply":
    #     users_answer = int(users_operand1) * int(users_operand2)

    # elif users_operation == "divide":
    #     users_answer = int(users_operand1) / int(users_operand2)
    
    # return f'You chose to {users_operation} {users_operand1} and {users_operand2}. Your result is: {users_answer}'

# refactor calulator_results to render template
@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    users_operand1 = request.args.get('operand1')
    users_operation = request.args.get('operation')
    users_operand2 = request.args.get('operand2')

    print("***********")
    print(users_operation)
    if users_operation == "add":
        users_answer = int(users_operand1) + int(users_operand2)
   
    if users_operation == "subtract":
        users_answer = int(users_operand1) - int(users_operand2)

    if users_operation == "multiply":
        users_answer = int(users_operand1) * int(users_operand2)

    if users_operation == "divide":
        users_answer = int(users_operand1) / int(users_operand2) 

    context = {
        "users_operand1": users_operand1,
        "users_operation": users_operation,
        "users_operand2": users_operand2,
        "users_answer": users_answer  
    }
    print(context)
    return render_template('calculator_results.html', **context)



HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}
print("testing horoscope")
print(HOROSCOPE_PERSONALITIES['aries'])

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    users_name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)

    context = {
        'users_name': users_name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality,
        'lucky_number': lucky_number
    }
    print(context)
    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
