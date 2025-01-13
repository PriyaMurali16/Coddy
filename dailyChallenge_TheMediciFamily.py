def medici_family(relation_name, relation_role):
    if relation_name.lower() == "giovanni di bicci de' medici":
        if relation_role.lower() == 'founder':
            final_result = True
        else :
            final_result = False 
    elif relation_name.lower() == "lorenzo de' medici":
        if relation_role.lower() == 'patron':
            final_result = True
        else :
            final_result = False 

    elif relation_name.lower() == "cosimo de' medici":
        if relation_role.lower() == 'politician':
            final_result = True
        else :
            final_result = False 
    
    elif relation_name.lower() == "piero di cosimo de' medici":
        if relation_role.lower() == 'father':
            final_result = True
        else :
            final_result = False 
    
    return final_result

