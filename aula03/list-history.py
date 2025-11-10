class ListaHistorico:

    def __init__(self, lista:list):
        self._lista = lista
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self._lista):
            raise IndexError('Índice fora do intervalo da lista!')
        return self._lista[index]
    
    def __setitem__(self, index, valor):
        if index < 0 or index >= len(self._lista):
            raise IndexError('Índice fora do intervalo da lista!')
        self._lista[index] = valor
    
    def __delitem__(self, index):
        if index < 0 or index >= len(self._lista):
            raise IndexError('Índice fora do intervalo da lista!')
        del self._lista[index]
    
    def __contains__(self, valor):
        return valor in self._lista
    
    def __len__(self):
        return len(self._lista)

if __name__ == '__main__':
    hlist = ListaHistorico(['maçã', 'banana', 'cereja'])

    print(f'Tamanho da lista: {len(hlist)}') # 3

    del hlist[1] # Deletar 'banana'
    print(f'Tamanho da lista após deleção: {len(hlist)}') # 2

    print(hlist[0]) # 'maçã'
    
    hlist[1] = 'laranja' # Alterar 'cereja' para 'laranja'
    print(hlist[1]) # 'laranja'

    print('maçã' in hlist) # True

    print('banana' in hlist) # False