import numpy as np
from ot import emd2

# from ot import emd2
def distance(a, b):
    a, b = max(a, b), min(a, b)
    return min(abs(a - b), abs(a - 2 * np.pi - b))
fixed_bins = np.linspace(-0.05, 2 * np.pi-0.05, 50)
C = np.array([[distance(a, b) for a in fixed_bins[:-1]] for b in fixed_bins[:-1]])
def get_phase_entropy(complex):
    real = np.real(complex)
    imag = np.imag(complex)
    mag = np.sqrt(real * real + imag * imag)
    phase = np.arccos(real / mag)
    phase[np.arcsin(imag / mag) < 0] += np.pi
    
    values, bins = np.histogram(phase, bins=fixed_bins)
    pival = np.searchsorted(bins, 3.14)
    n_ones = np.count_nonzero(real > 0)
    n_zeros = np.count_nonzero(real < 0)
    comparison_measure = np.zeros_like(values).astype(float)
    comparison_measure[0] = float(n_ones / (n_ones + n_zeros))/3
    comparison_measure[-1] = float(n_ones / (n_ones + n_zeros))/3
    comparison_measure[1] = float(n_ones / (n_ones + n_zeros))/3
    comparison_measure[pival+1] = float(n_zeros / (n_ones + n_zeros))/3
    comparison_measure[pival-1] = float(n_zeros / (n_ones + n_zeros))/3
    comparison_measure[pival] = float(n_zeros / (n_ones + n_zeros))/3
    # prob = values / values.sum()
    emd = emd2(prob, comparison_measure, C)
    entropy_p_hcomplete = -np.nansum(prob * np.log(prob))
    return entropy_p_hcomplete, emd
re1 = re.compile(r'\(([\d\.e\+-]+),\s*([\d\.e\+-]+)\)')
re2 = re.compile(r'Energy:\s*([\d\.-]+)\n(.*)')
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
palette = [
    "#ca0020",
    "#f4a582",
    "#92c5de",
    '#0571b0'
]
def read_cnf(path):
    with open(path) as cnffile:
        clauses = []
        for line in cnffile:
            line = line.strip()
            if line == '' or line[0] == 'c':
                continue
            if line[0] == 'p':
                n, m = map(int, line.strip().split()[2:])
                continue
            clauses.append(
                list(map(int, line.strip().split()[:-1]))
            )
    return n, clauses

def getunsat(clauses, assignment):
    nunsat = 0
    for c in clauses:
        sat = False
        for lit in c:
            if (lit > 0) == (assignment[abs(lit)-1] == '1'):
                sat = True
                break
        nunsat += not sat
    return nunsat
