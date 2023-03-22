*** Settings ***
Documentation  API Testing in Robot Framework for [people] endpoint.
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

Resource    variables.robot


*** Test Cases ***
Get all peoples
    [Documentation]     Get all existed peoples
    [Tags]    smoke
    ${resp}=    GET    ${all_peoples}
    Status Should Be    200    ${resp}
    ${name}=    Get Value From Json     ${resp.json()}[0]  name
    ${name_from_list}=  Get From List   ${name}  0
    Should be equal  ${name_from_list}  Luke Skywalker


Get second in peoples list
    [Documentation]     Get second in peoples list
    [Tags]    smoke
    ${resp}=    GET    ${all_peoples}/2
    Status Should Be    200    ${resp}
    ${name}=    Get value from JSON    ${resp.json()}    $.name
    Should be equal  ${name[0]}  C-3PO


Get unexisted people
    [Documentation]     Get unexisted people
    [Tags]    smoke
    ${resp}=    GET    ${all_peoples}/200   builtin.run keyword and expect error    404
