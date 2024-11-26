"""
Sorting Bird Sightings


Challenge

Easy
Create a function named sort_bird_sightings that receives sightings as its parameter.

This function aims to sort a list of bird sightings, moving illegible entries (represented as empty strings) to the end while preserving the relative order of legible species.

You are an aspiring ornithologist participating in a bird count. During the count, you recorded each bird sighting in a list. However, your notebook got a bit wet, and some of the species names became illegible (represented as empty strings ""). To analyze the sightings effectively, you need to sort the list by moving all the illegible entries to the end while keeping the legible species in their original relative order.

Parameters:

sightings (list): A list of strings representing the bird species sighted. Empty strings ("") represent illegible entries.
The function returns a sorted list of strings, where legible species appear at the beginning in their original relative order, followed by the illegible entries at the end.
"""

def sort_bird_sightings(sightings):
    # Separate the legible species and the illegible entries
    legible = [sighting for sighting in sightings if sighting != ""]
    illegible = [sighting for sighting in sightings if sighting == ""]
    
    # Combine the two lists
    return legible + illegible
   
