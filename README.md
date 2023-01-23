
<p align="center">
  <img src="https://raw.githubusercontent.com/AndersonAyache/AluraVoz/main/IMG/Logo_Alura_Voz.png#vitrinedev"> 
</p>


# Alura Voz - Challenge de Data Science 

Bem-vindo ao projeto de portfólio de Data Science "Alura Voz"! Este projeto foi criado com o objetivo de demonstrar minhas habilidades e conhecimentos na área de limpeza, análise e modelagem de dados. O projeto é dividido em três etapas: limpeza dos dados, análise dos dados e criação de um modelo de machine learning. Os arquivos estão organizados em pastas específicas para cada etapa.



| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Análise da taxa de cancelamento da Alura voz**
| :label: Tecnologias | Python
| :rocket: URL         |[Alura Voz](https://github.com/AndersonAyache/AluraVoz)
| :fire: Desafio     | [Alura Challenges - Alura Voz](https://www.alura.com.br/challenges/data-science)


## Detalhes do projeto

O programa de desafios, da Alura, é uma oportunidade para colocar em prática o que foi aprendido em seus cursos de tecnologia. Ele tem como objetivo simular uma situação de trabalho real, onde é necessário entregar um projeto para uma empresa fictícia, nesse caso a Alura Voz, uma empresa de telecomunicações que deseja compreender os cancelamentos de seus clientes.

# Etapas
## Limpeza dos dados
A etapa de limpeza e preparação dos dados é crucial para garantir que as informações analisadas sejam precisas e confiáveis. Durante essa etapa, foram realizadas ações como remoção de valores faltantes, correção de dados incorretos e formatação dos dados para facilitar a análise. Essas ações garantem que a equipe de vendas esteja trabalhando com informações precisas, o que é fundamental para tomar decisões estratégicas e alcançar os objetivos da empresa. Além disso, ao remover dados inconsistentes ou incorretos, a equipe de vendas pode se concentrar nas informações mais relevantes e importantes para suas decisões, o que aumenta a eficiência e a eficácia de suas ações.

## Análise dos dados
Após a limpeza dos dados, realizar uma análise destes dados é crucial para entender as tendências e padrões existentes e, assim, obter insights valiosos para ajudar a equipe de vendas a enquadrar novos clientes em planos que terão maiores chances de permanência. Foram utilizadas técnicas estatísticas e visualizações de dados para identificar as relações entre as variáveis e compreender as tendências do mercado. Como resultado, foi possível observar que 1869 clientes, ou seja, aproximadamente **26,54%** de todos os clientes observados neste estudo, efetuaram o cancelamento, o que representa uma taxa relativamente alta.

<p align="center">
  <img src="https://raw.githubusercontent.com/AndersonAyache/AluraVoz/main/IMG/cancalamento_total.png">
</p>

Também nesta etapa, foi observada a relação entre o tipo de serviço de internet e a tendência de cancelamento. Os clientes que usam fibra óptica têm uma tendência maior de cancelar do que os clientes que utilizam DSL ou aqueles que não possuem internet. Além disso, ao analisarmos o serviço de telefone, foi observado que a tendência de cancelamento dos clientes que usam o serviço é aproximadamente 10 vezes maior do que a dos clientes que não usam.

<p align="center">
  <img src="https://raw.githubusercontent.com/AndersonAyache/AluraVoz/main/IMG/cancalamento_serico_telefonico.png">
</p>

Outra análise importante realizada foi a relação entre o uso de StreamingTV e StreamingMovies e a tendência de cancelamento, onde foi observado que esses serviços têm uma taxa de cancelamento acima de 40%. No entanto, não foi observada diferença significativa no cancelamento entre homens e mulheres, nem que os idosos cancelem mais frequentemente. Além disso, foi possível ver que as pessoas com cônjuge ou dependentes têm uma tendência menor de cancelar. Por último, mas não menos importante, foi observado que os clientes novos têm um alto índice de cancelamento, especialmente aqueles que têm gastos elevados.

<p align="center">
  <img src="https://raw.githubusercontent.com/AndersonAyache/AluraVoz/main/IMG/tabela_de_servicos.png">
</p>

Já quando se fala de tempo de permanência como cliente e a tendência de cancelamento, se observa que os clientes mais novos tendem a cancelar. Isso pode sugerir que os clientes novos podem estar experimentando os serviços da empresa e decidindo se eles atendem às suas necessidades, e se não atenderem, eles tendem a cancelar.

Além disso, foi observada uma relação entre o gasto mensal dos clientes e a tendência de cancelamento. Foi constatado que os clientes que cancelam têm gastos mensais mais altos em comparação com os clientes que não cancelam.

<p align="center">
  <img src = "https://raw.githubusercontent.com/AndersonAyache/AluraVoz/main/IMG/violino_gasto_total.png", width = 60%>
</p>

Por outro lado, é importante observar a relação entre o gasto total dos clientes e a tendência de cancelamento. Nossa análise mostrou que os clientes que cancelaram os serviços possuem gastos totais significativamente menores do que os clientes que não cancelaram. Isso sugere que esses clientes podem estar cancelando devido à falta de necessidade dos serviços, insatisfação com o valor pago, ou até mesmo pela qualidade do serviço prestado. Essa descoberta tem grande valor para a empresa, pois permite identificar e compreender as principais razões pelas quais os clientes estão cancelando os serviços, possibilitando assim, a implementação de medidas para melhorar a retenção de clientes.


## Criação do modelo de machine learning
Nesta etapa, um modelo de machine learning é criado com base nos insights obtidos na etapa anterior de análise de dados. Isso inclui a seleção de algoritmos adequados, treinamento e avaliação do modelo para garantir sua precisão e capacidade de generalização.

Os algoritmos utilizados foram:


<table align="center">
  <tr>
    <th>Nome completo do modelo</th>
    <th>Abreviação</th>
  </tr>
  <tr>
    <td>K-Nearest Neighbors</td>
    <td>knn</td>
  </tr>
  <tr>
    <td>Support Vector Machine</td>
    <td>svc</td>
  </tr>
  <tr>
    <td>Decision Tree</td>
    <td>dtree</td>
  </tr>
  <tr>
    <td>Random Forest</td>
    <td>rforest</td>
  </tr>
    <td>Naive Bayes</td>
    <td>bnb</td>
  </tr>
</table>  
    

</table>
Com base nos resultados obtidos ao avaliar diferentes modelos, é possível afirmar que o modelo K-Nearest Neighbors (KNN) se destaca como a melhor opção para prever o comportamento de cancelamento de clientes da "Alura Voz". Como mostra na tabela apresentada, o KNN obteve os melhores resultados em quase todas as métricas avaliadas, superando os demais modelos e se mostrando como a escolha mais adequada para atender as necessidades da empresa.

Com isso, o KNN é capaz de prever com maior precisão os clientes que têm tendência a cancelar o serviço, o que é importante para a empresa "Alura Voz" que fornece serviços de telefonia e internet. Além disso, o modelo KNN é conhecido por ser um dos algoritmos mais simples e fáceis de entender, o que facilita a interpretação dos resultados obtidos e a implementação de medidas para melhorar a retenção de clientes.

Portanto, levando em consideração esses resultados e as necessidades da empresa "Alura Voz", o KNN é o modelo escolhido como o melhor para prever o comportamento de cancelamento de clientes.
