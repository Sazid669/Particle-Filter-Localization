import numpy as np
import matplotlib.pyplot as plt
from Localization import Localization

class ParticleFilter(Localization):
    """
    Particle Filter Localization.

    This class implements basic plotting and logging functionality for the Particle Filter,
    as well as the interface for the child classes to implement.

    A particle filter is a Monte Carlo algorithm that approximates the posterior distribution of the robot
    by a set of weighted particles.  Note that the "weight" (which is a terrible term) is simply the 
    probability of the particle being correct. Therefore, each particle is an estimate, and each estimate 
    has some probability of being correct.

    """
    def __init__(self, index, kSteps, robot, particles, *args):
        """
        Constructor of the Particle Filter class.

        :param index: Logging index structure (:class:`Index`)
        :param kSteps: Number of time steps to simulate
        :param robot: Simulation robot object (:class:`Robot`)
        :param particles: initial particles as a list of Pose objects (or at least a list of numpy arrays)
        :param args: Rest of arguments to be passed to the parent constructor
        """
        self.particles = particles
        self.particle_weights = np.ones(len(particles)) / len(particles) # evenly distributed weights
        self.n_eff = 0
        
        super().__init__(index, kSteps, robot, self.get_mean_particle(), *args)

        self.init_plotting()

    def MotionModel(self, particle, u, noise):
        """"
        Motion model of the Particle Filter to be overwritten by the child class.

        :param particle: particle state vector
        :param uk: input vector
        :param noise: sample from a noise distribution to be added to the input
        :return particle: updated particle state vector
        """
        return particle
    
    def Weight(self, z, R) -> None:
        """
        Weight each particle by the liklihood of the particle being correct.
        The probability the particle is correct is given by the probability that it is correct given the measurements (z). 

        
        :param z: measurement vector
        :param R: measurement noise covariance
        :return: None
        """
        print("Weight function not implemented")
        pass
 
    def Resample(self) -> None:
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
        print("Resample function not implemented")
        pass
    
    def Prediction(self, u, Q):
        """
        Predict the next state of the system based on a given motion model.

        This function updates the state of each particle by predicting its next state using a motion model.

        :param u: input vector
        :param Q: the covariance matrix associated with the input vector
        :return: None
        """
        print("Prediction function not implemented")
        pass

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
        print("Update function not implemented")
        pass

    def get_mean_particle(self):
        """
        Calculate the mean particle based on the current set of particles and their weights.
        :return: mean particle
        """
        # Weighted mean
        return np.average(self.particles, axis=0, weights=self.particle_weights)
    
    def get_best_particle(self):
        """
        Calculate the best particle based on the current set of particles and their weights.
        :return: best particle
        """
        # Maximum weight
        return self.particles[np.argmax(self.particle_weights)]

    '''
    Plotting
    '''
    def init_plotting(self):
        """
        Init the plotting of the particles and the mean particle.
        """
        self.x_idx = 0
        self.y_idx = 1
        self.yaw_idx = 2

        for x in self.index:
            if x.state == 'x': self.x_idx = x.simulation
            if x.state == 'y': self.y_idx = x.simulation
            if x.state == 'yaw': self.yaw_idx = x.simulation

        self.plt_particles = []
        self.plt_particles_ori = []
        for i in range(len(self.particles)):
            plt_particle, = plt.plot(self.particles[i][self.x_idx], self.particles[i][1], 'g.', markersize=2)
            # make plot on top
            plt_particle.set_zorder(10)
            self.plt_particles.append(plt_particle)

        for i in range(len(self.particles)):
            plt_particle, = plt.plot([self.particles[i][self.x_idx], self.particles[i][self.x_idx] + 0.5 * np.cos(self.particles[i][self.yaw_idx])],
                                     [self.particles[i][self.y_idx], self.particles[i][self.y_idx] + 0.5 * np.sin(self.particles[i][self.yaw_idx])], 'g',
                                     markersize=1)
            # make plot on top
            plt_particle.set_zorder(10)
            self.plt_particles_ori.append(plt_particle)
        
        # append the mean particle
        plt_mean_particle, = plt.plot(0, 0, 'b.', markersize=8)
        # make plot on top
        plt_mean_particle.set_zorder(10)
        self.plt_particles.append(plt_mean_particle)
        plt_mean_particle_ori, = plt.plot([0, 1 * np.cos(0)], [0, 1 * np.sin(0)], 'b', markersize=4)
        plt_mean_particle_ori.set_zorder(10)
        self.plt_particles_ori.append(plt_mean_particle_ori)

    
    def PlotParticles(self):
        """
        Plots all the particles and the mean particle.
        Particles are plotted as green dots, and the mean particle is plotted as a blue dot.
        Particle orientation is plotted as a green line, and the mean particle orientation is plotted as a blue line.
        Particle size is proportional to the particle weight.
        Note that the size is scaled for visualization purposes, and does not reflect the actual weight.
        """
        # update particles
        K_size = 200 # increase the size of the particles for visualization
        K_len = 40 # increase the length of the particle vector (orientation) for visualization
        for i in range(len(self.particles)):
            self.plt_particles[i].set_data(self.particles[i][self.x_idx], self.particles[i][self.y_idx])
            self.plt_particles[i].set_markersize(self.particle_weights[i] * K_size)
            self.plt_particles_ori[i].set_data([self.particles[i][self.x_idx], self.particles[i][self.x_idx] + K_len * self.particle_weights[i] * np.cos(self.particles[i][self.yaw_idx])],
                                     [self.particles[i][self.y_idx], self.particles[i][self.y_idx] + K_len * self.particle_weights[i] * np.sin(self.particles[i][self.yaw_idx])])

        # update mean particle
        mean_particle = self.get_mean_particle()
        self.plt_particles[-1].set_data(mean_particle[self.x_idx], mean_particle[self.y_idx])
        self.plt_particles_ori[-1].set_data([mean_particle[self.x_idx], mean_particle[self.x_idx] + 1 * np.cos(mean_particle[self.yaw_idx])],
                                        [mean_particle[self.y_idx], mean_particle[self.y_idx] + 1 * np.sin(mean_particle[self.yaw_idx])])
      