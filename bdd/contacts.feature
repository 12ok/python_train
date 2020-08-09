Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename> and <lastname>
  When I add the contact to the list
  Then the new list is equal to the old list with the added contact

  Examples:
  | firstname | middlename | lastname |
  | Olga      | Ivanovna   | Petrova  |
  | Alexander | Olegovich  | Sidorov  |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new list is equals to the old list without the delete contact

Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <middlename> and <lastname>
  When I modify the contact from the list
  Then the new list is equals to the old list with modify contact

  Examples:
  | firstname | middlename | lastname |
  | Alla      | Petrovna   | Suvorova |

