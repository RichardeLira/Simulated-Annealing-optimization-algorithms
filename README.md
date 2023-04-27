# Breve descrição sobre o algoritmo

O algoritmo Simulated Annealing (Cozinhamento Simulado) é um método de otimização global que busca encontrar a solução ótima de um problema em um espaço de busca grande e complexo.

O algoritmo é inspirado no processo físico de resfriamento de um material até que sua estrutura atinja um estado de mínima energia. A partir daí, o algoritmo simula o processo de aquecimento e resfriamento controlado, permitindo que o sistema escape de mínimos locais e explore regiões distantes do espaço de busca.

O Simulated Annealing usa uma função de custo que mede a qualidade de uma solução candidata e um conjunto de parâmetros que determinam a intensidade da perturbação da solução e o ritmo de resfriamento.

O algoritmo começa com uma solução inicial aleatória e, em seguida, faz uma série de perturbações, aceitando ou rejeitando as soluções candidatas de acordo com uma probabilidade que depende da temperatura atual. À medida que a temperatura diminui, a probabilidade de aceitar soluções piores diminui, permitindo que o algoritmo se aproxime de um mínimo global.

O Simulated Annealing é amplamente utilizado em áreas como engenharia, física, ciência da computação e otimização de problemas complexos. É um algoritmo poderoso para encontrar soluções aproximadas de problemas de otimização global, mesmo quando a função de custo é complexa e não diferenciável
