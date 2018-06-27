from collections import defaultdict

import numpy as np


class PseudoDigraph(object):
    def __init__(self, N=0):
        '''Inicializar o grafo com N vértices'''
        self.id_name = ['' for i in range(N)]
        self.name_id = {}

    def _resolve_node(self, u):
        try:
            if isinstance(u, int):
                assert 0 <= u < len(self.id_name)
            elif isinstance(u, str):
                assert u
                u = self.name_id[u]
            else:
                raise Exception

            return u
        except Exception:
            raise ValueError('O no {} não pertence ao grafo.'.format(u))

    def apend_node(self, ustr=''):
        '''Adiciona nó com nome=ustr'''
        self.name_id[ustr] = len(self.id_name)
        self.id_name.append(ustr)

    def set_node_name(self, u, ustr):
        '''Atribuir ustr ao nó u.'''
        try:
            self.id_name[u] = ustr
        except Exception as e:
            raise ValueError('O no {} não pertence ao grafo.'.format(u))

    def node_name(self, u):
        '''String atribuida ao nó u.'''
        try:
            name = self.id_name[self._resolve_node(u)]
            if name:
                return name
        except Exception as e:
            raise ValueError('O no {} não pertence ao grafo.'.format(u))

        raise ValueError('O no {} não possui um nome.'.format(u))

    def node_id(self, ustr):
        '''ID atribuida ao nó ustr.'''
        return self._resolve_node(ustr)

    def add_edge(self, u, v, simetric=False):
        '''Acrescentar um arco (u,v)'''
        raise NotImplemented()

    def adj(self, u):
        '''Lista de sucessores de u'''
        raise NotImplemented()

    def is_edge(self, u, v):
        '''Testar se existe arco (u,v)'''
        raise NotImplemented()

    @staticmethod
    def from_file(file):
        '''Ler um grafo de um arquivo'''
        raise NotImplemented()


class AdjacencyListDigraph(PseudoDigraph):
    def __init__(self, N=0):
        PseudoDigraph.__init__(self, N)
        self.adjlist = defaultdict(list)

    def add_edge(self, u, v, simetric=False):
        u = self._resolve_node(u)
        v = self._resolve_node(v)
        self.adjlist[u].append(v)
        if simetric:
            self.adjlist[v].append(u)

    def is_edge(self, u, v):
        return self._resolve_node(v) in self.adj(u)

    def adj(self, u):
        u = self._resolve_node(u)
        return self.adjlist[u]


class MatrixListDigraph(PseudoDigraph):
    def __init__(self, N=0):
        PseudoDigraph.__init__(self, N)
        self.matrix = np.zeros((N, N), dtype=np.int32)

    def add_edge(self, u, v, simetric=False):
        u = self._resolve_node(u)
        v = self._resolve_node(v)
        self.matrix[u, v] = 1
        if simetric:
            self.matrix[v, u] = 1

    def is_edge(self, u, v):
        u = self._resolve_node(u)
        v = self._resolve_node(v)
        return bool(self.matrix[u, v])

    def adj(self, u):
        u = self._resolve_node(u)
        return list(self.matrix[u, :])
