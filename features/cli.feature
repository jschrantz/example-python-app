Feature: cli basic functionality

Scenario: Single csv sorted by gender
    Given the example file records.csv
    When I sort by gender
    Then the output should match
        """
        Washington Martha F Blue 06/13/1731
        Washington George M Red 02/22/1732
        """

Scenario: Single csv sorted by dob
    Given the example file records.csv
    When I sort by dob
    Then the output should match
        """
        Washington Martha F Blue 06/13/1731
        Washington George M Red 02/22/1732
        """

Scenario: Single csv sorted by name
    Given the example file records.csv
    When I sort by name
    Then the output should match
        """
        Washington Martha F Blue 06/13/1731
        Washington George M Red 02/22/1732
        """

Scenario: Single psv sorted by gender
    Given the example file records.psv
    When I sort by gender
    Then the output should match
        """
        Doe Jane F Purple 04/07/1992
        Smith Juliet F Green 08/10/1979
        Doe John M Blue 05/05/1990
        Smith Joe M Orange 09/08/1980
        """

Scenario: Single psv sorted by dob
    Given the example file records.psv
    When I sort by dob
    Then the output should match
        """
        Smith Juliet F Green 08/10/1979
        Smith Joe M Orange 09/08/1980
        Doe John M Blue 05/05/1990
        Doe Jane F Purple 04/07/1992
        """

Scenario: Single psv sorted by name
    Given the example file records.psv
    When I sort by name
    Then the output should match
        """
        Smith Juliet F Green 08/10/1979
        Smith Joe M Orange 09/08/1980
        Doe John M Blue 05/05/1990
        Doe Jane F Purple 04/07/1992
        """

Scenario: Single ssv sorted by gender
    Given the example file records.ssv
    When I sort by gender
    Then the output should match
        """
        Curie Marie F Green 11/07/1867
        Becquerel Antoine M Red 12/15/1852
        Curie Pierre M Yellow 05/15/1859
        """

Scenario: Single ssv sorted by dob
    Given the example file records.ssv
    When I sort by dob
    Then the output should match
        """
        Becquerel Antoine M Red 12/15/1852
        Curie Pierre M Yellow 05/15/1859
        Curie Marie F Green 11/07/1867
        """

Scenario: Single ssv sorted by name
    Given the example file records.ssv
    When I sort by name
    Then the output should match
        """
        Curie Pierre M Yellow 05/15/1859
        Curie Marie F Green 11/07/1867
        Becquerel Antoine M Red 12/15/1852
        """

Scenario: All files sorted by gender
    Given the example file records.csv
    Given the example file records.psv
    Given the example file records.ssv
    When I sort by gender
    Then the output should match
        """
        Curie Marie F Green 11/07/1867
        Doe Jane F Purple 04/07/1992
        Smith Juliet F Green 08/10/1979
        Washington Martha F Blue 06/13/1731
        Becquerel Antoine M Red 12/15/1852
        Curie Pierre M Yellow 05/15/1859
        Doe John M Blue 05/05/1990
        Smith Joe M Orange 09/08/1980
        Washington George M Red 02/22/1732
        """

Scenario: All files sorted by dob
    Given the example file records.csv
    Given the example file records.psv
    Given the example file records.ssv
    When I sort by dob
    Then the output should match
        """
        Washington Martha F Blue 06/13/1731
        Washington George M Red 02/22/1732
        Becquerel Antoine M Red 12/15/1852
        Curie Pierre M Yellow 05/15/1859
        Curie Marie F Green 11/07/1867
        Smith Juliet F Green 08/10/1979
        Smith Joe M Orange 09/08/1980
        Doe John M Blue 05/05/1990
        Doe Jane F Purple 04/07/1992
        """

Scenario: All files sorted by name
    Given the example file records.csv
    Given the example file records.psv
    Given the example file records.ssv
    When I sort by name
    Then the output should match
        """
        Washington Martha F Blue 06/13/1731
        Washington George M Red 02/22/1732
        Smith Juliet F Green 08/10/1979
        Smith Joe M Orange 09/08/1980
        Doe John M Blue 05/05/1990
        Doe Jane F Purple 04/07/1992
        Curie Pierre M Yellow 05/15/1859
        Curie Marie F Green 11/07/1867
        Becquerel Antoine M Red 12/15/1852
        """