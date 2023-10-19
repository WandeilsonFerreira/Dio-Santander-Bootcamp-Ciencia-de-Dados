
<center>
    
   ![](./Assets/0.png)
 
</center>

## Descrição do desafio módulo – Processamento de Dados Simplificado com Power BI
1. Criação de uma instância na Azure para MySQL
    <center>

    ![](./Assets/1.png)

    </center>
1. Criar o Banco de dados com base disponível no github
    <center>

    ![](./Assets/2.png)

    </center>
1. Integração do Power BI com MySQL no Azure 
    <center>

    ![](./Assets/3.png)

    </center>

1. Verificar problemas na base a fim de realizar a transformação dos dados
Diretrizes para transformação dos dados
    <center>

    ![](./Assets/4.png)

    </center>

1. Verifique os cabeçalhos e tipos de dados    
    <center>

    ![](./Assets/5.png)

    </center>

1. Modifique os valores monetários para o tipo double preciso
    <center>

    ![](./Assets/6.png)

    </center>

1. Verifique a existência dos nulos e analise a remoção
    <center>

    ![](./Assets/7.png)

    </center>   
    
1. Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente
    <center>

    ![](./Assets/8.png)

    </center>

1. Verifique se há algum departamento sem gerente
    <center>

    ![](./Assets/9.png)

    </center>

1. Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas
    <center>

    ![](./Assets/9.png)

    </center>

1. Verifique o número de horas dos projetos
    <center>

    ![](./Assets/10.png)

    </center> 

1. Separar colunas complexas
    <center>

    ![](./Assets/11.png)

    </center> 

1. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção
    <center>

    ![](./Assets/11.png)

    </center> 
1. Neste processo elimine as colunas desnecessárias. 
     <center>

    ![](./Assets/13.png)

    </center> 

1. Realize a junção dos colaboradores e respectivos nomes dos gerentes . Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.
    <center>

    ![](./Assets/13.png)

    </center> 
1. Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores
    <center>

    ![](./Assets/14.png)

    </center> 
1. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.
    <center>

    ![](./Assets/16.png)

    </center> 
1. Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir. 
- A diferença basica entre mesclar e atribuir esta na forma que eles relacionam as colunas, este trata as linhas e outro as colunas. 

1. Agrupe os dados a fim de saber quantos colaboradores existem por gerente
    <center>

    ![](./Assets/17.png)

    </center> 

1. Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tabela

    <center>

    ![](./Assets/18.png)

    </center> 