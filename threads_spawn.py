#!/usr/bin/python2.7
import thread
import time
import random
#em python todas as threads sao threads de kernel apesar de terem algumas
#restricoes para interagir com algumas bibliotecas C, oq faz com que sejam
#pessimas para multicore pq mesmo coom 4 cores apenas 1 instrucao python pode
#ser executada por vez ou seja os outros 3 cores ficariam a maior parte do tempo
#bloqueados


def sleep(process):
    seconds = random.randint(5, 10)
    message = 'Processo {0}, aguardando por {1}'.format(process, seconds)
    print message
    time.sleep(seconds)


def thread_kernel_1():
    while True:
        sleep(1)


def thread_kernel_2():
    while True:
        sleep(2)


def thread_kernel_3():
    while True:
        sleep(3)


def thread_kernel_4():
    while True:
        sleep(4)


def thread_kernel_5():
    while True:
        sleep(5)

#inicia as threads
thread.start_new_thread(thread_kernel_1, ())
thread.start_new_thread(thread_kernel_2, ())
thread.start_new_thread(thread_kernel_3, ())
thread.start_new_thread(thread_kernel_4, ())
thread.start_new_thread(thread_kernel_5, ())

while True: pass