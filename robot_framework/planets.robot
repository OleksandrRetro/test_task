*** Settings ***
Documentation  API Testing in Robot Framework for [planets] endpoint.
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

Resource    variables.robot


*** Test Cases ***
Get all planets
    [Documentation]     Get all existed planets
    [Tags]    smoke
    ${resp}=    GET    ${all_planets}
    Status Should Be    200    ${resp}
    ${name}=    Get Value From Json     ${resp.json()}[0]  name
    ${name_from_list}=  Get From List   ${name}  0
    Should be equal  ${name_from_list}  Yavin IV


Get second in planets list
    [Documentation]     Get second in planets list
    [Tags]    smoke
    ${resp}=    GET    ${all_planets}/2
    Status Should Be    200    ${resp}
    ${name}=    Get value from JSON    ${resp.json()}    $.name
    Should be equal  ${name[0]}  Alderaan


Get unexisted planets
    [Documentation]     Get unexisted planets
    [Tags]    smoke
    ${resp}=    GET    ${all_planets}/200   builtin.run keyword and expect error    404
