import time
# While es otra estructura de control que repite pasos. Es similar al for. Pdemos entenderla como 'mientras'

counter = 0
while counter < 5:
    print(counter)
    time.sleep(0.5)
    counter = counter + 1