"""
Exercício de Programação de Inteligência Artificial
Professora Doutora Patrícia Rufino Oliveira

Autores:
Lucas Borelli Amaral                9360951
Paulo Henrique Freitas Guimarães    9390361
Silas Rocha Pereira                 9424079
Victor Taendy Sousa Emerenciano     8921421

Módulo responsável por fazer interações com arquivos
"""



# Módulos necessários
from anytree.exporter import JsonExporter



def write_arvore_no_arquivo(arvore, arquivo):
    """
    Escreve a @arvore no @arquivo
    """
    exporter = JsonExporter(indent=2, sort_keys=True)
    json = exporter.export(arvore)

    with open(arquivo, 'w') as obj_file:
        obj_file.write(json)



def write_conjunto_no_arquivo(conjunto, arquivo, encoding='utf-8'):
    """
    Escreve o @conjunto no @arquivo usando o @encoding
    """
    conjunto.to_csv(arquivo, encoding=encoding, index=False)



def write_saida(acuracia, arquivo, numero_nos):
    """
    Escreve a @acuracia e o @numero_nos no @arquivo no formato CSV
    """
    with open(arquivo, 'a') as obj_file:
        obj_file.write('{0}, {1}'.format(acuracia, numero_nos) + '\n')



def write_regras(arquivo, string_de_regras):
    """
    Escreve a @string_de_regras no @arquivo no formato TXT
    """
    with open(arquivo, 'w') as obj_file:
        obj_file.write(string_de_regras)


