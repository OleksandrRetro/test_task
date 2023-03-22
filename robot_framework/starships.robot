*** Settings ***
Documentation  API Testing in Robot Framework for [starships] endpoint.
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

Resource    variables.robot


*** Test Cases ***
Get all starships
    [Documentation]     Get all existed starships
    [Tags]    smoke
    ${resp}=    GET    ${all_starships}
    Status Should Be    200    ${resp}
    ${name}=    Get Value From Json     ${resp.json()}[0]  name
    ${name_from_list}=  Get From List   ${name}  0
    Should be equal  ${name_from_list}  Star Destroyer


Get first in starships list
    [Documentation]     Get first in starships list
    [Tags]    smoke
    ${resp}=    GET    ${all_starships}/1
    Status Should Be    200    ${resp}
    ${name}=    Get value from JSON    ${resp.json()}    $.name
    Should be equal  ${name[0]}  CR90 corvette


Get unexisted starships
    [Documentation]     Get unexisted starships
    [Tags]    smoke
    ${resp}=    GET    ${all_starships}/200   builtin.run keyword and expect error    404
