from Localization import Localization
from ParticleFilter import ParticleFilter
import matplotlib.pyplot as plt
import numpy as np
class MCLocalization(ParticleFilter):
    """
    Monte Carlo Localization class.

    This class is used as "Dead Reckoning" localization using a Particle Filter.
    It implements the Prediction method from :class:`ParticleFilter` and the 
    Localize and LocalizationLoop methods from :class:`Localization`.
    """

    def __init__(self, index, kSteps, robot, particles, *args):
        """
        Constructor.
        :param index: Named tuple used to map the state vector, the simulation vector and the observation vector (:class:`prpy.IndexStruct`)
        :param kSteps: simulation time steps
        :param robot: Simulated Robot object
        :param particles: initial particles as a list of Pose objects (or at least a list of numpy arrays)
        :param args: arguments to be passed to the parent constructor
        """

        super().__init__(index, kSteps, robot, particles, *args)
        self.robot.visualizationInterval = 20

    def Prediction(self, u, Q):
        """
        Prediction overriden from :class:`ParticleFilter`.
        Note: Use the MotionModel method from :class:`ParticleFilter` to update the particles to keep it generic. Then,
        child classes can overwrite the MotionModel method to implement their own motion model.
        """
        # **To be completed by the student**.

    def Localize(self):
        """
        Single Localization iteration. Given the previous robot pose, the function reads the inout and computes the current pose.

        :returns: **xk** current robot pose (we can assume the mean of the particles or the most likely particle)

        """
        uk, Qk = self.GetInput()  # Get the input from the robot
        if uk.size > 0:
            self.Prediction(uk, Qk)

        self.PlotParticles()
        return self.get_mean_particle()
    
    def LocalizationLoop(self, x0, usk):
        """
        Given an initial robot pose :math:`x_0` and the input to the :class:`SimulatedRobot` this method calls iteratively :meth:`DRLocalization.Localize` for k steps, solving the robot localization problem.

        :param x0: initial robot pose
        :param usk: input vector for the simulation

        """
        xsk_1 = self.robot.xsk_1

        for self.k in range(self.kSteps):
            xsk = self.robot.fs(xsk_1, usk)  # Simulate the robot motion

            self.xk = self.Localize()  # Localize the robot

            xsk_1 = xsk  # current state becomes previous state for next iteration

            self.PlotTrajectory()  # plot the estimated trajectory

        plt.show()
        return

    













