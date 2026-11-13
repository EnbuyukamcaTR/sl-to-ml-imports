def autoinput(text=""):
    user_input = input(text)
    try:
        result = ast.literal_eval(user_input)
    except(ValueError, SyntaxError):
        result = user_input
    return result
