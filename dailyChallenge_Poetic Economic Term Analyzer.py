def poem_analyzer(poem_line, economic_terms):
    words = poem_line.split()
    found_et = []
    for word in words:
        if word in economic_terms:
            found_et.append(word)
    if found_et:  
        return ', '.join(found_et)
    else:
        
        return "No economic terms found."
