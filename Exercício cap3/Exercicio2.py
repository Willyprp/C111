# Criando os Conjuntos
loja1 = {'iPhone 13','Samsung Galaxy S21','Google Pixel 6','OnePlus 9 Pro','Xiaomi Mi 11','Huawei P40 Pro'}
loja2 = {'Realme GT', 'Asus ROG Phone 5', 'Vivo X60 Pro', 'Nokia 5.4', 'iPhone 13','Samsung Galaxy S21'}

# Modelos totais
print('Modelos disponíveis em alguma dessas lojas: ')
print(loja1|loja2)

# Modelos iguais
print('Modelos disponíveis em ambas lojas: ')
print(loja1&loja2)