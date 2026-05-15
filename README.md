# Relatório De atividade de Instalação.

**1.** Primeiro instalamos a VM no aplicativo Oracle VirtualBox e colocamos ela para rodar.
   
   <img width="954" height="738" alt="Captura de tela 2026-04-24 100715" src="https://github.com/user-attachments/assets/0d5a0b6e-b4db-41fc-9242-ea67dbf14e3c" />

**2.** Então realizamos a instalação da máquina virtual, que no meio da instalção tinha para: Definir o usuário do omputador, senha, como queriamos o sistema (CLI ou GUI) entre outras configurações e depois de instalado ele ficava assim.
   
   <img width="957" height="794" alt="Captura de tela 2026-04-24 094319" src="https://github.com/user-attachments/assets/2a3a9c58-7aeb-419c-a8b0-50c471b040ab" />

**3.** Foi identificado no escopo da atividade, que precisavamos fazer a instalação  FileZilla Client no sistema host (Windows 64-bit x86).
Esta ferramenta gerenciará o serviço FTP previsto na atividade.

<img width="1180" height="585" alt="image" src="https://github.com/user-attachments/assets/3dde71e4-1251-40ce-95d3-8ba53f0c0369" />

**4.** Então começamos a fazer a programação do site.
- Página Inicial (/): Abre o arquivo visual (index.html).
- Validação de Login (/login): Recebe um nome e uma senha.
- Se for "Alef" e a senha "1234", ele libera o acesso.
  Caso contrário, ele nega.
- Ele roda na porta 8000 do seu computador.
- <img width="682" height="496" alt="image" src="https://github.com/user-attachments/assets/2fb0ca99-1ac8-472c-94c3-7abbc5dea5ee" />


**5.** Este dqui é a parte visual da página, onde ele criou:
- O botão de início
- Botão de entrar
- Confere se as informações adicionadas pelo cliente está correta.
<img width="840" height="449" alt="image" src="https://github.com/user-attachments/assets/796fabd4-1dcd-4a64-9112-298c0667f455" />


**6.** Aqui é a parte de interface gráfica onde vemos as cores das coisas entre outras coisas.


<img width="736" height="930" alt="image" src="https://github.com/user-attachments/assets/7942cea4-ba06-4a5a-973e-3c5e0d1eae5c" />

**7.** Nesse print fizemos uma conexão entra o Windows para a VM, para conseguirmos mandar o site para eles "conversarem", então quando mandamos o PI e a posrta do hospedeiro ele consegue identificar o site.

<img width="909" height="630" alt="Captura de tela 2026-04-24 085040" src="https://github.com/user-attachments/assets/0899c096-c050-48f8-8349-059fb68a552d" />

**8.** Então conectamos a máquina virtual UBUNTO com a Windows, através do comando: ssh -p 2222 user@127.0.0.1  (-p indica aporta)


<img width="822" height="555" alt="Captura de tela 2026-04-24 090052" src="https://github.com/user-attachments/assets/ed9eafae-4149-4cab-81c1-225850f5d2de" />


**9.** Após conectarmos a pasta apareceu lá na máquina virtual.


<img width="1221" height="723" alt="image" src="https://github.com/user-attachments/assets/065c34cb-f587-4d74-b586-63f82b976912" />

**10.**
Então conectamos a máquina com outra.
Teste de Conexão e Acesso à Rede
Nesta fase, o objetivo foi tirar o site do "computador interno" e deixá-lo disponível para outras pessoas da mesma rede.

Localizando o Caminho (IP): Foi usado o comando ipconfig para descobrir o "RG" do computador (IP: 10.10.147.164). Esse é o endereço que os outros dispositivos usam para encontrar o servidor.

Site no Ar: Ao digitar o endereço no navegador, o sistema funcionou perfeitamente. O visual (estilo Hello Kitty) carregou sem erros, provando que a ponte entre a Máquina Virtual e o computador real está configurada corretamente.

Teste de Segurança: Foi testado o envio de dados no formulário. Ao digitar o nome e a senha, o sistema recebe as informações e responde se o acesso está permitido ou bloqueado, confirmando que o "cérebro" do programa está funcionando.

<img width="1202" height="581" alt="image" src="https://github.com/user-attachments/assets/556825b6-3245-440a-86aa-cbceada01e54" />

<img width="1240" height="504" alt="image" src="https://github.com/user-attachments/assets/3ba6ee45-ba8d-497e-8898-32c82fd907eb" />


<img width="1240" height="504" alt="image" src="https://github.com/user-attachments/assets/362d3d2a-7a59-4227-8629-99f0227197ac" />

<img width="1240" height="504" alt="image" src="https://github.com/user-attachments/assets/7539be0d-dd42-41a8-a703-b65a1f0bcfd0" />

<img width="1237" height="788" alt="image" src="https://github.com/user-attachments/assets/696de005-9c56-4be7-9fcf-544e234ec21c" />


<img width="1237" height="788" alt="image" src="https://github.com/user-attachments/assets/c7aebd40-b242-4433-8de2-0218beb8155b" />


<img width="1240" height="760" alt="image" src="https://github.com/user-attachments/assets/61e13486-1d59-4e2e-85f6-89ff1c7e0cd6" />


<img width="1238" height="722" alt="image" src="https://github.com/user-attachments/assets/79fa50ee-fd79-4d0d-89e7-406fce2533a5" />

<img width="1240" height="682" alt="image" src="https://github.com/user-attachments/assets/8600c878-5e91-422f-8165-5a76c6559140" />



