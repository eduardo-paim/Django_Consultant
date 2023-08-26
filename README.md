# Django_Consultant

## Descrição

Stack Tecnológico

Django
Django Celery
Django Rest Framework
Requisitos

Os usuários devem poder solicitar empréstimos.
Os empréstimos devem ser analisados por uma API de terceiros.
Os empréstimos aprovados devem ser disponibilizados para os usuários.
Implementação

Os principais trechos de código para atender aos requisitos são os seguintes:

Criação do Modelo de Proposta

- Um modelo de proposta é criado para armazenar as informações de cada solicitação de empréstimo. O modelo inclui os seguintes campos:

* campos: Campos flexíveis definidos pelo admin
* status: Status da proposta
* resultado_analise: Resultado da análise
Interface de Preenchimento de Propostas
Uma interface de preenchimento de propostas é criada para permitir que os usuários solicitem empréstimos. A interface inclui um formulário com os campos definidos no modelo de proposta.

API para Criação de Propostas

- Uma API é criada para permitir que os usuários solicitem empréstimos. A API recebe as informações do formulário de preenchimento de propostas e as salva no modelo de proposta.

Configuração do Celery para Análise Assíncrona

- O Celery é utilizado para realizar a análise dos empréstimos de forma assíncrona. A API chama uma tarefa do Celery para enviar a proposta para análise.

Integração com a API de Análise de Crédito

- A API de análise de crédito é utilizada para avaliar o risco de cada solicitação de empréstimo. A tarefa do Celery chama a API de análise de crédito com as informações da proposta.

Django Admin para Gerenciamento

- O Django Admin é utilizado para gerenciar as propostas de empréstimo. O admin inclui uma página para visualizar e editar as propostas.
