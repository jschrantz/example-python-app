Feature: rest basic functionality

Scenario: Add a single record to the system
    Given the example records
        """
        Washington,George,M,Red,2/22/1732
        """
    When I submit the records to the system
    Then it should return successfully

Scenario: Add a list of records in json to the system
    Given the example records
        '''
        ["Doe|John|M|Blue|5/5/1990",
        "Doe|Jane|F|Purple|4/7/1992",
        "Smith|Joe|M|Orange|9/8/1980",
        "Smith|Juliet|F|Green|8/10/1979"]
        '''
    When I submit the records to the system
    Then it should return successfully

Scenario: Get records sorted by gender
    When I get the records sorted by gender
    Then it should return successfully
    And the response should match
        '''
        [{"last_name": "Doe", "first_name": "Jane", "gender": "F", "color": "Purple", "birth_date": "04/07/1992"},
        {"last_name": "Smith", "first_name": "Juliet", "gender": "F", "color": "Green", "birth_date": "08/10/1979"},
        {"last_name": "Doe", "first_name": "John", "gender": "M", "color": "Blue", "birth_date": "05/05/1990"},
        {"last_name": "Smith", "first_name": "Joe", "gender": "M", "color": "Orange", "birth_date": "09/08/1980"},
        {"last_name": "Washington", "first_name": "George", "gender": "M", "color": "Red", "birth_date": "02/22/1732"}]
        '''

Scenario: Get records sorted by birthdate
    When I get the records sorted by birthdate
    Then it should return successfully
    And the response should match
        '''
        [{"last_name": "Washington", "first_name": "George", "gender": "M", "color": "Red", "birth_date": "02/22/1732"},
        {"last_name": "Smith", "first_name": "Juliet", "gender": "F", "color": "Green", "birth_date": "08/10/1979"},
        {"last_name": "Smith", "first_name": "Joe", "gender": "M", "color": "Orange", "birth_date": "09/08/1980"},
        {"last_name": "Doe", "first_name": "John", "gender": "M", "color": "Blue", "birth_date": "05/05/1990"},
        {"last_name": "Doe", "first_name": "Jane", "gender": "F", "color": "Purple", "birth_date": "04/07/1992"}]
        '''

Scenario: Get records sorted by name
    When I get the records sorted by name
    Then it should return successfully
    And the response should match
        '''
        [{"last_name": "Washington", "first_name": "George", "gender": "M", "color": "Red", "birth_date": "02/22/1732"},
        {"last_name": "Smith", "first_name": "Juliet", "gender": "F", "color": "Green", "birth_date": "08/10/1979"},
        {"last_name": "Smith", "first_name": "Joe", "gender": "M", "color": "Orange", "birth_date": "09/08/1980"},
        {"last_name": "Doe", "first_name": "John", "gender": "M", "color": "Blue", "birth_date": "05/05/1990"},
        {"last_name": "Doe", "first_name": "Jane", "gender": "F", "color": "Purple", "birth_date": "04/07/1992"}]
        '''