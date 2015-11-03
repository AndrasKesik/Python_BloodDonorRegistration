<<<<<<< HEAD
def valid_gender(gender_string):
    return gender_string.upper() == "F" or gender_string.upper() == "M"
=======


def validate_name(name_string):
    name = name_string.split()
    return name_string.isalpha() and len(name) > 1

>>>>>>> aabdb4a9d9bb868ff5d3652e00d18ead4167b8dd
