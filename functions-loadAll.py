# define via link
# exec(__import__('requests').get('https://raw.githubusercontent.com/EnbuyukamcaTR/sl-to-ml-imports/refs/heads/main/functions-autoinput.py').text)
# exec(__import__('requests').get('https://raw.githubusercontent.com/EnbuyukamcaTR/sl-to-ml-imports/refs/heads/main/functions-cls.py').text)

# define directly
def autoinput(text=""):
    user_input = input(text)
    try:
        result = ast.literal_eval(user_input)
    except(ValueError, SyntaxError):
        result = user_input
    return result
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
