class CPFValidator:

    def __init__(self, cpf):
        self.cpf = cpf 

    def cpf_validator(self):
        while len(self.cpf) != 11:
            self.cpf = str(input("CPF invalido digite novamente"))
        self.cpf = list(self.cpf)

        for i in range(0, len(self.cpf)):
            try:
                self.cpf[i] = int(self.cpf[i])
            except ValueError:
                print("CPF invalido apenas numeros!")
    
    def first_digit(self):
        self.numbers_cpf = []
        i = len(self.cpf)
        for j in range(0, 9):
            i -= 1
            self.numbers_cpf.append(self.cpf[j] * i)
        self.numbers_cpf = sum(self.numbers_cpf)
        self.numbers_cpf = (self.numbers_cpf * 10) % 11
        if self.numbers_cpf == 10:
            self.numbers_cpf = 0

    def second_digit(self):
        self.r = []
        m = len(self.cpf) + 1
        for n in range(0, 10):
            m -= 1
            self.r.append(self.cpf[n] * m)
        self.r = sum(self.r)
        self.r = (self.r * 10) % 11
        if self.r == 10:
            self.r = 0

    def final(self):
        if self.numbers_cpf == self.cpf[9] and self.r == self.cpf[10]:
            return True
        return False

cpf = str(input("Digite um CPF:\n")).replace(".", "").replace("-", "")
cpf = CPFValidator(cpf)
print(cpf.cpf_validator())
print(cpf.first_digit())
print(cpf.second_digit())
print(cpf.final())
