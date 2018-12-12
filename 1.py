'''
Escreva um programa em Python que:

    A - obtenha a lista de processes executando no momento, considerando que o processo pode deixar de
    existir enquanto seu programa manipula suas informações;
    B - imprima o nome do processo e seu PID;
    C - imprima também o percentual de uso de CPU e de uso de memória.
'''
import psutil

try:
    processes = psutil.pids()
    for p in processes:

        process_list = psutil.Process(p)
        name = process_list.name()
        m = round(process_list.memory_percent(), 2)
        cpu = int(process_list.cpu_percent(interval=1.0))

        print("Nome: {:<20}   Pid: {:<10}   Memoria: {:>3}%  CPU: {}".format(name, p, m, cpu))
except Exception as NoSuchProcess:
    print(NoSuchProcess)


