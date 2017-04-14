from subprocess import call
from glob import glob
from matplotlib import pyplot as plt
from time import sleep

time_remaining = 5
count = 0
while count <= 5:
    call('bash feed_export_script.sh')
    print('%d minutes remaining...' % time_remaining)
    if count < 5:
        sleep(5)
    time_remaining -= 1
    count += 1

filenames = glob('*.csv')

eur_us_rates = []
eur_gbp_rates = []
for file in filenames:
    with open(file) as f:
        for line in f.readlines():
            if line.startswith('US'):
                eur_us_rates.append(float(line.strip().split(',')[1]))
            elif line.startswith('Brit'):
                eur_gbp_rates.append(float(line.strip().split(',')[1]))

i = 0
plt.plot(eur_us_rates)
plt.ylabel('Rate')
plt.xlabel('Minutes')
plt.title('EUR to USD Exchange Rate')
for item in eur_us_rates:
    plt.annotate(item, xy=(i, item))
    i += 1
plt.show()

i = 0
plt.plot(eur_gbp_rates)
plt.ylabel('Rate')
plt.xlabel('Minutes')
plt.title('EUR to GBP Exchange Rate')
for item in eur_gbp_rates:
    plt.annotate(item, xy=(i, item))
    i += 1
plt.show()
call('bash cleanup.sh')