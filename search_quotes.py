import json


with open('quotes.json', 'r') as quotes_file:
    quotes = json.load(quotes_file)


def prepare_quote(quote):
    prepared_quote= ''
    prepared_quote += f"Author: {quote['author']}\n"
    prepared_quote += "Tags:\n"
    for tag in quote['tags']:
        prepared_quote += f"  #{tag}\n"
    prepared_quote += f"Quote text:\n  {quote['quote']}\n\n"
    return prepared_quote
  

def search_by_author(a_name):
    result = '\n'
    for quote in quotes:
        if quote['author'] == a_name:
            result += prepare_quote(quote)
    
    if len(result) == 1:
        result = f"\nNothing has been foung by '{a_name}'!\n"

    return result

def search_by_tag(tag):
    result = '\n'
    for quote in quotes:
        if tag in quote['tags']:
            result += prepare_quote(quote)
    
    if len(result) == 1:
        result = f"\nNothing has been found by '{tag}'!\n"

    return result

def search_by_tags(tags):
    result = '\n'
    splt_tags = tags.split(',')

    for quote in quotes:
        counter = 0
        for tag in splt_tags:
            if tag in quote['tags']:
                counter += 1
        
        if len(splt_tags) == counter:
            result += prepare_quote(quotes)
    
    if len(result) == 1:
        result = f"\nNothing has been foung by '{tag}'!\n"

    return result

def searching_main():
    print("\nStarted!\nType 'info' to see all the useful information\n")
    while True:
        inp = input('Type any name/tag/tags to find >>> ')
        inp_split_lst = inp.split()
        command = inp_split_lst[0]
        searching_key = ' '.join(inp_split_lst[1:]).strip()

        if inp in ['exit', 'close']:
            print('\nGood bye!')
            break

        elif command == 'name:':
            print(search_by_author(searching_key))

        elif command == 'tag:':
            print(search_by_tag(searching_key))
        
        elif command == 'tags:':
            print(search_by_tags(searching_key))

        elif inp == 'info':
            print("\nYou can type:\n- 'name: *name_to_find*'\n- 'tag: *tag_to_find*'\n- 'tags: *tag_1,tag_2,tag_n*'\n\nOr type 'exit' or 'close' to stop the searching program\n")

        else:
            print("\nIncorrect input!\nType 'info' to all the commands availible!\n")

if __name__ == '__main__':
    searching_main()