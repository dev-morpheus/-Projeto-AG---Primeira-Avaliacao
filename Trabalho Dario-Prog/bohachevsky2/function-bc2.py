#
# Trabalho avaliativo - Algoritmo Genético 
# Função Bohachevsky 2 (BC2)
# Aluno:
#   Vitor dos Santos Correia
#

import numpy as np
import time


def bf2_objective(x):
    x = np.atleast_2d(x)
    x1, x2 = x[:, 0], x[:, 1]
    # Fórmula BF2: f(x) = x1^2 + 2x2^2 - 0.3 * cos(3*pi*x1) * cos(4*pi*x2) + 0.3
    term1 = x1**2 + 2*x2**2
    term2 = -0.3 * np.cos(3 * np.pi * x1) * np.cos(4 * np.pi * x2)
    term3 = 0.3
    return term1 + term2 + term3

def executar_ag_bf2():
    lb, ub = -50.0, 50.0
    size_pop = 100
    num_geracoes_max = 1000
    alpha = 0.8  
    nfe = 0
    
    # 1. Inicialização da População
    pop = np.random.uniform(lb, ub, (size_pop, 2))
    fitness = bf2_objective(pop)
    nfe += size_pop
    
    min_fit_anterior = float('inf')
    cont_fit_rep = 0
    
    for geracao in range(num_geracoes_max):
        min_fit_atual = np.min(fitness)
        
        if abs(min_fit_atual - min_fit_anterior) < 1e-8:
            cont_fit_rep += 1
        else:
            cont_fit_rep = 0
            
        if cont_fit_rep >= 50 or min_fit_atual < 1e-6:
            break
        min_fit_anterior = min_fit_atual

        # 2. Seleção por Torneio
        idx = np.random.randint(0, size_pop, (size_pop, 4))
        p1_idx = np.where(fitness[idx[:, 0]] < fitness[idx[:, 1]], idx[:, 0], idx[:, 1])
        p2_idx = np.where(fitness[idx[:, 2]] < fitness[idx[:, 3]], idx[:, 2], idx[:, 3])
        
        pai_sel1 = pop[p1_idx]
        pai_sel2 = pop[p2_idx]
        
        # 3. Crossover Aritmético (90%)
        filhos = np.copy(pai_sel1)
        mask_cross = np.random.rand(size_pop) < 0.9
        melhor_p1 = (fitness[p1_idx] < fitness[p2_idx]).reshape(-1, 1)
        
        filhos[mask_cross] = np.where(melhor_p1[mask_cross], 
                                      pai_sel1[mask_cross] * alpha + pai_sel2[mask_cross] * (1 - alpha),
                                      pai_sel2[mask_cross] * alpha + pai_sel1[mask_cross] * (1 - alpha))
        
        # 4. Mutação Gaussiana com redução de escala
        mask_mut = np.random.rand(size_pop) < 0.5
        escala = (ub - lb) * 0.1 * (1 - geracao/num_geracoes_max) 
        
        for i in np.where(mask_mut)[0]:
            gene_idx = np.random.randint(0, 2)
            ruido = np.random.normal(0, escala)
            filhos[i, gene_idx] += ruido
            filhos[i, gene_idx] = np.clip(filhos[i, gene_idx], lb, ub)
            
        pop = filhos
        fitness = bf2_objective(pop)
        nfe += size_pop
        
    return np.min(fitness), nfe

# --- EXECUÇÃO DAS 100 REPETIÇÕES PARA A TABELA ---
if __name__ == "__main__":
    num_repeticoes = 100
    total_nfe, sucessos = 0, 0
    start_time = time.time()

    print("Executando 100 repetições para BF2.")

    for r in range(num_repeticoes):
        res, nfe_run = executar_ag_bf2()
        total_nfe += nfe_run
        if abs(res - 0.0) < 0.01:
            sucessos += 1
            
    total_time = time.time() - start_time
    print(f"\n--- RESULTADOS FINAIS ITEM 5 (BF2) ---")
    print(f"Tempo Total: {total_time:.2f}s")
    print(f"Taxa de Sucesso (SR): {sucessos}%")
    print(f"NFE Médio: {total_nfe / num_repeticoes:.2f}")