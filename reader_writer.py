#!/usr/bin/python2.7
import thread
import time
import random

#semaforo file_lock a lib de thread faz o controle por si nao precisa de
# interferencia do usuario quando nao e possivel adquirir o lock
file_lock_read = thread.allocate_lock()
file_lock_write = thread.allocate_lock()


def sleep(process):
    seconds = random.randint(5, 10)
    message = 'Processo {0}, aguardando por {1}'.format(process, seconds)
    print message
    time.sleep(seconds)


def read(reader_number):
    print 'Leitor {0} tentando adquirir semaforo file_lock'.format(reader_number)
    if file_lock_read.acquire():
        #abre arquivo para leitura
        file_locked = open('text1', 'r')
        content = file_locked.read()
        file_locked.close()
        print content
        print 'Arquivo lido pelo Leitor {0} liberando file_lock'.format(reader_number)
        #aguarda um pouco pra liberar o file_lock
        sleep('Leitor {0}'.format(reader_number))
        file_lock_read.release()
    else:
        print 'Arquivo bloqueado para Leitor {0}'.format(reader_number)
    sleep('Leitor {0}'.format(reader_number))


def reader_1():
    while True:
        read(1)


def reader_2():
    while True:
        read(2)


def reader_3():
    while True:
        read(3)


def write(writer_number):
    print 'Escritor {0} tentando adquirir semaforo file_lock'.format(writer_number)
    if file_lock_read.acquire() and file_lock_write.acquire():
        #abre arquivo para leitura
        file_locked = open('text1', 'r')
        content = file_locked.readlines()
        file_locked.close()
        #abre arquivo para escrita
        file_locked = open('text1', 'w')
        content.append('Arquivo alterado por Escritor {0}'.format(writer_number))
        file_locked.writelines(content)
        file_locked.close()
        print content
        print 'Arquivo lido pelo Escritor {0} liberando file_lock'.format(writer_number)
        #espera um pouco antes de liberar o file_lock
        sleep('Escritor {0}'.format(writer_number))
        file_lock_read.release()
        file_lock_write.release()
    else:
        print 'Arquivo bloqueado para Escritor {0}'.format(writer_number)
    sleep('Escritor {0}'.format(writer_number))


def writer_1():
    while True:
        write(1)


def writer_2():
    while True:
        write(2)

#inicia as threads
thread.start_new_thread(reader_1, ())
thread.start_new_thread(reader_2, ())
thread.start_new_thread(reader_3, ())
thread.start_new_thread(writer_1, ())
thread.start_new_thread(writer_2, ())

while True: pass