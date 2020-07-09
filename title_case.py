def title_case(title, minor_words=""):

    result = ""
    index = 0
    minor_words.split()
 
    while index in range(len(title.split())):
        if index==0:
            result = title.split()[index].lower().capitalize()
        else:
            if title.split()[index].lower() in minor_words.lower().split():
                result = result + " " + title.split()[index].lower()
            else:
                result = result + " " + title.split()[index].lower().capitalize()
        index = index + 1

    return result



print(title_case('a clash of KINGS', 'a an the of'))