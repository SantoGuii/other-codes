class no:
    def __init__(self, v):
        self.valor = v
        self.prox = None

class lista:
    def __init__(self):
        self.cabeca = None
        self.len = 0
    def __str__(self):
        s = '['
        atual = self.cabeca
        while atual != None:
            s = s + str(atual.valor) + ','
            atual = atual.prox
        if s != '[':
            s = s[:-1]
        s = s + ']'
        return s
    
    def __len__(self):
        return self.len
    
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, indice):
        if indice > self.len-1:
            raise IndexError("Indice excede len-1!")
        else:
            atual = self.cabeca
            for _ in range(indice):
                atual = atual.prox
            return atual.valor
        
    def __setitem__(self, indice, v):
        if indice > self.len-1:
            raise IndexError("Indice excede len-1!")
        else:
            atual = self.cabeca
            for _ in range(indice):
                atual = atual.prox
            atual.valor = v
            
    def push_right(self, v):
        meu_no = no(v)
        if self.cabeca == None:
            self.cabeca = meu_no
            self.len = self.len + 1
        else:
            atual = self.cabeca
            while atual.prox != None:
                atual = atual.prox
            atual.prox = meu_no
            self.len = self.len + 1
            
    def pop_right(self):
        if self.cabeca == None:
            raise IndexError("Lista vazia!")
        elif self.cabeca.prox == None:
            v = self.cabeca.valor
            self.cabeca = None
            self.len = self.len - 1
            return v
        else:
            atual = self.cabeca
            anterior = self.cabeca
            while atual.prox != None:
                anterior = atual
                atual = atual.prox
            v = atual.valor
            anterior.prox = None
            self.len = self.len - 1
            return v
        
    def push_left(self,v):
        meu_no = no(v)
        meu_no.prox = self.cabeca
        self.cabeca = meu_no
        self.len = self.len + 1
        
    def pop_left(self):
        if self.cabeca == None:
            raise IndexError("Lista vazia!")
        else:
            v = self.cabeca.valor
            self.cabeca = self.cabeca.prox
            self.len = self.len - 1
            return v
        
p = lista()
p.push_right(2)
p.push_right(3)
p.push_left(5)
p.push_right(4)
print(p)
print(p.pop_right())
print(p)
#print(p.pop_left())
print(p)
#print(p.pop_right())
print(p)
print(p.pop_left())
print(p)
