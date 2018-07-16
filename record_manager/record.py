
class Record(object):
    def __init__(self, last_name, first_name, gender, color, dob):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.color = color
        self.dob = dob

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return '{} {} {} {} {}'.format(self.last_name,
                                       self.first_name,
                                       self.gender,
                                       self.color,
                                       self.dob.strftime('%m/%d/%Y'))

    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'gender': self.gender,
            'color': self.color,
            'birth_date': self.dob.strftime('%m/%d/%Y')
        }
