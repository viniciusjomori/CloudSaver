# Cloud Saver

Relatório de custos da *AWS*, desenvolvido com *Lambda*, *CDK* e *Pandas*

## Como Funciona

Uma ou mais vezes ao dia, uma *AWS Lambda* é invocada. Ela consulta todos os serviços consumidos por uma conta AWS e os seus custos, através do serviço *Cost Explorer*, e cria uma tabela com a relação. Em seguida, a tabela é enviada por email, sendo um resumo no corpo e o detalhamento total em anexo.

### Exemplo:

<table>
  <tr>
    <th>SERVIÇO</th>
    <th>VALOR</th>
    <th>MOEDA</th>
  </tr>
  <tr>
    <td>Amazon EC2</td>
    <td>300.00</td>
    <td>USD</td>
  </tr>
  <tr>
    <td>Amazon S3</td>
    <td>10.00</td>
    <td>USD</td>
  </tr>
  <tr>
    <td>AWS Cost Explorer</td>
    <td>0.32</td>
    <td>USD</td>
  </tr>
  <tr>
    <td>TOTAL</td>
    <td>310.32</td>
    <td>USD</td>
  </tr>
</table>

## Deploy

### Ambiente
* Na raiz do projeto, crie um diretório chamado `env`
* Nesse diretório, crie um arquivo `.json`. O nome do arquivo será o nome do ambiente. Exemplo: `env/dev.json` -> "*dev*" é o nome do ambiente.
* No Json, coloque essas informações:

```
{
  "schedule": {
    "hour": "Horário de agendamento",
    "minute": "Minutagem de agendamento"
  },
  "email": {
    "user": "Usuário do email",
    "password": "Senha do email",
    "name": "Nome do email a enviar o relatório",
    "from": "Endereço de email a enviar o relatório",
    "smtp": "Endereço SMTP",
    "port": "Porta do endereço SMTP. Geralmente, 587",
    "to": ["Emails a receber o relatório"],
    "cc": ["Emails a receber o relatório (via cópia)"],
    "cco": ["Emails a receber o relatório (via cópia oculta)"]
  },
  "format": {
    "header": {
      "bgColor": "Cor de fundo do cabeçalho (hexadecimal)",
      "fontColor": "Cor da fonte do cabeçalho (hexadecimal)"
    },
    "body": {
      "odd": {
        "bgColor": "Cor de fundo das linhas pares (hexadecimal)",
        "fontColor": "Cor da fonte das linhas pares (hexadecimal)"
      },
      "even": {
        "bgColor": "Cor de fundo das linhas ímpares (hexadecimal)",
        "fontColor": "Cor da fonte das linhas ímpares (hexadecimal)"
      }
    }
  }
}
```

### Docker
* Instale o *Docker*
* Inicie o *Docker Desktop*

### AWS CLI
* Instale a *AWS CLI*
* Crie um usuário no IAM e adquira suas chaves
* No terminal, execute o comando `aws configure`, para realizar a autenticação e escolher em qual região ocorrerá o deploy

### CDK
* Instale o *Node.js* e *AWS CDK*
* Caso seja sua primeira vez usando CDK, execute o comando `cdk bootstrap`, para instanciar os recursos padrão
* Execute o comando `cdk diff`, para visualizar os recursos a serem criados para o projeto
* Após seguir todos os passos anteriores, execute o comando `cdk deploy -c env=dev --require-approval never`, para criar todos os recursos e colocar a aplicação em produção. Substitua o parâmetro "*dev*" pelo nome do ambiente.

## Tecnologias

* **AWS Lambda**: Serviço de computação serverless da AWS usado para executar automaticamente a função que gera o relatório.

* **Python**: Linguagem principal utilizada na imagem da AWS Lambda, a qual define todo o core do projeto.

* **EventBridge**: serviço de eventos da AWS. Usado para agendamento da execução da Lambda

* **Cost Explorer**: serviço da AWS para consulta e análise da fatura da nuvem.

* **Docker**: utilizado para configurar o ambiente da função Lambda, permitindo a inclusão de pacotes externos e bibliotecas nativas que não estão disponíveis no ambiente padrão da AWS.

* **CDK**: utilizado para provisionar toda a infraestrutura AWS do projeto, através de IoC (Infrastructure as Code).

* **TypeScript**: linguagem utilizada no CDK.

* **Boto3**: biblioteca Python oficial da AWS, usada para consultar informações do Cost Explorer.

* **Pandas**: biblioteca Python para manipulação de dados. Usada para analisar as informações recebidas pelo Cost Explorer.

* **AWS SES (Simple Email Service)**: serviço de emails da AWS. Esse projeto usa SMTP para o envio de relatórios, o que permite o uso do SES, porém, não é obrigatório. Você pode usar qualquer servidor SMTP (Gmail, Outlook, etc).