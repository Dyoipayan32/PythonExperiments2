*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Library    BuiltIn
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***
Do a GET Request and validate the response code and response body
    [documentation]  This test case verifies that the response code of the GET Request should be 200,
    ...  the response body contains the 'title' key with value as 'quis ut nam facilis et officia qui',
    [tags]  Smoke
    Create Session  mysession  https://jsonplaceholder.typicode.com  verify=false
    ${response}=  GET On Session  mysession  /todos/  params=id=2
    Status Should Be  200  ${response}  #Check Status as 200

    #Check Title as quis ut nam facilis et officia qui from Response Body
    ${title}=  Get Value From Json  ${response.json()}[0]  title
    Log   ${title}
    ${titleFromList}=  Get From List   ${title}  0
    Log   ${titleFromList}
    Should be equal  ${titleFromList}  quis ut nam facilis et officia qui

    #Check userId is present in the repsonse body
    ${body}=  Convert To String  ${response.content}
    Log    ${body}
    Should Contain  ${body}  userId