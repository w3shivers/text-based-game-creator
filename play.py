import json

class Story():
    __user_name = None
    __story = None

    def __init__(self) -> None:
        file = open('story.json')
        self.__story = json.load(file)
        self.__get_user()
        self.__read_chapter()
    
    def __get_user(self) -> None:
        self.__user_name = input('What is your name? ')
        if not self.__user_name:
            print('Error name must be provided.\n')
            self.__get_user()
        
    def __read_chapter(self, chapter: str='intro') -> None:
        only_chapter = self.__story[chapter]
        message = only_chapter['message'].replace('__name__', self.__user_name)
        print(message)
        new_capter = self.__get_input(input_data=only_chapter['input'], options=only_chapter['options'])
        self.__read_chapter(chapter=new_capter)
    
    def __get_input(self, input_data: str, options: dict, count: int=0) -> str:
        if count >= 5:
            print('Game left. You got to many times the wrong input')
            quit()
        error = False
        user_input = input(input_data + " ").lower().strip()
        if not user_input:
            error = True
            print('Sorry no option provided. Please try again.')
        elif user_input not in options.values():
            error = True
            print('Sorry only one of the following options allowed:')
            for key in options:
                print('- ', options[key])
        if error:
            count += 1
            return self.__get_input(input_data=input_data, options=options, count=count)
        for key in options:
            if options[key] == user_input:
                print('') # space after each chapter.
                return key

Story()