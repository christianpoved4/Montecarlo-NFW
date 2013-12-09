import numpy as np, pylab,sys, nfw

# Plots a halo
# Requires:
#     x,y,z: arrays with the positions for each particle
#     x_center,y_center,z_center: position of the halo center
# Returns:
#     Three files with graphics in the planes x-y, y-z and z-x of the halo

def halo(x,y,z,x_center,y_center,z_center):
    
    sys.stdout.write('\rPlotting halo... ')
    sys.stdout.flush()
    pylab.plot(x , y, 'k,')
    pylab.plot(x_center , y_center, 'r.', label="Potential Minumum")
    pylab.plot(np.average(x) , np.average(y), 'c.', label="Center of Mass")
    pylab.legend(loc=4, borderaxespad=0.5)
    pylab.xlabel('x (Mpc/H)')
    pylab.ylabel('y (Mpc/H)')
    pylab.title('Halo x-y')
    pylab.savefig('halo_xy.png',format='png',dpi=600)
    pylab.close()

    pylab.plot(y , z, 'k,')
    pylab.plot(y_center , z_center, 'r.', label="Potential Minumum")
    pylab.plot(np.average(y) , np.average(z), 'c.',label="Center of Mass")
    pylab.legend(loc=4, borderaxespad=0.5)
    pylab.xlabel('y (Mpc/H)')
    pylab.ylabel('z (Mpc/H)')
    pylab.title('Halo y-z')
    pylab.savefig('halo_yz.png',format='png',dpi=600)
    pylab.close()

    pylab.plot(z , x, 'k,')
    pylab.plot(z_center , x_center, 'r.', label="Potential Minumum")
    pylab.plot(np.average(z) , np.average(x), 'c.',label="Center of Mass")
    pylab.legend(loc=4, borderaxespad=0.5)
    pylab.xlabel('z (Mpc/H)')
    pylab.ylabel('x (Mpc/H)')
    pylab.title('Halo z-x')
    pylab.savefig('halo_zx.png',format='png',dpi=600)
    pylab.close()
    sys.stdout.write('Done\n')

# Plots the NFW mass profile 
# Requires:
#     radius: array with the radial distances
#     mass: array with the mass values
#     parameters: an array with the parameters of the NFW profile (mean density and scale radius)
# Returns:
#     A file with agraphic of the mass profile

def mass(radius, mass, parameters):
    
    pylab.plot(radius , mass,'b',label="Real Mass")
    pylab.plot(radius , nfw.mass(radius,parameters[0],parameters[1]),'r',label="NFW profile")
    pylab.legend(loc=4, borderaxespad=0.5)
    pylab.xlabel('Radius (Mpc/H)')
    pylab.ylabel('Mass (10^11 Solar Masses)')
    pylab.title('Mass')
    pylab.savefig('mass.png',format='png',dpi=600)
    pylab.close()

# Plots the NFW mass profile in logarithmic scale 
# Requires:
#     logR: array with the logarithm of the radial distances
#     logM: array with the logarithm of the mass values
#     parameters: an array with the parameters of the NFW profile (mean density and scale radius)
# Returns:
#     A file with a graphic of the mass profile in logarithmic scale
    
def logmass(logR, logM, parameters):
    
    log10R=np.log10(np.exp(logR))
    log10M=np.log10(np.exp(logM))
    pylab.plot(log10R , log10M,'.b',label="Real Mass")
    pylab.plot(log10R , np.log10(np.exp(nfw.logmass(logR,parameters[0],parameters[1]))),'r',label="NFW profile")
    pylab.legend(loc=4, borderaxespad=0.5)
    pylab.xlabel('Radius (Mpc/H)')
    pylab.ylabel('Mass (10^11 Solar Masses)')
    pylab.title('Mass (log-log)')
    pylab.savefig('log_mass.png',format='png',dpi=600)
    pylab.close()

# Plots the NFW density profile in logarithmic scale 
# Requires:
#     r_density: array with the radial distances
#     density: array with the density values
#     logR: array with the logarithm of the radial distances
#     parameters: an array with the parameters of the NFW profile (mean density and scale radius)
# Returns:
#     A file with a graphic of the density profile in logarithmic scale
    
def logdensity(r_density, density, logR, parameters):
    log10R=np.log10(np.exp(logR))
    pylab.plot(np.log10(r_density) , np.log10(density),'.b',label="Real Density")
    pylab.plot(log10R , np.log10(np.exp(nfw.logdensity(logR,parameters[0],parameters[1]))),'r',label="NFW profile")
    pylab.legend(loc=4, borderaxespad=0.5)
    pylab.xlabel('Radius (Mpc/H)')
    pylab.ylabel('Density (10^11 Solar Masses/(Mpc/H)^3)')
    pylab.title('Density (log-log)')
    pylab.savefig('log_density.png',format='png',dpi=600)
    pylab.close()

# Makes a contour plot of the likelihood 
# Requires:
#     a_walk: array with the random walk of the first parameter
#     b_walk: array with the random walk of the second parameter
#     chi2: array with the chi squared estimate for each step in the random walk
# Returns:
#     A file with a contour plot of the likelihood in function of both parameters
    
def rainbow_likelihood(a_walk,b_walk,chi2):
    
    N = 1000j
    extent = (a_walk[np.argmin(a_walk)],a_walk[np.argmax(a_walk)],b_walk[np.argmin(b_walk)],b_walk[np.argmax(b_walk)])

    my_xs,my_ys = np.mgrid[extent[0]:extent[1]:N, extent[2]:extent[3]:N]

    my_resampled = griddata(a_walk, b_walk, np.exp(chi2), my_xs, my_ys)
    pylab.imshow(my_resampled.T,extent=extent,origin='lower',interpolation='bicubic',cmap='spectral',aspect='auto')

    pylab.title('$\cal{L}$')
    pylab.xlabel('$a$')
    pylab.ylabel('$b$')
    pylab.colorbar()
    pylab.savefig('rainbow.png',format='png',dpi=600)
    pylab.close()
