Shopify Manager
===============

<div align="center">
  <img src="https://i.ibb.co/mNn8WJT/icon.png" alt="Ícone da Shopify Tools">   
</div>
<br />
<p align="center">
  <a href="https://github.com/Kockiee/Shopify-Tools/releases/tag/v1.0.0">
    <img src="https://img.shields.io/badge/Download-v1.0.0-brightgreen.svg" alt="Download">
  </a>
  <a href="https://github.com/Kockiee/Shopify-Tools/stargazers">
    <img src="https://img.shields.io/github/stars/Kockiee/Shopify-Tools.svg?style=social&label=Stars" alt="GitHub stars">
  </a>
  <a href="https://github.com/Kockiee/Shopify-Tools/network">
    <img src="https://img.shields.io/github/forks/Kockiee/Shopify-Tools.svg" alt="Forks">
  </a>
</p>

### Introdução

Bem-vindo ao Shopify Manager! Este script em Python foi desenvolvido para facilitar a gestão de uma loja Shopify, permitindo a atualização de preços, comparações de preços, estoque e consulta de informações. Abaixo, você encontrará instruções sobre como utilizar as diferentes funcionalidades do programa.

OBS: Fiz este script para melhorar minhas habilidades com Python apenas, não me importo com o que você pode fazer com esse código, apenas peço que mantenha-o gratuito.

### Requisitos

Antes de começar, certifique-se de ter instalado os seguintes pacotes Python:

bashCopy code

```
pip install --upgrade ShopifyAPI          
pip install prettytable           
pip install pyactiveresource            
```

### Configuração Inicial

Ao iniciar o programa, você será solicitado a fornecer algumas informações necessárias para a autenticação na loja Shopify. Digite a URL original da loja (Ex: `myshop.myshopify.com`) e o Token de App (certifique-se de criar um app com todas as permissões necessárias).

### Funcionalidades Principais

1.  **Atualizar preços de uma coleção**
    
    *   Opção: `1`
    *   Informe o ID da coleção e a porcentagem de ajuste de preço (negativa para subtrair, positiva para adicionar).
2.  **Atualizar preços de um produto**
    
    *   Opção: `2`
    *   Informe o ID do produto e a porcentagem de ajuste de preço (negativa para subtrair, positiva para adicionar).
3.  **Consultar produtos de uma coleção**
    
    *   Opção: `3`
    *   Informe o ID da coleção para visualizar os produtos associados.
4.  **Atualizar comparações de preços de uma coleção**
    
    *   Opção: `4`
    *   Informe o ID da coleção e a porcentagem de ajuste nas comparações de preços.
5.  **Atualizar comparação de preços de um produto**
    
    *   Opção: `5`
    *   Informe o ID do produto e a porcentagem de ajuste nas comparações de preços.
6.  **Consultar produto pelo ID**
    
    *   Opção: `6`
    *   Informe o ID do produto para visualizar as informações detalhadas.
7.  **Atualizar em massa estoque das variantes de um produto**
    
    *   Opção: `7`
    *   Informe o ID do produto, a nova quantidade em estoque e o nome da localização.
8.  **Atualizar estoque de uma variante de um produto**
    
    *   Opção: `8`
    *   Informe o ID da variante, a nova quantidade em estoque e o nome da localização.

### Encerrando o Programa

A qualquer momento, você pode encerrar o programa pressionando `Ctrl + C`. Certifique-se de evitar interrupções durante a execução de uma função para evitar problemas.

Lembre-se de que nenhuma informação é salva localmente, garantindo a segurança dos dados. Em caso de dúvidas ou problemas, entre em contato com o suporte técnico.

**Aproveite a gestão simplificada da sua loja Shopify com o Shopify Manager!**
