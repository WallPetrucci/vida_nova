*** Settings ***
Documentation   Essa suite de teste tem como objetivo testar a API da Marvel.
            ... Como forma de estudo da automação de Testes de API para o vida Nova.

Resource        marvel_char.resource
Suite Setup     Criar Configuracao Inicial do Teste

*** Test Cases ***
Testar API Char da Marvel 
    Realizar requisicao GET na /v1/public/characters
    Validar se status code retornou 200
    Validar se a chave "code" esta preenchida
    Validar se a chave "copyright" esta preenchida

