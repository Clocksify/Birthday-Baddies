import math
import random
import statistics

def zipfian_distribution(N): 
    #generate Zipfian distribution for N bins:
    #bin i has weight proportional to 2^(-i), then normalized to sum to 1
    weights = [2 ** (-i) for i in range(N)]
    total = sum(weights)
    return [w/total for w in weights]

def uniform_distribution(N):
    return [1.0/N] * N

def half_doubled_distribution(N):
    #first N/2 bins 2p, remaining bins p
    cutoff = N // 2
    weights = [2.0 if i <= cutoff else 1 for i in range(N)]
    #for odd N, change the sign of i < cutoff to <= shift middle bin to 2p, otherwise keep as < for middle bin as p
    #for even N, change to <= to include N/2 + 1 bin
    #change weight of bin to get 2p/3p/4p etc
    total = sum(weights)
    return [w/total for w in weights]

def half_doubled_distribution_specific(N, heavy_bins):
    #First `heavy_bins` bins get weight=2, the rest get weight=1.
    #starts from index 0 so first 4 bins is 0, 1, 2, 3
    #if heavy_bins is None, then use N // 2 as default (for odd number bins, this will not incdue the middle bin)

    if heavy_bins is None:
        heavy_bins = N // 2
    
    weights = [
        2.0   if i < heavy_bins else 
        1.0 
        for i in range(N)
    ]
    total = sum(weights)
    return [w/total for w in weights]


def run_one_trial(distribution, q):
    """
    throw q balls (with replacement) based on `distribution`.
    return True if at least one collision occurred.
    """
    picks = random.choices(range(len(distribution)), weights=distribution, k=q)
    return len(set(picks)) < q

def run_experiment(distribution, q, attempts):
    """
    run `attempts` independent q-ball trials and
    return fraction that resulted in a collision.
    """
    collisions = sum(run_one_trial(distribution, q) for _ in range(attempts))
    return collisions / attempts

if __name__ == "__main__":
    N = 8   
    #count of number of bins, not maximum index   
    #setting N = 8 means bins are 0, 1, 2, 3, 4, 5, 6, 7 
    q = 2            
    attempts = 1000000     
    distribution = half_doubled_distribution_specific(N, heavy_bins=5)

    collision_prob = run_experiment(distribution, q, attempts)
    print(f"Estimated collision probability (q={q}, N={N}) over {attempts} trials: {collision_prob:.6f}")