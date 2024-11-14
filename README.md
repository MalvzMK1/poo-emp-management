# POO - Gerenciamento de Funcionários

Uma CLI de gerenciamento de funcionários, departamentos, funções e tarefas.

## Instalar Dependências

O arquivo `requirements.txt` possui as informações das dependências do projeto. Execute o seguinte comando no terminal para instalar as dependências:

```sh
pip install -r ./requirements.txt
```

## Iniciando a CLI

Existem dois jeitos de inicializar a CLI, uma delas é usando a CLI do python padrão:

```sh
python ./run_migration.py; python ./main.py
# ou
python3 ./run_migration.py; python3 ./main.py
```

A outra forma é rodando o arquivo `run.sh` na raíz do projeto. Com ele, duas configurações adicionais vem na hora de rodar o programa, além de fazer a busca automática no arquivo onde está a venv (por diferenças da Venv do Windows e do Linux).

- `--no-cache`: Isso vai apagar todas as pastas `__pycache__` dentro de `app`.
- `--migrate`: Isso vai rodar o script de migração para criar o banco e popular a base.

Para utilizar o arquivo `run.sh`, basta rodar os seguintes comandos em um terminal bash:

```sh
chmod +x ./run.sh # dê permissão para o arquivo
./run.sh --migrate --no-cache # execute com as flags (as flags são opcionais)
```

## Entidades

1. Departamento (Department)
2. Função (Role)
3. Tarefa (Task)
4. Funcionário (Employee)

## Módulos

No sistema, existem 4 módulos, no qual cada um é responsável por permitir a interação com cada entidade no sistema

1. Módulo de funcionário
2. Módulo de departamento
3. Módulo de tarefas
4. Módulo de funções

## Utilização

- Para utilizar o sistema, siga os números correspondentes aos módulos / funcionalidades.
- Para listar os módulos disponíveis, digite `lm` quando for solicitado para escolher um módulo.
- Para sair do sistema, digite `exit` quando for solicitado para escolher um módulo.

## Funcionalidades

### Funcionário

1.  Criar
2.  Listar todos
3.  Atualizar dados base (nome e documento)
4.  Atualizar departamento do funcionário
5.  Atualizar departamento que o funcionário gerencia
6.  Atualizar função do funcionário
7.  Listar tarefas do funcionário
8.  Deletar funcionário

### Departamento

1.  Listar todos
2.  Criar
3.  Deletar
4.  Atualizar
5.  Listar Funcionários
6.  Mostrar o Gerente

### Tarefa

1.  Listar todas
2.  Criar
3.  Deletar
4.  Atualizar o nome
5.  Mudar o responsável da tarefa
6.  Alterar status de conclusão da tarefa (funciona como um toggle)

### Função

1.  Listar todas
2.  Criar
3.  Deletar
4.  Atualizar
5.  Listar funcionários

---

_Total: 25 funcionalidades_
