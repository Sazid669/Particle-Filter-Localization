import numpy as np
import math
from MCLocalization import MCLocalization

class PFMBL(MCLocalization):
    """
    Particle Filter Map Based Localization class.

    This class defines a Map Based Localization using a Particle Filter. It inherits from :class:`MCLocalization`, so the Prediction step is already implemented.
    It needs to implement the Update function, and consecuently the Weight and Resample functions.
    """
    def __init__(self, zf_dim, M, *args) -> None:
        
        self.zf_dim = zf_dim  # dimensionality of a feature observation
        
        self.M = M
        self.nf = len(M)
        super().__init__(*args)


    def Weight(self, z, R): 
        """
        Weight each particle by the liklihood of the particle being correct.
        The probability the particle is correct is given by the probability that it is correct given the measurements (z). 

        
        :param z: measurement vector
        :param R: measurement noise covariance
        :return: None
        """
        # To be completed by the student
        return
    
    
    def Resample(self):
        """
        Resample the particles based on their weights to ensure diversity and prevent particle degeneracy.

        This function implements the resampling step of a particle filter algorithm. It uses the weights
        assigned to each particle to determine their likelihood of being selected. Particles with higher weights
        are more likely to be selected, while those with lower weights have a lower chance.

        The resampling process helps to maintain a diverse set of particles that better represents the underlying
        probability distribution of the system state. 

        After resampling, the attributes 'particles' and 'weights' of the ParticleFilter instance are updated
        to reflect the new set of particles and their corresponding weights.

        :return: None
        """
        # To be completed by the student
        return
    
    def Update(self, z, R):
        """
        Update the particle weights based on sensor measurements and perform resampling.

        This function adjusts the weights of particles based on how well they match the sensor measurements.
       
        The updated weights reflect the likelihood of each particle being the true state of the system given
        the sensor measurements.

        After updating the weights, the function may perform resampling to ensure that particles with higher
        weights are more likely to be selected, maintaining diversity and preventing particle degeneracy.
        
        :param z: measurement vector
        :param R: the covariance matrix associated with the measurement vector

        """
        # To be completed by the student
        return
    

    def Localize(self):
        uk, Qk = self.GetInput()

        if uk.size > 0:
            self.Prediction(uk, Qk)
        
        zf, Rf = self.GetMeasurements()
        if zf.size > 0:
            self.Update(zf, Rf)

        self.PlotParticles()
        return self.get_mean_particle()