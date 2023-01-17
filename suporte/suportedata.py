import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score ,confusion_matrix
from matplotlib.colors import LinearSegmentedColormap


# revela as valores das variaveis
def tipo_variaveis(coluna):
    for i in coluna.columns:
        print(f'Valores da variável {i} --> {coluna[i].unique()} \n')


# visualizar lista depois da normalização
def visualizar(lista):
    for data in lista:
        display(data.head())
    
    

# plot de comparação para balanceamento
def plot_comparacao(data, x,title=None, xlabel=None, figsize=None, xticks=None):
    # escondendo os eixos da direta e do topo
    custom_params = {"axes.spines.right": False, "axes.spines.top": False}

    # definindo o tema e o tamanho do gráfico
    sns.set_theme(style="white", rc=custom_params)
    if figsize == None:
        figsize =(8,6)
        
    plt.figure(figsize=figsize)     

    # plotando o gráfico
    g = sns.countplot(x=x, data=data, palette=['#154580','#82D712'])

    # adicionando título e rótulos aos eixos
    g.set_title(title,x = 0.6, ha= 'center' , fontsize = 22, pad=25)
    g.set_xlabel(xlabel, fontsize=14)
    g.set_ylabel('Quantidade', fontsize=14)

    #mudando os valores de entrada
    if xticks != None:
        g.set_xticklabels(xticks)
    
    # adicionando o valor a cada categoria
    categorias = data[x].unique()
    for i, categoria in enumerate(categorias):
        count = data[data[x] == categoria].shape[0]
        g.annotate(count, (i, count-300), ha='center', va='center', fontsize=15, color='w')
    
    # exibindo o Gráfico
    plt.show()



# criação da matriz de confusão
def matriz_confusao(y_true_teste, y_pred_teste, group_names=None,
                         categories='auto', count=True, cbar=True,
                         xyticks=True, sum_stats=True, figsize=None,
                         title=None):

    cf = confusion_matrix(y_true_teste, y_pred_teste)
    custom_cmap = LinearSegmentedColormap.from_list(name='custom', colors=['#82D712', '#154580'], N=256)    
    
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names) == cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    box_labels = [f"{v1}{v2}".strip()
                  for v1, v2 in zip(group_labels, group_counts)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    if sum_stats:

        accuracy = accuracy_score(y_true_teste, y_pred_teste)
        precision = precision_score(y_true_teste, y_pred_teste)
        recall = recall_score(y_true_teste, y_pred_teste)
        f1_score_metric = f1_score(y_true_teste, y_pred_teste)

        stats_text = "\n\nAcurácia={:0.3f}\nPrecisão={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
            accuracy, precision, recall, f1_score_metric)
    else:
        stats_text = ""

    if figsize == None:
        figsize = (10,7)

    if xyticks == False:
        categories = False

    plt.figure(figsize= figsize)
    sns.set(font_scale=1.4)  # for label size
    sns.heatmap(cf, annot=box_labels, fmt="", cmap=custom_cmap, cbar=cbar,
                xticklabels=categories, yticklabels=categories)
    plt.ylabel('Valores verdadeiros', fontsize=16)
    plt.xlabel('Valores preditos' + stats_text, fontsize=16)

    if title:
        plt.title(title, fontsize=20)

        
def compara_modelos_metricas(metrica, nomes_modelos, y_true_treino, y_pred_treinos, y_true_teste, y_pred_testes):
    """
    metrica: {'Acurácia Treino', 'Acurácia Teste', 'Precisão', 'Recall', 'F1-Score'}
    Returns:
        DataFrame ordenado de acordo com a métrica passada. 
    """
    knn = []
    bnb = []
    acc = []
    precision = []
    recall = []
    f1 = []

    for y_pred_teste in y_pred_testes:
        knn.append(accuracy_score(y_true_teste, y_pred_teste))
        bnb.append(accuracy_score(y_true_teste, y_pred_teste))
        acc.append(accuracy_score(y_true_teste, y_pred_teste))
        precision.append(precision_score(y_true_teste, y_pred_teste))
        recall.append(recall_score(y_true_teste, y_pred_teste))
        f1.append(f1_score(y_true_teste, y_pred_teste))

    acc_treino = []
    for y_pred_treino in y_pred_treinos:
        acc_treino.append(accuracy_score(y_true_treino, y_pred_treino))

    tabela = pd.DataFrame({'Modelo': nomes_modelos,  'Acurácia Treino': acc_treino,
                          'Acurácia Teste': acc, 'Precisão': precision, 'Recall': recall, 'F1-Score': f1})

    return tabela.sort_values(by=metrica, ascending=False).reset_index(drop=True)
