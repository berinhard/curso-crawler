#coding:utf-8
import pickle

class Person():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __unicode__(self):
        return '%(nome)s - %(idade)d' % self.__dict__

alice = Person('Alice', 24)

pickled_alice = pickle.dumps(alice)
print u'Conteúdo serializado por pickle: %s' % pickled_alice

alice_again = pickle.loads(pickled_alice)
print u'\nConteúdo deserializado por pickle: %s' % alice_again
