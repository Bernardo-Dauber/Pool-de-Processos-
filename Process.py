class Process:
    def __init__(self, tipo,pid=0):
        self.pid = pid 
        self.tipo = tipo # use o tipo para verificar qual objeto pertence para qual classe 

    def execute(self):
        pass

class ComputingProcess(Process):
    def __init__(self, expressao,tipo, pid=0):
        super().__init__(tipo,pid)
        self.expressao = expressao
        self.tipo = "C"
        

    def execute(self):
        expressao_split = self.expressao.split()
        operador = expressao_split[1]
        num1 = int(expressao_split[0])
        num2 = int(expressao_split[2])

        if operador == "+":
            print(num1 + num2)
        elif operador == "-":
            print(num1 - num2)
        elif operador == "*":
            print(num1 * num2)
        elif operador == "/":
            print(num1 / num2)

class WritingProcess(Process):
    def __init__(self, expressao,tipo, pid=0):
        super().__init__(tipo, pid)
        self.expressao = expressao
        self.tipo = "W"
        

    def execute(self):
        with open('computation.txt', 'a') as file_write:
            file_write.writelines(" {}  \n".format( self.expressao))
            file_write.close()
            
         
class ReadingProcess(Process):
    def __init__(self,listaProcesso,tipo, pid=0):
        super().__init__(tipo, pid)
        self.listaProcesso = listaProcesso
        self.tipo = "R"
        


    def execute(self):
        with open('computation.txt', 'r') as file_read:
            

            for line in file_read:
           
                obj = ComputingProcess(line)
                self.listaProcesso.append(obj)
            file_read.close()
        
        print(len(self.listaProcesso))
        with open('computation.txt', 'w') as file_exit:
            file_exit.close()

        return self.listaProcesso
        
class PrintingProcess(Process):
    def __init__(self, listaProcesso, tipo, pid=0):
        super().__init__(tipo, pid)
        self.listaProcesso = listaProcesso
        self.tipo = "P"
        

    def execute(self):
        for process in self.listaProcesso:
            

            
            # Print the object's specific attributes depending on its type
            if isinstance(process, ComputingProcess):
                print(process.tipo, process.pid, process.expressao)
            elif isinstance(process, WritingProcess):
                print( process.tipo, process.pid, process.expressao)
            elif isinstance(process, ReadingProcess):
                print(process.tipo, process.pid, process.listaProcessos)
            else:
                print("Unknown process type")



class Sistema:
    def __init__(self, menu):
        self.listaProcesso = []

    def MenuMain(self):
        
        
        print()
        print("Sistema: ")
        print("1- Criar Processos ")
        print("2- Executar Próximo Processo ")
        print("3- Executar Processo Específico ")
        print("4- Salvar a Fila de Processos")
        print("5- Carregar Processo")
        print("0- Sair")
        print()
        
        choice = int(input("Escolha uma opção: "))
        

        while choice != 0:
            if choice == 1:
                self.Criar_Processo()
            elif choice == 2:
                self.Executar_Processo()
            elif choice == 3:
                self.ExecutarProcesso_específico()
            elif choice == 4:
                self.Salva_Fila()
            elif choice == 5:
                self.CarregarFile()
            elif choice == 0:
                break

            print() 
            print("Sistema: ")
            print("1- Criar Processos ")
            print("2- Executar Próximo Processo ")
            print("3- Executar Processo Específico ")
            print("4- Salvar a Fila de Processos")
            print("5- Carregar Processo")
            print("0- Sair")
            print()
            
            choice = int(input("Escolha uma opção: "))


    def Criar_Processo(self):
        
        print()
        print("Processos: ")
        print("1- ComputingProcess: ")
        print("2- WritingProcess ")
        print("3- ReadingProcess: ")
        print("4- PrintingProcess: ")
        print("5- Voltar: ")
        print()
        
        x = int(input("Escolha um Processo: "))
        pid = 1
        while True:
            
            
            
            if x == 1:
                print("1- ComputingProcess: ")
                
                expressao = input("Digite uma expressão: ")
                computing_process = ComputingProcess(expressao,"C",pid)
                self.listaProcesso.append(computing_process)
                print("Adicionado a lista de processos")
                print()
            
            elif x == 2:
                print("2- WritingProcess ")
                
                expressao = input("Digite a expressao para ser gravada:")
                write_process = WritingProcess(expressao,"W",pid)
                self.listaProcesso.append(write_process)
                print("Adicionado a lista de processos")
                print()
            elif x == 3:
                print("3- ReadingProcess: ")
                
                reading_Process = ReadingProcess(self.listaProcesso,"R" ,pid)
                self.listaProcesso.append(reading_Process)
                print("Adicionado a lista de processos")
                print()
            elif x == 4:
                print("4- PrintingProcess: ")
                
                printing_process = PrintingProcess(self.listaProcesso,"P",pid)
                self.listaProcesso.append(printing_process)
                print("Adicionado a lista de processos")
                print()
            elif x == 5:
                self.MenuMain()
            pid +=1
           
            

            print()
            print("Processos: ")
            print("1- ComputingProcess: ")
            print("2- WritingProcess ")
            print("3- ReadingProcess: ")
            print("4- PrintingProcess: ")
            print("5- Voltar: ")
            print()
        
            x = int(input("Escolha um Processo: "))
    
    def Executar_Processo(self):
        processo_executar = self.listaProcesso.pop(0) # elemento na posição 0 
        print("Processo Executado: ")
        processo_executar.execute()# executar obj na posição zero 
        return self.listaProcesso# retornar a lista sem o obj executado
    
    def ExecutarProcesso_específico(self):
        print("Selecione um pid:")

        
        pid = int(input())

        
        process_index = None
        for i, process_obj in enumerate(self.listaProcesso):
            if process_obj.pid == pid:
                process_index = i
                break

       
        if process_index:
            
            process = self.listaProcesso.pop(process_index)
            print("Processo Executado")
            process.execute()
        
        return self.listaProcesso


    def Salva_Fila(self):

        with open ("computation_2.txt",'a') as file_salva:
                
                    file_salva.write("{}\n".format(self.listaProcesso))


    def CarregarFile(self):
        with open("computation_2.txt", 'r') as file_load:
            for line in file_load:
                if isinstance(line, ComputingProcess):
                    obj_c = ComputingProcess(obj_c)
                    self.listaProcesso.append(obj_c)
                elif isinstance(line, WritingProcess):
                    obj_w = WritingProcess(obj_w)
                    self.listaProcesso.append(obj_w)
                elif isinstance(line, ReadingProcess):
                    obj_r = ReadingProcess(self.listaProcesso)
                    self.listaProcesso.append(obj_r)
                elif isinstance(line, PrintingProcess):
                    obj_p = PrintingProcess(self.listaProcesso)
                    self.listaProcesso.append(obj_p)
                


if __name__ == '__main__':
    ativar_sistema = "S"
    menu = Sistema(ativar_sistema)
    menu.MenuMain()
