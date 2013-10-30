#!/usr/bin/python2.7
import subprocess

#utiliza a lib subprocess do core do python para chamar processos filhos
#a chamada de um próximo processo só é feita após o encerramento do anterior
#devido o método call ser uma abstração do Popen(args).wait() que nada mais é
#que: Popen -> executa processo de acordo com os argumentos passados e wait()
#espera o término da execução do processo
subprocess.call('gnome-terminal')
subprocess.call('gimp')
subprocess.call('mine')
subprocess.call('firefox')