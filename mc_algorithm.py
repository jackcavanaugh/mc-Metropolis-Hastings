import numpy as np

def run_mc(r, runs, N, d0, alpha, L, bins, dAsqd, histogram):
    for ll in range(runs):
        for ii in range(N):
            r_try = np.zeros(2)
            for jj in range(2):
                r_try[jj] = r[ii, jj] + alpha*(2*np.random.rand()-1)
                if r_try[jj] < 0:
                    r_try[jj] += L
                if r_try[jj] >= L:
                    r_try[jj] -= L
            overlap = False
            for kk in range(N):
                if kk == ii:
                    continue
                dr = r_try - r[kk]
                for jj in range(2):
                    if dr[jj] > L/2:
                        dr[jj] -= L
                    elif dr[jj] < -L/2:
                        dr[jj] += L
                if np.sum(dr**2) < d0**2:
                    overlap = True
                    break
            if not overlap:
                r[ii] = r_try
            for kk in range(N):
                if kk == ii:
                    continue
                dr = r[ii] - r[kk]
                for jj in range(2):
                    if dr[jj] > L/2:
                        dr[jj] -= L
                    elif dr[jj] < -L/2:
                        dr[jj] += L
                drsqd = np.sum(dr**2)
                bin_index = int(np.floor(np.pi*(drsqd - d0**2)/dAsqd))
                if 0 <= bin_index < bins:
                    histogram[bin_index, 1] += 1
    return r, histogram
