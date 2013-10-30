#!/usr/bin/python2.7
import subprocess
from subprocess import Popen

#utiliza a lib subprocess do core do python para chamar processos filhos
#a chamada de um proximo processo so e feita apos o encerramento do anterior
#devido o metodo call ser uma abstracao do Popen(args).wait() que nada mais e
#que: Popen -> executa processo de acordo com os argumentos passados e wait()
#espera o termino da execucao do processo
subprocess.call('gnome-terminal')
subprocess.call('gimp')
subprocess.call('mine')
subprocess.call('firefox')

#abaixo e mostrado como deve ser feito para abrir subprocessos simultaneos
#utilizamos diretamente a Popen e omitimos o funcao em cascada wait()
Popen('gnome-terminal')
Popen('firefox')
Popen('mine')
Popen('gimp')