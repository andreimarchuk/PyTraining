Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname | lastname |
  | test_firstname_bdd | test_lastname_bdd |

Scenario: Delete some contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact

Scenario Outline: Edit some contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname>
  When I edit the contact from the list
  Then the new contact list is equal to the old list with edited contact

    Examples:
  | firstname | lastname |
  | testedit_firstname_bdd | testedit_lastname_bdd |