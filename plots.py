import numpy as np
import matplotlib.pyplot as plt
from visualize import visualize

def plot_results(r0, r, d0, L, histogram):
    plt.close('all')
    
    visualize(r0, d0, L)
    plt.title('Hard disks in initial state')
    plt.savefig('pre_sim.png')
    plt.clf()
    
    visualize(r, d0, L)
    plt.title('Hard disks after simulation')
    plt.savefig('post_sim.png')
    plt.clf()
    
    plt.figure()
    plt.plot(histogram[:,0], histogram[:,1], 'o')
    plt.title('RDF for gas state')
    plt.xlabel('r')
    plt.ylabel('g(r)')
    plt.savefig('rdf.png')
    plt.clf()
    
    plt.figure()
    plt.plot(histogram[:,0], 1 + np.pi*d0**2*histogram[:,1]/2, 'o')
    plt.title('Pressure v. r for gas state')
    plt.xlabel('r')
    plt.ylabel('PA/(N*kb*T)')
    plt.savefig('pressure.png')
    plt.close('all')
