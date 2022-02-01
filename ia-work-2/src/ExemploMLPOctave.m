clear all
close all
clc


# gera��o dos dados
load('ex3data1.mat')

K(5000,1) = zeros;

for i = 1: 5000
  for j = 1:10 
    b =  T(i,j);
    if (b <= 0)

    else
        
       K(i,1) = j;
       
    endif
  endfor
endfor

NewX = [X K];
%Utilizar a estratégia de gradiente descedente

X = NewX(:,1:400);
Y = NewX(:,401);
Y = Y';

 #Par�metros
Dn=X';

[LinD ColD]=size(X');

I=randperm(ColD);
Dn=Dn(:,I);
alvos=Y(:,I);   % Embaralha saidas desejadas tambem p/ manter correspondencia com vetor de entrada

# Define tamanho dos conjuntos de treinamento/teste (hold out)
ptrn=0.8;    % Porcentagem usada para treino
pval=0.1     % Porcentagem usada para validação
ptst=1-ptrn-pval; % Porcentagem usada para teste

J=floor(ptrn*ColD);

% Vetores para treinamento e saidas desejadas correspondentes
P = Dn(:,1:J); 
T1 = alvos(:,1:J); 
[lP cP]=size(P);   % Tamanho da matriz de vetores de treinamento

S = 4500;
% Vetores para validação e saidas desejadas correspondentes
R = Dn(:,J+1:S); 
T3 = alvos(:,J+1:S); 
[lR cR]=size(R);   % Tamanho da matriz de vetores de validaçao

% Vetores para teste e saidas desejadas correspondentes
Q = Dn(:,S+1:end); 
T2 = alvos(:,S+1:end); 
[lQ cQ]=size(Q);   % Tamanho da matriz de vetores de teste


% DEFINE ARQUITETURA DA REDE
%===========================
Ne = 1000; % No. de epocas de treinamento
Nh = 10;   % No. de neuronios na camada oculta
No = 2;   % No. de neuronios na camada de saida

alfa=0.001;   % Passo de aprendizagem

% Inicia matrizes de pesos
WW=0.1*rand(Nh,lP+1);   % Pesos entrada -> camada oculta

MM=0.1*rand(No,Nh+1);   % Pesos camada oculta -> camada de saida"ENTROU TREINAMENTO"

%%% ETAPA DE TREINAMENTO
for t=1:Ne,
    
    Epoca=t,
    
    I=randperm(cP); P=P(:,I); T1=T1(:,I);   % Embaralha vetores de treinamento e saidas desejadas
    
    EQ=0;
    for tt=1:cP,   % Inicia LOOP de epocas de treinamento
        % CAMADA OCULTA
        X=[-1; P(:,tt)];      % Constroi vetor de entrada com adicao da entrada x0=-1
        Ui = WW * X;          % Ativacao (net) dos neuronios da camada oculta
        Yi = 1./(1+exp(-Ui)); % Saida entre [0,1] (funcao logistica)

        % CAMADA DE SAIDA 
        Y=[-1; Yi];           % Constroi vetor de entrada DESTA CAMADA com adicao da entrada y0=-1
        Uk = MM * Y;          % Ativacao (net) dos neuronios da camada de saida
        Ok = 1./(1+exp(-Uk)); % Saida entre [0,1] (funcao logistica)

        % CALCULO DO ERRO 
        Ek = T1(:,tt) - Ok;           % erro entre a saida desejada e a saida da rede
        
        %%% CALCULO DOS GRADIENTES LOCAIS
        Dk = Ok.*(1 - Ok);  % derivada da sigmoide logistica (camada de saida)
        DDk = Ek.*Dk;       % gradiente local (camada de saida)
        
        Di = Yi.*(1 - Yi); % derivada da sigmoide logistica (camada oculta)
        DDi = Di.*(MM(:,2:end)'*DDk);    % gradiente local (camada oculta)

        % AJUSTE DOS PESOS - CAMADA DE SAIDA
        MM = MM + alfa*DDk*Y';
        
        % AJUSTE DOS PESOS - CAMADA OCULTA
        WW = WW + alfa*DDi*X';
    end   % Fim de uma epoca
    
    %%% ETAPA DE VALIDAÇÃO
    OUT4=[];
    for tt=1:cR,
      X=[-1; R(:,tt)];      % Constroi vetor de entrada com adicao da entrada x0=-1
      Ui = WW * X;          % Ativacao (net) dos neuronios da camada oculta
      Yi = 1./(1+exp(-Ui)); % Saida entre [0,1] (funcao logistica)
      
      % CAMADA DE SAIDA 
      Y=[-1; Yi];           % Constroi vetor de entrada DESTA CAMADA com adicao da entrada y0=-1
      Uk = MM * Y;          % Ativacao (net) dos neuronios da camada de saida
      Ok = 1./(1+exp(-Uk)); % Saida entre [0,1] (funcao logistica)
      OUT4=[OUT4 Ok];       % Armazena saida da rede
    end
    % CALCULA TAXA DE ACERTO
    count_OKVal=0;  % Contador de acertos
    for t=1:cR,
        [T3max iT3max] = max(T3(:,t));  % Indice da saida desejada de maior valor
        [OUT4_max iOUT4_max]=max(OUT4(:,t)); % Indice do neuronio cuja saida eh a maior
        if iT3max==iOUT4_max,   % Conta acerto se os dois indices coincidem 
            count_OKVal=count_OKVal+1;
        end
    end
    
    Tx_OK_Validacao=100*(count_OKVal/cR)
    
    
    % MEDIA DO ERRO QUADRATICO P/ EPOCA
    
end   % Fim do loop de treinamento


%% ETAPA DE TESTE  %%%
EQ2=0;
HID2=[];
OUT2=[];
for tt=1:cQ,
    % CAMADA OCULTA
    X=[-1; Q(:,tt)];      % Constroi vetor de entrada com adicao da entrada x0=-1
    Ui = WW * X;          % Ativacao (net) dos neuronios da camada oculta
    Yi = 1./(1+exp(-Ui)); % Saida entre [0,1] (funcao logistica)
    
    % CAMADA DE SAIDA 
    Y=[-1; Yi];           % Constroi vetor de entrada DESTA CAMADA com adicao da entrada y0=-1
    Uk = MM * Y;          % Ativacao (net) dos neuronios da camada de saida
    Ok = 1./(1+exp(-Uk)); % Saida entre [0,1] (funcao logistica)
    OUT2=[OUT2 Ok];       % Armazena saida da rede
    
    
end

% CALCULA TAXA DE ACERTO
count_OK=0;  % Contador de acertos
for t=1:cQ,
    [T2max iT2max]=max(T2(:,t));  % Indice da saida desejada de maior valor
    [OUT2_max iOUT2_max]=max(OUT2(:,t)); % Indice do neuronio cuja saida eh a maior
    if iT2max==iOUT2_max,   % Conta acerto se os dois indices coincidem 
        count_OK=count_OK+1;
    end
end

% Taxa de acerto global
Tx_OK=100*(count_OK/cQ)




% Gera a figura da superf�cie de decis�o
xc = 0:0.01:1;
yc = 0:0.01:1;

OUT3 = [];
IdxX = [];
IdxY = [];
for i = 1:length(xc)
    for j = 1:length(yc)
        X=[-1; xc(i) ;yc(j)];      % Constroi vetor de entrada com adicao da entrada x0=-1
        Ui = WW * X;          % Ativacao (net) dos neuronios da camada oculta
        Yi = 1./(1+exp(-Ui)); % Saida entre [0,1] (funcao logistica)
        
        % CAMADA DE SAIDA 
        Y=[-1; Yi];           % Constroi vetor de entrada DESTA CAMADA com adicao da entrada y0=-1
        Uk = MM * Y;          % Ativacao (net) dos neuronios da camada de saida
        Ok = 1./(1+exp(-Uk)); % Saida entre [0,1] (funcao logistica)
        OUT3=[OUT3 Ok];       % Armazena saida da rede
        
        [OUT3_max iOUT3_max]=max(Ok); % Indice do neuronio cuja saida eh a maior

        Result(i,j) = iOUT3_max;
        ResultIdxX(i,j) = xc(i);
        ResultIdxY(i,j) = yc(j);
        IdxX = [IdxX xc(i)];
        IdxY = [IdxY yc(j)];
    end
end
hold on
mesh(ResultIdxX,ResultIdxY,Result)
plot3(x(1:500,1),x(1:500,2),2*ones(500,1),'x')
hold on
plot3(x(501:1000,1),x(501:1000,2),2*ones(500,1),'rx')