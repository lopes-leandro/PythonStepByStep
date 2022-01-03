tupl = 1,2,3,4,5;
print(tupl);
print("O valor da tuple no índice 1 é ", tupl[1]);
print("tuple[1:3] é ", tupl[1:3]);
tupl2 = (11,12,13);
tupl3 = tupl + tupl2;
print(tupl3);
# repetição de tuples
print(tupl * 2)
# teste de associação
print(5 in tupl)
# indexação negativa
print(tupl[-1])
# função length de tuple
print(len(tupl));
# valor máximo
print(max(tupl));
# valor mínimo
print(min(tupl));
# modificação em tuple não é aceito
# tupl[1] = 5;
print(tupl == tupl2)
print(tupl > tupl2)
# trocando valores em tuples
l = ['one', 'two'];
x, y = l;
print(x, y);
x, y = y, 10;
print(x, y);