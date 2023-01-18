<p align="center">
  <img src="https://raw.githubusercontent.com/AndersonAyache/AluraVoz/main/IMG/Logo_Alura_Voz.png">
</p>

# Introdução
Bem-vindo ao projeto de portfólio de Data Science "Alura Voz"! Este projeto foi criado com o objetivo de demonstrar minhas habilidades e conhecimentos na área de limpeza, análise e modelagem de dados. O projeto é dividido em três etapas: limpeza dos dados, análise dos dados e criação de um modelo de machine learning. Os arquivos estão organizados em pastas específicas para cada etapa.

# Etapas
## Limpeza dos dados
Nesta etapa, os dados são coletados, limpos e preparados para a análise. Isso inclui a remoção de valores faltantes, a correção de dados incorretos e a formatação dos dados para facilitar a análise. Durante esta etapa foram encontradas inconsistências, como informações em branco na variável alvo, bem como em algumas outras variáveis. Somente após essas correções, foi possível exportar o Jupyter notebook para fazer uma análise mais precisa dos dados.

## Análise dos dados
Nesta etapa, os dados limpos são analisados para obter insights e compreender a relação entre as variáveis. Isso inclui a utilização de técnicas estatísticas e visualização de dados para identificar padrões e tendências. Durante esta etapa foi possível observar que 1869 clientes, ou seja, aproximadamente **26,54%** de todos os clientes observados neste estudo, representam uma taxa relativamente alta.

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



|Nome completo do modelo | Abreviação|
|------------------------|-----------|
|K-Nearest Neighbors	   | knn       |
|Support Vector Machine	 | svc       |
|Decision Tree	         | dtree     |
|Random Forest	         | rforest   |
|Naive Bayes	           | bnb       |
