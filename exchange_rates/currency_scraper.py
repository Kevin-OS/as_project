from subprocess import call
from glob import glob
import matplotlib.pyplot as plt

call('bash feed_export_script.sh')

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