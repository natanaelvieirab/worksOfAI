clear all;
close all;
clc;

M = load("ex1data1.txt");

X = M(:,1);
Y = M(:,2);

VetorEpocas = [];

Alpha = 0.001;
OmegaZero = randn;
Omega = randn;

for Epoca = 1:1000

  I = randperm(97);%RADOMIZANDO OS DADOS
  N = length(I); %TAMANHO DA AMOSTRA
  %Para cada amostra vamos radomizar o conjunto dos dados
  Xrand = X(I,:);
  Yrand = Y(I,:);

  vet = [];

  for i = 1:N
    YEsp = (Omega*Xrand(i) + OmegaZero); %YBARRA(Y esperado)
    Erro = (Yrand(i) - YEsp);   %ERRO = Y(O que ja temos) - YBARRA(Esperado)
    OmegaZero = OmegaZero + Alpha * Erro; %Atualiza o valor de OmegaZero
    Omega = Omega + Alpha * Erro.*Xrand(i); %Atualiza o valor de Omega

    m = length(Yrand);%???
    sqrErrors = (Yrand(i) - YEsp).^2;
    vet(i) = sqrErrors;
  endfor;    
  
  
  Custo = 0;

  Custo = 1/(2*m) * sum(vet);

  VetorEpocas = [VetorEpocas;Epoca Custo];

endfor;
   
disp(OmegaZero);
disp(Omega);


r1 = VetorEpocas(:,1);
r2 = VetorEpocas(:,2);

plot(r1,r2,'b'); 