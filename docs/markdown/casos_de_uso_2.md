# Modelo de caso de uso

### 1. Casos de uso por ator: 

***

 | Organizador                    | Público em Geral        |
 |:--:                            |:--:                     |
 | Cadastrar Unidade (UC1)        | Divulgação (UC6)        |
 | Cadastrar Campeonato (UC2)     | Visualizar Tabelas (UC7)|
 | Cadastrar Times (UC3)          |                         |?????????????????????????????????????????????????????????????????????????????????????????????????????
 | Gerenciar Partidas (UC4)       |                         |
 | Registrar Resultados (UC5)     |                         |
 | Gerenciar Inscrições (UC8)     |                         |

***


### 2. Descrições resumidas dos casos de uso:

* **Cadastrar Unidade (UC1):**
   - **Ator:** Organizador
   - **Descrição:** O Organizador pode cadastrar informações sobre uma nova unidade, incluindo nome e endereço. Isso é necessário para a gestão dos campeonatos.

* **Cadastrar Campeonato (UC2):**
   - **Ator:** Organizador
   - **Descrição:** O Organizador pode cadastrar um novo campeonato, fornecendo detalhes como nome, unidade, quadra, período de inscrição e datas dos jogos. Isso permite a organização de competições entre times.

* **Cadastrar Times (UC3):**
   - **Ator:** Organizador
   - **Descrição:** O Organizador pode cadastrar times para um campeonato específico, inserindo informações como nome e posição. Isso é necessário para compilar as tabelas de classificação.

* **Gerenciar Partidas (UC4):**
   - **Ator:** Organizador
   - **Descrição:** O Organizador tem a capacidade de gerenciar as partidas, incluindo a programação de datas e horários, atribuindo times a cada partida e especificando a rodada. Isso ajuda a estruturar os jogos do campeonato.

* **Registrar Resultados (UC5):**
   - **Ator:** Organizador
   - **Descrição:** O Organizador pode registrar os resultados das partidas, informando os placares de cada time. Isso permite o acompanhamento das pontuações e classificações ao longo do campeonato.

* **Divulgação (UC6):**
   - **Ator:** Público em geral
   - **Descrição:** O Público em geral tem a capacidade de visualizar informações divulgadas sobre o campeonato, como datas, horários das partidas e resultados. Isso permite que as pessoas acompanhem os eventos.

* **Visualizar Tabelas (UC7):**
   - **Ator:** Público em geral
   - **Descrição:** O Público em geral tem a capacidade de visualizar as tabelas de classificação, que mostram a posição de cada time no campeonato com base em seus resultados. Isso ajuda a entender o desempenho dos times.

* **Gerenciar Inscrições (UC8):**
   - **Ator:** Organizador
   - **Descrição:** O Organizador pode gerenciar as inscrições dos times nos campeonatos, verificando e controlando quem está registrado para participar. Isso é importante para garantir a organização adequada dos jogos.

*** 

### 3. Fluxos de caso de uso

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC1 |
| **Nome** | Cadastrar Unidade |
| **Ator** | Organizador |
| **Sumário** | Permitir que o Organizador cadastre informações sobre uma nova unidade, incluindo nome e endereço, para fins de gestão de campeonatos. |
| **Pré-condição** | O Organizador deve estar logado na plataforma. |
| **Pós-condição** | A nova unidade é cadastrada com sucesso na plataforma. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

| **Fluxo Principal** |  |
|--|--|
| Ações do Ator | Ações do Sistema |
|1. O Organizador acessa a plataforma e seleciona a opção "Cadastrar Unidade". | |
|2. O sistema apresenta um formulário para o Organizador preencher com informações sobre a nova unidade, incluindo nome e endereço. | |
|3. O Organizador preenche o formulário com os dados da unidade a ser cadastrada. | |
| |4. O sistema valida os dados e cadastra a nova unidade na plataforma. |
| |5. O sistema exibe uma mensagem de confirmação de sucesso. |

***

**Fluxo Alternativo 1:** Dados inválidos|  
|--|
| Se os dados fornecidos pelo Organizador forem inválidos ou insuficientes, o sistema exibirá uma mensagem de erro e solicitará que os dados sejam corrigidos. |  

**Fluxo Alternativo 2:** Unidade já existe|
|--|
| Se a unidade com o mesmo nome já estiver cadastrada na plataforma, o sistema informará ao Organizador e solicitará que ele forneça um nome único.|

***

|  **Fluxo de Exceção 1:** Falha na conexão | |
|--|--|
| **Ações do Ator** | **Ações do Sistema** |
|1. O Organizador tenta cadastrar uma nova unidade, mas a conexão com o servidor falha. | |
| | 2. O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 3. O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |

***

<br>
<br>

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC2 |
| **Nome** | Cadastrar Campeonato |
| **Ator** | Organizador |
| **Sumário** | Permitir que o Organizador cadastre um novo campeonato, fornecendo detalhes como nome, unidade, quadra, período de inscrição e datas dos jogos. |
| **Pré-condição** | O Organizador deve estar logado na plataforma. Deve haver unidades cadastradas na plataforma. |
| **Pós-condição** | O novo campeonato é criado com sucesso na plataforma. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

### Fluxo Principal

| Ações do Ator | Ações do Sistema |
|--|--|
| 1. O Organizador acessa a plataforma e seleciona a opção "Cadastrar Campeonato". | |
| | 2. O sistema exibe um formulário para o Organizador preencher com informações sobre o novo campeonato, incluindo nome, unidade, quadra, período de inscrição e datas dos jogos. |
| 3. O Organizador preenche o formulário com os dados do campeonato a ser cadastrado. | |
| | 4. O sistema valida os dados e cria o novo campeonato na plataforma. |
| | 5. O sistema exibe uma mensagem de confirmação de sucesso. |

### Fluxo de Exceção 1: Dados inválidos

| Ações do Ator | Ações do Sistema |
|--|--|
| 3.1 O Organizador preenche o formulário com dados inválidos ou insuficientes. | |
| | 3.2 O sistema exibe uma mensagem de erro e solicita que o Organizador corrija os dados. |

### Fluxo de Exceção 2: Unidade não encontrada

| Ações do Ator | Ações do Sistema |
|--|--|
| | 3.3 O Organizador tenta cadastrar um campeonato vinculado a uma unidade que não existe na plataforma. |
| | 3.4 O sistema informa ao Organizador que a unidade especificada não foi encontrada e solicita que ele selecione uma unidade válida. |

### Fluxo de Exceção 3: Falha na conexão

| Ações do Ator | Ações do Sistema |
|--|--|
| 1.1 O Organizador tenta cadastrar um novo campeonato, mas a conexão com o servidor falha. | |
| | 1.2 O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 1.3 O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |

***

<br>
<br>

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC3 |
| **Nome** | Cadastrar Times |
| **Ator** | Organizador |
| **Sumário** | Permitir que o Organizador cadastre times para um campeonato específico, inserindo informações como nome e posição. |
| **Pré-condição** | O Organizador deve estar logado na plataforma. Deve haver um campeonato ativo na plataforma. |
| **Pós-condição** | Os times são cadastrados com sucesso no campeonato. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

### Fluxo Principal

| Ações do Ator | Ações do Sistema |
|--|--|
| 1. O Organizador acessa a plataforma e seleciona o campeonato ao qual deseja adicionar times. | |
| | 2. O sistema exibe uma lista de times que já estão inscritos no campeonato, se houver. |
| 3. O Organizador seleciona a opção "Cadastrar Times". | |
| | 4. O sistema exibe um formulário para o Organizador preencher com informações sobre os times, incluindo nome e posição. |
| 5. O Organizador preenche o formulário com os dados dos times a serem cadastrados. | |
| | 6. O sistema valida os dados e cadastra os times no campeonato. |
| | 7. O sistema exibe uma mensagem de confirmação de sucesso. |

### Fluxo de Exceção 1: Dados inválidos

| Ações do Ator | Ações do Sistema |
|--|--|
| 5.1 O Organizador preenche o formulário com dados inválidos ou insuficientes. | |
| | 5.2 O sistema exibe uma mensagem de erro e solicita que o Organizador corrija os dados. |

### Fluxo de Exceção 2: Campeonato não encontrado

| Ações do Ator | Ações do Sistema |
|--|--|
| | 1.1 O Organizador tenta cadastrar times em um campeonato que não existe ou não está ativo na plataforma. |
| | 1.2 O sistema informa ao Organizador que o campeonato especificado não foi encontrado ou não está ativo. |

### Fluxo de Exceção 3: Falha na conexão

| Ações do Ator | Ações do Sistema |
|--|--|
| 1.2 O Organizador tenta cadastrar times em um campeonato ativo na plataforma, mas a conexão com o servidor falha. | |
| | 1.3 O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 1.4 O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |

***

<br>
<br>

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC4 |
| **Nome** | Gerenciar Partidas |
| **Ator** | Organizador |
| **Sumário** | Permitir que o Organizador gerencie as partidas, incluindo a programação de datas e horários, atribuindo times a cada partida e especificando a rodada. |
| **Pré-condição** | O Organizador deve estar logado na plataforma. Deve haver um campeonato ativo com partidas a serem gerenciadas. |
| **Pós-condição** | As alterações nas partidas são registradas com sucesso na plataforma. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

### Fluxo Principal

| Ações do Ator | Ações do Sistema |
|--|--|
| 1. O Organizador acessa a plataforma e seleciona o campeonato que contém as partidas a serem gerenciadas. | |
| 2. O sistema exibe uma lista das partidas do campeonato, incluindo informações como datas, horários e times participantes. | |
| 3. O Organizador seleciona uma partida da lista para gerenciar. | |
| 4. O Organizador pode realizar as seguintes ações na partida selecionada: | |
| | 5. O sistema permite que o Organizador programe datas e horários para a partida, atribua times a cada partida e especifique a rodada. |
| | 6. O sistema valida as alterações e as registra na plataforma. |
| | 7. O sistema exibe uma mensagem de confirmação de sucesso. |

### Fluxo de Exceção 1: Partida não encontrada

| Ações do Ator | Ações do Sistema |
|--|--|
| 3.1 O Organizador tenta gerenciar uma partida que não existe ou não está listada no campeonato selecionado. | |
| | 3.2 O sistema informa ao Organizador que a partida especificada não foi encontrada no campeonato selecionado. |

### Fluxo de Exceção 2: Dados inválidos

| Ações do Ator | Ações do Sistema |
|--|--|
| 4.1 O Organizador tenta realizar ações na partida com dados inválidos ou insuficientes. | |
| | 4.2 O sistema exibe uma mensagem de erro e solicita que o Organizador corrija os dados. |

### Fluxo de Exceção 3: Falha na conexão

| Ações do Ator | Ações do Sistema |
|--|--|
| 1.2 O Organizador tenta acessar a plataforma e selecionar um campeonato, mas a conexão com o servidor falha. | |
| | 1.3 O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 1.4 O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |

***

<br>
<br>

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC5 |
| **Nome** | Registrar Resultados |
| **Ator** | Organizador |
| **Sumário** | Permitir que o Organizador registre os resultados das partidas, informando os placares de cada time. |
| **Pré-condição** | O Organizador deve estar logado na plataforma. Deve haver partidas com resultados a serem registrados. |
| **Pós-condição** | Os resultados das partidas são registrados com sucesso na plataforma. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

### Fluxo Principal

| Ações do Ator | Ações do Sistema |
|--|--|
| 1. O Organizador acessa a plataforma e seleciona o campeonato que contém as partidas com resultados a serem registrados. | |
| 2. O sistema exibe uma lista das partidas do campeonato, incluindo informações como datas, times participantes e status das partidas. | |
| 3. O Organizador seleciona uma partida da lista para registrar os resultados. | |
| 4. O Organizador informa os placares de cada time na partida selecionada. | |
| | 5. O sistema valida os resultados e os registra na plataforma. |
| | 6. O sistema exibe uma mensagem de confirmação de sucesso. |

### Fluxo de Exceção 1: Partida não encontrada

| Ações do Ator | Ações do Sistema |
|--|--|
| 3.1 O Organizador tenta registrar resultados para uma partida que não existe ou não está listada no campeonato selecionado. | |
| | 3.2 O sistema informa ao Organizador que a partida especificada não foi encontrada no campeonato selecionado. |

### Fluxo de Exceção 2: Dados inválidos

| Ações do Ator | Ações do Sistema |
|--|--|
| 4.1 O Organizador tenta registrar resultados com dados inválidos, como placares em formato incorreto. | |
| | 4.2 O sistema exibe uma mensagem de erro e solicita que o Organizador corrija os dados dos resultados. |

### Fluxo de Exceção 3: Falha na conexão

| Ações do Ator | Ações do Sistema |
|--|--|
| 1.2 O Organizador tenta acessar a plataforma e selecionar um campeonato, mas a conexão com o servidor falha. | |
| | 1.3 O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 1.4 O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |

***

<br>
<br>

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC6 |
| **Nome** | Divulgação |
| **Ator** | Público em geral |
| **Sumário** | Permitir que o Público em geral visualize informações divulgadas sobre o campeonato, como datas, horários das partidas e resultados. |
| **Pré-condição** | Deve haver informações de divulgação disponíveis na plataforma. |
| **Pós-condição** | O Público em geral visualiza as informações de divulgação sobre o campeonato. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

### Fluxo Principal

| Ações do Ator | Ações do Sistema |
|--|--|
| 1. O Público em geral acessa a plataforma e navega para a seção de "Divulgação" ou "Informações do Campeonato". | |
| 2. O sistema exibe informações divulgadas sobre o campeonato, como datas, horários das partidas, resultados de partidas anteriores e notícias relacionadas. | |

### Fluxo de Exceção 1: Nenhuma informação disponível

| Ações do Ator | Ações do Sistema |
|--|--|
| | 2.1 Não há informações de divulgação disponíveis no momento. |
| 2.2 O Público em geral visualiza uma mensagem informando que não há informações disponíveis para divulgação. | |

### Fluxo de Exceção 2: Falha na conexão

| Ações do Ator | Ações do Sistema |
|--|--|
| 1.1 O Público em geral tenta acessar a plataforma para visualizar informações de divulgação, mas a conexão com o servidor falha. | |
| | 1.2 O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 1.3 O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |

***

<br>
<br>

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC7 |
| **Nome** | Visualizar Tabelas |
| **Ator** | Público em geral |
| **Sumário** | Permitir que o Público em geral visualize as tabelas de classificação, que mostram a posição de cada time no campeonato com base em seus resultados. |
| **Pré-condição** | Deve haver tabelas de classificação disponíveis na plataforma. |
| **Pós-condição** | O Público em geral visualiza as tabelas de classificação do campeonato. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

### Fluxo Principal

| Ações do Ator | Ações do Sistema |
|--|--|
| 1. O Público em geral acessa a plataforma e navega para a seção de "Tabelas" ou "Classificação". | |
| 2. O sistema exibe as tabelas de classificação do campeonato, mostrando a posição de cada time com base em seus resultados, como pontos, vitórias, derrotas e saldo de gols. | |

### Fluxo de Exceção 1: Tabelas de classificação não disponíveis

| Ações do Ator | Ações do Sistema |
|--|--|
| | 2.1 Não há tabelas de classificação disponíveis no momento. |
| 2.2 O Público em geral visualiza uma mensagem informando que as tabelas de classificação não estão disponíveis no momento. | |

### Fluxo de Exceção 2: Falha na conexão

| Ações do Ator | Ações do Sistema |
|--|--|
| 1.1 O Público em geral tenta acessar a plataforma para visualizar as tabelas de classificação, mas a conexão com o servidor falha. | |
| | 1.2 O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 1.3 O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |

***

<br>
<br>

| **Especificação de caso de uso** | |
|--|--|
| **Identificador** | UC8 |
| **Nome** | Gerenciar Inscrições |
| **Ator** | Organizador |
| **Sumário** | Permitir que o Organizador gerencie as inscrições dos times nos campeonatos, verificando e controlando quem está registrado para participar. |
| **Pré-condição** | O Organizador deve estar logado na plataforma. Deve haver campeonatos com times inscritos na plataforma. |
| **Pós-condição** | As alterações nas inscrições dos times são registradas com sucesso na plataforma. |
| **Pontos de Inclusão** |  |
| **Pontos de Extensão** |  |

***

### Fluxo Principal

| Ações do Ator | Ações do Sistema |
|--|--|
| 1. O Organizador acessa a plataforma e seleciona o campeonato que deseja gerenciar em relação às inscrições dos times. | |
| 2. O sistema exibe a lista de times inscritos no campeonato, incluindo informações como nome, foto, habilidades e dados de contato. | |
| 3. O Organizador pode realizar as seguintes ações nas inscrições dos times: | |
| | 4. O sistema permite que o Organizador confirme a inscrição de um time clicando em um botão de confirmação ao lado do nome do time. |
| | 5. O sistema permite que o Organizador rejeite a inscrição de um time clicando em um botão de rejeição ao lado do nome do time. |
| | 6. O sistema permite que o Organizador adicione um novo time à lista de inscritos clicando em um botão de adição e fornecendo as informações do time. |
| | 7. O sistema permite que o Organizador remova um time da lista de inscritos clicando em um botão de remoção ao lado do nome do time. |
| | 8. O sistema registra as alterações nas inscrições dos times na plataforma. |
| | 9. O sistema notifica os times sobre a confirmação ou rejeição de suas inscrições. |

### Fluxo de Exceção 1: Times não encontrados

| Ações do Ator | Ações do Sistema |
|--|--|
| 2.1 O Organizador tenta gerenciar as inscrições de times em um campeonato que não tem times inscritos ou não está listado na plataforma. | |
| | 2.2 O sistema informa ao Organizador que não há times inscritos no campeonato especificado ou que o campeonato não está disponível. |

### Fluxo de Exceção 2: Falha na conexão

| Ações do Ator | Ações do Sistema |
|--|--|
| 1.2 O Organizador tenta acessar a plataforma e selecionar um campeonato, mas a conexão com o servidor falha. | |
| | 1.3 O sistema exibe uma mensagem de erro informando que a operação não pode ser concluída devido a problemas de conexão. |
| | 1.4 O sistema oferece a opção de tentar novamente ou entrar em contato com o suporte. |
