# define via link
# --- removed for now because of name changes ---

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
