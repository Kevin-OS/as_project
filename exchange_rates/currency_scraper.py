from subprocess import call
from glob import glob
import matplotlib.pyplot as plt
from time import sleep

time_remaining = 5
count = 0
while count <= 5:
    call('bash feed_export_script.sh')
    print('%d minutes remaining...' % time_remaining)
    sleep(60)
    time_remaining -= 1
    count += 1

filenames = glob('*.csv')
print(filenames)

eur_us_rates = []
eur_gbp_rates = []
for file in filenames:
    with open(file) as f:
        for line in f.readlines():
            if line.startswith('US'):
                eur_us_rates.append(float(line.strip().split(',')[1]))
            elif line.startswith('Brit'):
                eur_gbp_rates.append(float(line.strip().split(',')[1]))

plt.plot(eur_us_rates)
plt.ylabel('EUR to USD')
plt.show()
plt.plot(eur_gbp_rates)
plt.ylabel('EUR to GBP')
plt.show()