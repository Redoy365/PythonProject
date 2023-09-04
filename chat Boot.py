CB = {
    'hi':'hello',
    'your name':'my name is chatbot',
    'your old':'i am only 1 year old',
    'your aim': 'My aim is MLE'
}


while True:

    try:
        quit = input()
        if quit == 'exit':
            break
        print(CB[quit])
        print("____________")
    
    except:
        print("I don't know !")


