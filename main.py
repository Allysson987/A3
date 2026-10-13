import json
import os
class Analysing:
    def __init__(self):
        self.users={}
        self.metrics={}
        self.max_tentativas=3
    def save_data(self):
        with open('users.json', 'w') as f:
            json.dump(self.users, f)
        with open('metrics.json', 'w') as f:
            json.dump(self.metrics, f)
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def load_data(self):
        try:
            with open('users.json', 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = {}
        try:
            with open('metrics.json', 'r') as f:
                self.metrics = json.load(f)
        except FileNotFoundError:
            self.metrics = {}
    def validate_name(self,name):
        if not name:
            return False
        if any(char.isdigit() for char in name):
            return False
        if len(name) < 2 or len(name) > 50:
            return False
        return True
    def validate_age(self,age):
        if age < 0 or age > 120:
            return False
        return True
    def calculated_alfabetization_rate(self):
        self.clear_screen()
        print("Calculando taxa de alfabetização")
        if not self.users:
            return 0
        literate_count = sum(1 for info in self.users.values() if info["alfabetizado"].upper() == "S")
        return (literate_count / len(self.users)) * 100
    def validate_literate(self,literate):
        if literate.upper() not in ['S', 'N']:
            return False
        return True
    def validate_income(self,income):
            if income < 0:
                return False
            return True
    def validate_residents(self,residents):
        if residents < 0:
            return False
        return True
    def medium_residents(self):
        if not self.users:
            return 0
        total_residents = sum(info["moradores"] for info in self.users.values())
        return total_residents / len(self.users)
    def median_age_literate(self):
        if not self.users:
            return 0, []
        ages=[]
        names=[]
        for name, info in self.users.items():
            if info["alfabetizado"].upper() == "S":
                ages.append(info["idade"])
                names.append(name)
        if not ages:
            return 0, []
        if len(ages) == 1:
            return ages[0], names
        ages.sort(key=int)
        if len(ages) % 2 == 0:
            mid_index = len(ages) // 2
            median_age = (ages[mid_index - 1] + ages[mid_index]) / 2
        else:
            median_age = ages[len(ages) // 2]
        return median_age, names
    def calcular_media_renda_per_capita(self):
        if not self.users:
            return 0

        rendas = []

        for info in self.users.values():
            renda = self.renda_per_capita(
                info["renda"],
                info["moradores"]
            )
            rendas.append(renda)

        return sum(rendas) / len(rendas)
    def list_users(self):
        self.clear_screen()
        print("Listando usuários cadastrados")
        if not self.users:
            print("Nenhum usuário cadastrado.")
            return
        print("Lista de usuários cadastrados:")
        for name, info in self.users.items():
            print(f"name: {name}, Idade: {info['idade']}, Alfabetizado: {info['alfabetizado']}, Renda: {info['renda']}, Número de moradores: {info['moradores']}")
    
    def cadastre_users(self):
        self.clear_screen()
        print("Cadastrando Usuario")
        for i in range(self.max_tentativas):
            try:
                name=str(input("name: "))
                if self.validate_name(name):
                    break
            except ValueError:
                print("Entrada inválida para o nome.")
        for i in range(self.max_tentativas):
            try:
                age=int(input("Idade: "))
                if self.validate_age(age):
                    break
            except ValueError:
                print("Entrada inválida para a idade.")
        for i in range(self.max_tentativas):
            try:
                literate=str(input("Alfabetizado (S/N): "))
                if self.validate_literate(literate):
                    break
            except ValueError:
                print("Entrada inválida para o status de alfabetização.")
                
        for i in range(self.max_tentativas):
            try:
                income=float(input("Renda: "))
                if self.validate_income(income):
                    break
            except ValueError:
                print("Entrada inválida para a renda.")
        for i in range(self.max_tentativas):
            try:
                residents=int(input("Número de moradores: "))
                if self.validate_residents(residents):
                    break
            except ValueError:
                print("Entrada inválida para o número de moradores.")

        if not self.validate_name(name):
            print("name inválido!")
            return
        
        if not self.validate_age(age):
            print("Idade inválida!")
            return
        
        if not self.validate_literate(literate):
            print("Opção inválida!")
            return
        if not self.validate_income(income):
            print("Renda inválida!")
            return
        if not self.validate_residents(residents):
            print("Número de moradores inválido!")
            return
        self.users[name] = {'idade': age, 'alfabetizado': literate.upper(), 'renda': income, 'moradores': residents}
        print("Usuário cadastrado com sucesso!")
        self.save_data()
    def calculate_average_age(self):
        self.clear_screen()
        print("Calculando média de idade")
        if not self.users:
            return 0
        total_age = sum(info["idade"] for info in self.users.values())
        return total_age / len(self.users)
    def renda_per_capita(self, income, residents):
        if residents <= 0:
            return 0
        return income / residents
    def generate_metrics(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gerando métricas")
        matriz = []
        if not self.users:
            print("Nenhum usuário cadastrado.")
            return matriz
        for name, info in self.users.items():
            line = [
                name,
                info["idade"],
                info["alfabetizado"],
                info["renda"],
                info["moradores"]
            ]
            matriz.append(line)
        age_min = min(info["idade"] for info in self.users.values())
        age_max = max(info["idade"] for info in self.users.values())
        recipients_min= min(info["renda"] for info in self.users.values())
        recipients_max= max(info["renda"] for info in self.users.values())
        average_residents = sum(info["moradores"] for info in self.users.values()) / len(self.users) if self.users else 0
        total_users = len(self.users)
        ages_sum= sum(info["idade"] for info in self.users.values())
        moradores_sum= sum(info["moradores"] for info in self.users.values())
        alfabetizados_count = sum(1 for info in self.users.values() if info["alfabetizado"].upper() == "S")
        no_alfabetizados_count = sum(1 for info in self.users.values() if info["alfabetizado"].upper() == "N")
        percentage_alfabetizados = (alfabetizados_count / total_users) * 100 if total_users > 0 else 0
        percentage_no_alfabetizados = (no_alfabetizados_count / total_users)
        print(f"Total de usuários: {total_users}")
        print(f"Soma das idades: {ages_sum}")
        print(f"Soma dos moradores: {moradores_sum}")
        print(f"Idade mínima: {age_min} - do usuário: {[name for name, info in self.users.items() if info['idade'] == age_min][0]}")
        print(f"Idade máxima: {age_max} - do usuário: {[name for name, info in self.users.items() if info['idade'] == age_max][0]}")
        print(f"Renda mínima: {recipients_min} - do usuário: {[name for name, info in self.users.items() if info['renda'] == recipients_min][0]}")
        print(f"Renda máxima: {recipients_max} - do usuário: {[name for name, info in self.users.items() if info['renda'] == recipients_max][0]}")
        print(f"Média de moradores: {average_residents}")
        print(f"Quantidade de alfabetizados: {alfabetizados_count} - Percentual: {percentage_alfabetizados:.2f}%")
        print(f"Quantidade de não alfabetizados: {no_alfabetizados_count} - Percentual: {percentage_no_alfabetizados:.2f}%")
        print("Matriz de métricas:")
        
        return matriz
    
    def menu(self):
        try:
            tentativas_restantes = self.max_tentativas
            while True:
                
                try:
                    
                    print("#"*50)
                    
                    print("-- SELECIONE UMA OPÇÃO --")
                    print("-- SELECIONE 1 PARA CADASTRAR UM USUÁRIO --")
                    print("-- SELECIONE 2 PARA LISTAR OS USUÁRIOS CADASTRADOS --")
                    print("-- SELECIONE 3 PARA GERAR MÉTRICAS --")
                    print("-- SELECIONE 4 PARA CALCULAR A MÉDIA DE IDADE --")
                    print("-- SELECIONE 5 PARA CALCULAR A MEDIANA DE IDADE DOS ALFABETIZADOS --")
                    print("-- SELECIONE 6 PARA CALCULAR A TAXA DE ALFABETIZAÇÃO --")
                    print("-- SELECIONE 7 PARA CALCULAR A MÉDIA DE MORADORES --")
                    print("-- SELECIONE 8 PARA SAIR DO PROGRAMA --")

                    # print("-- SELECIONE 5 PARA SAIR DO PROGRAMA --")
                    option=int(input(''))
                    tentativas_restantes = self.max_tentativas  # Reset tentativas_restantes on successful input
                except ValueError:
                    tentativas_restantes -= 1
                    print("Opção inválida. Por favor, insira um número inteiro.")
                    print(f"Tentativas restantes: {tentativas_restantes}")
                    if tentativas_restantes <= 0:
                        print("Número máximo de tentativas atingido. Encerrando o programa.")
                        break
                    continue
                if option == 1:
                    self.cadastre_users()
                elif option == 2:
                    self.list_users()
                elif option == 3:
                    metrics = self.generate_metrics()
                    for line in metrics:
                        print(line)
                elif option == 4:
                    average_age = self.calculate_average_age()
                    print(f"A média de idade é: {average_age}")
                elif option == 5:
                    print("Calculando renda per capita")
                    median_age_alfabetized, names_alfabetized = self.median_age_literate()
                    print(f"A mediana de idade dos alfabetizados é: {median_age_alfabetized}")
                    print(f"Os alfabetizados são: {', '.join(names_alfabetized)}")
                elif option == 6:
                    alfabetization_rate = self.calculated_alfabetization_rate()
                    print(f"A taxa de alfabetização é: {alfabetization_rate}%")
                elif option == 7:
                    average_residents = self.medium_residents()
                    print(f"A média de moradores é: {average_residents}")
                elif option == 8:
                    print("Encerrando o programa.")
                    break
                    

        except Exception as e:
            print('Erro na seleção', e)
app=Analysing()
app.load_data()
app.menu()