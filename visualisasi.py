import matplotlib.pyplot as plt
import numpy as np

# Data dosis dan warna
doses = [0, 20, 40, 50, 70]
colors = ['rgb(75,75,150)', 'rgb(100,100,170)', 
          'rgb(125,125,190)', 'rgb(150,150,210)', 
          'rgb(175,175,230)']

# Buat visualisasi
plt.figure(figsize=(10, 6))

# Plot kotak warna untuk setiap dosis
for i, (dose, color) in enumerate(zip(doses, colors)):
    rgb = eval(color.replace('rgb',''))
    rgb = (rgb[0]/255, rgb[1]/255, rgb[2]/255)
    
    plt.fill_between([i,i+0.8], [0,0], [1,1], color=rgb)
    plt.text(i+0.4, -0.1, f'{dose} kGy', ha='center')

plt.ylim(-0.2, 1.2)
plt.xlim(-0.2, len(doses))
plt.title('Visualisasi Warna Sampel pada Berbagai Dosis Radiasi')
plt.axis('off')

# Simpan gambar dengan dpi=600
plt.savefig('warna_sampel.png', dpi=600, bbox_inches='tight')

# Tampilkan gambar
plt.show()
