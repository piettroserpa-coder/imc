// 1 - Declaração da função calcularIMC que recebe peso e altura
function calcularIMC(peso, altura) {
    // 2 - Retorna o resultado da divisão do peso pela altura ao quadrado
    return peso / (altura * altura);
}

// 3 - Declaração da função classificarIMC que recebe o IMC
function classificarIMC(imc) {
    // 4 - Verifica se o IMC é menor que 18.5
    if (imc < 18.5) {
        // 5 - Retorna objeto com classificação "Abaixo do peso"
        return {
            // 6 - Nome da classificação
            classificacao: "Abaixo do peso",
            // 7 - Categoria da classificação
            categoria: "Magreza",
            // 8 - Grau de obesidade (0 = não obeso)
            grau: 0,
            // 9 - Classe CSS para estilização
            classe: "abaixo-peso"
        };
    }
    // 10 - Senão, verifica se o IMC é menor que 25
    else if (imc < 25) {
        // 11 - Retorna objeto com classificação "Peso normal"
        return {
            classificacao: "Peso normal",
            categoria: "Saudável",
            grau: 0,
            classe: "peso-normal"
        };
    }
    // 12 - Senão, verifica se o IMC é menor que 30
    else if (imc < 30) {
        // 13 - Retorna objeto com classificação "Sobrepeso"
        return {
            classificacao: "Sobrepeso",
            categoria: "Sobrepeso",
            grau: 1,
            classe: "sobrepeso"
        };
    }
    // 14 - Senão, verifica se o IMC é menor que 35
    else if (imc < 35) {
        // 15 - Retorna objeto com classificação "Obesidade grau 1"
        return {
            classificacao: "Obesidade grau 1",
            categoria: "Obesidade",
            grau: 2,
            classe: "obesidade"
        };
    }
    // 16 - Senão, verifica se o IMC é menor que 40
    else if (imc < 40) {
        // 17 - Retorna objeto com classificação "Obesidade grau 2"
        return {
            classificacao: "Obesidade grau 2",
            categoria: "Obesidade severa",
            grau: 2,
            classe: "obesidade"
        };
    }
    // 18 - Senão (IMC maior ou igual a 40)
    else {
        // 19 - Retorna objeto com classificação "Obesidade grau 3"
        return {
            classificacao: "Obesidade grau 3",
            categoria: "Obesidade mórbida",
            grau: 3,
            classe: "obesidade"
        };
    }
}

// 20 - Declaração da função calcularPesoIdeal que recebe a altura
function calcularPesoIdeal(altura) {
    // 21 - Define o IMC mínimo ideal (18.5)
    const imcMinIdeal = 18.5;
    // 22 - Define o IMC máximo ideal (24.9)
    const imcMaxIdeal = 24.9;

    // 23 - Calcula o peso mínimo ideal
    const pesoMin = imcMinIdeal * (altura * altura);
    // 24 - Calcula o peso máximo ideal
    const pesoMax = imcMaxIdeal * (altura * altura);

    // 25 - Retorna objeto com peso mínimo e máximo (1 casa decimal)
    return {
        min: pesoMin.toFixed(1),
        max: pesoMax.toFixed(1)
    };
}

// 26 - Declaração da função getRecomendacoes que recebe IMC e classificação
function getRecomendacoes(imc, classificacao) {
    // 27 - Cria um array vazio para armazenar as recomendações
    let recomendacoes = [];

    // 28 - Verifica se o IMC é menor que 18.5
    if (imc < 18.5) {
        // 29 - Adiciona recomendações para abaixo do peso
        recomendacoes = [
            "Consulte um nutricionista para ganho de peso saudável",
            "Aumente a ingestão de alimentos nutritivos e calóricos",
            "Pratique exercícios de fortalecimento muscular"
        ];
    }
    // 30 - Senão, verifica se o IMC é menor que 25
    else if (imc < 25) {
        // 31 - Adiciona recomendações para peso normal
        recomendacoes = [
            "Mantenha uma alimentação equilibrada",
            "Continue praticando atividades físicas regularmente",
            "Faça check-ups médicos periódicos"
        ];
    }
    // 32 - Senão, verifica se o IMC é menor que 30
    else if (imc < 30) {
        // 33 - Adiciona recomendações para sobrepeso
        recomendacoes = [
            "Adote uma dieta mais equilibrada e reduza calorias",
            "Aumente a prática de exercícios aeróbicos",
            "Considere consultar um nutricionista"
        ];
    }
    // 34 - Senão (obesidade)
    else {
        // 35 - Adiciona recomendações para obesidade
        recomendacoes = [
            "Procure orientação médica especializada",
            "Inicie um programa de emagrecimento supervisionado",
            "Pratique exercícios de baixo impacto regularmente"
        ];
    }

    // 36 - Retorna o array com as recomendações
    return recomendacoes;
}

// 37 - Adiciona evento de submit ao formulário quando a página carrega
document.getElementById('imcForm').addEventListener('submit', function (e) {
    // 38 - Previne o recarregamento da página ao enviar o formulário
    e.preventDefault();

    // 39 - Remove a classe 'show' da mensagem de erro (oculta)
    document.getElementById('errorMessage').classList.remove('show');

    // 40 - Obtém o valor do campo 'nome' e remove espaços extras
    const nome = document.getElementById('nome').value.trim();
    // 41 - Obtém o valor do campo 'idade' e converte para inteiro
    const idade = parseInt(document.getElementById('idade').value);
    // 42 - Obtém o valor do campo 'peso' e converte para decimal
    const peso = parseFloat(document.getElementById('peso').value);
    // 43 - Obtém o valor do campo 'altura' e converte para decimal
    const altura = parseFloat(document.getElementById('altura').value);

    // 44 - Verifica se o campo 'nome' está vazio
    if (!nome) {
        // 45 - Define a mensagem de erro
        document.getElementById('errorMessage').textContent = '❌ Por favor, digite seu nome.';
        // 46 - Adiciona a classe 'show' para exibir a mensagem
        document.getElementById('errorMessage').classList.add('show');
        // 47 - Interrompe a execução da função
        return;
    }

    // 48 - Verifica se a idade é inválida ou fora do intervalo
    if (isNaN(idade) || idade < 2 || idade > 120) {
        // 49 - Define a mensagem de erro
        document.getElementById('errorMessage').textContent = '❌ Idade inválida! Deve estar entre 2 e 120 anos.';
        // 50 - Adiciona a classe 'show' para exibir a mensagem
        document.getElementById('errorMessage').classList.add('show');
        // 51 - Interrompe a execução
        return;
    }

    // 52 - Verifica se o peso é inválido ou fora do intervalo
    if (isNaN(peso) || peso <= 0 || peso > 500) {
        // 53 - Define a mensagem de erro
        document.getElementById('errorMessage').textContent = '❌ Peso inválido! Deve estar entre 1 e 500 kg.';
        // 54 - Adiciona a classe 'show' para exibir a mensagem
        document.getElementById('errorMessage').classList.add('show');
        // 55 - Interrompe a execução
        return;
    }

    // 56 - Verifica se a altura é inválida ou fora do intervalo
    if (isNaN(altura) || altura <= 0 || altura > 2.5) {
        // 57 - Define a mensagem de erro
        document.getElementById('errorMessage').textContent = '❌ Altura inválida! Deve estar entre 0.5 e 2.5 metros.';
        // 58 - Adiciona a classe 'show' para exibir a mensagem
        document.getElementById('errorMessage').classList.add('show');
        // 59 - Interrompe a execução
        return;
    }

    // 60 - Chama a função calcularIMC passando peso e altura
    const imc = calcularIMC(peso, altura);

    // 61 - Chama a função classificarIMC passando o IMC
    const resultado = classificarIMC(imc);

    // 62 - Chama a função calcularPesoIdeal passando a altura
    const pesoIdeal = calcularPesoIdeal(altura);

    // 63 - Preenche o campo 'Nome' com o nome em maiúsculas
    document.getElementById('resultNome').textContent = nome.toUpperCase();
    // 64 - Preenche o campo 'Idade' com a idade + " anos"
    document.getElementById('resultIdade').textContent = idade + ' anos';
    // 65 - Preenche o campo 'Peso' com peso formatado + " kg"
    document.getElementById('resultPeso').textContent = peso.toFixed(1) + ' kg';
    // 66 - Preenche o campo 'Altura' com altura formatada + " m"
    document.getElementById('resultAltura').textContent = altura.toFixed(2) + ' m';
    // 67 - Preenche o campo 'IMC' com IMC formatado + " kg/m²"
    document.getElementById('resultIMC').textContent = imc.toFixed(1) + ' kg/m²';
    // 68 - Preenche o campo 'Classificação' com a classificação
    document.getElementById('resultClassificacao').textContent = resultado.classificacao;
    // 69 - Preenche o campo 'Peso ideal' com a faixa de peso ideal
    document.getElementById('resultPesoIdeal').textContent = pesoIdeal.min + ' - ' + pesoIdeal.max + ' kg';

    // 70 - Obtém a referência do elemento 'classificacaoBox'
    const classificacaoBox = document.getElementById('classificacaoBox');
    // 71 - Define o texto como a classificação
    classificacaoBox.textContent = resultado.classificacao;
    // 72 - Define as classes do elemento (base + classe específica)
    classificacaoBox.className = 'classificacao ' + resultado.classe;

    // 73 - Chama a função getRecomendacoes para obter as recomendações
    const recomendacoes = getRecomendacoes(imc, resultado.classificacao);
    // 74 - Obtém a referência da lista de recomendações
    const recomendacoesList = document.getElementById('recomendacoesList');
    // 75 - Limpa a lista (remove itens anteriores)
    recomendacoesList.innerHTML = '';

    // 76 - Percorre o array de recomendações
    recomendacoes.forEach(rec => {
        // 77 - Cria um novo elemento <li>
        const li = document.createElement('li');
        // 78 - Define o texto do item como a recomendação atual
        li.textContent = rec;
        // 79 - Adiciona o item à lista
        recomendacoesList.appendChild(li);
    });

    // 80 - Adiciona a classe 'show' para tornar a div visível
    document.getElementById('resultados').classList.add('show');

    // 81 - Rola a página suavemente até a div de resultados
    document.getElementById('resultados').scrollIntoView({
        // 82 - Rolagem suave
        behavior: 'smooth',
        // 83 - Alinha o início do elemento no topo
        block: 'start'
    });
    // 84 - Fechamento da função do evento
});

// 85 - Declaração da função limparResultados
function limparResultados() {
    // 86 - Remove a classe 'show' para ocultar os resultados
    document.getElementById('resultados').classList.remove('show');

    // 87 - Reseta o formulário (limpa todos os campos)
    document.getElementById('imcForm').reset();

    // 88 - Remove a classe 'show' da mensagem de erro (oculta)
    document.getElementById('errorMessage').classList.remove('show');

    // 89 - Rola a página suavemente para o topo
    window.scrollTo({
        // 90 - Posição vertical: topo da página
        top: 0,
        // 91 - Rolagem suave
        behavior: 'smooth'
    });
    // 92 - Fechamento da função limparResultados
}