
def sort_records_by_gender(records):
    """ Sort a list of records by gender, last name ascending. """
    return sorted(records, key=lambda x: (x.gender, x.last_name))

def sort_records_by_dob(records):
    """ Sort a list of records decending by date of birth. """
    return sorted(records, key=lambda x: x.dob)

def sort_records_by_name(records):
    """ Sort a list of records by last name descending. """
    return sorted(records, key=lambda x: (x.last_name, x.first_name), reverse=True)