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

def normal_distribution(N, mean=None, std=None):
    if mean is None:
        mean = (N - 1) / 2.0
    if std is None:
        std = N / 6.0
    # unnormalised Gaussian pdf at each bin center i
    weights = [math.exp(-((i - mean)**2) / (2 * std * std)) for i in range(N)]
    total = sum(weights)
    return [w/total for w in weights]

def half_doubled_distribution(N):
    #first N/2 bins 2p, remaining bins p
    cutoff = N // 2
    weights = [2.0 if i < cutoff else 1 for i in range(N)]
    #change the sign of i < cutoff to shift middle bin to 2p or p for odd N
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
    N = 365                  
    q = 21                   
    attempts = 1000000     
    distribution = half_doubled_distribution(N)

    collision_prob = run_experiment(distribution, q, attempts)
    print(f"Estimated collision probability (q={q}, N={N}) over {attempts} trials: {collision_prob:.6f}")