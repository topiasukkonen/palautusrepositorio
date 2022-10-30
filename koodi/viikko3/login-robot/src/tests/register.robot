*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  kallea  validPass123
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kallea  Kalle123
    Input New Command
    Input Credentials  kallea  Kalle123
    Output Should Contain  User with username kallea already exists
Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kKlle123
    Output Should Contain  Too short username
Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kallea  kal
    Output Should Contain  Too short password
Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kallea  kallekallekallekalle
    Output Should Contain  Password must contain at least one number
