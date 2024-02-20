import time
import multiprocessing

def tarea(num_tarea):
    print(f"\n[+] Proceso {num_tarea} iniciado")
    time.sleep(2)
    print(f"\n[+] Proceso {num_tarea} terminado")

process1 = multiprocessing.Process(target=tarea, args=(1,))
process2 = multiprocessing.Process(target=tarea, args=(2,))

process1.start()
process2.start()

process1.join()
process2.join()

print(f"\n[+] Los procesos han terminado existosamente")