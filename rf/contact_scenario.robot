*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname  middlename  lastname
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact List Should Be Equals  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Non Empty Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List   ${old_list}   ${index}
    Delete contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact List Should Be Equals  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Non Empty Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${old_contact}=  Get From List   ${old_list}   ${index}
    ${new_contact}=  New Contact  inna  olegvna  ivanova
    Modify Contact  ${old_contact}   ${new_contact}
    ${new_list}=  Get Contact List
    Set List Value  ${old_list}  ${index}  ${new_contact}
    Contact List Should Be Equals  ${new_list}  ${old_list}
