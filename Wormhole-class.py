import numpy as np

class Wormhole:
    def __init__(self, rho_0):
        """
        Initialize the wormhole with a constant energy density.
        
        Parameters:
        rho_0 : float
            A constant related to the energy density.
        """
        self.rho_0 = rho_0

    def shape_function(self, r):
        """
        Define the shape function b(r) for the wormhole.
        
        Parameters:
        r : float or np.ndarray
            Radial coordinate.
        
        Returns:
        float or np.ndarray
            The value of the shape function b(r).
        """
        # Example shape function: b(r) = r_0 (constant)
        r_0 = 1.0  # Example constant
        return r_0  # Modify as needed for your specific model

    def redshift_function(self, r):
        """
        Define the redshift function e^(phi(r)).
        
        Parameters:
        r : float or np.ndarray
            Radial coordinate.
        
        Returns:
        float or np.ndarray
            The value of the redshift function e^(phi(r)).
        """
        # Example redshift function: e^(phi(r)) = e^(k * r) for some constant k
        k = 0.1  # Example constant
        return np.exp(k * r)  # it can be Modified as needed for  specific model

    def energy_density(self, r):
        """
        Calculate the energy density rho at a given radial coordinate r.
        
        Parameters:
        r : float
            Radial coordinate.
        
        Returns:
        float
            The energy density rho.
        """
        b_r = self.shape_function(r)
        b_prime = 0  # Derivative of b(r) with respect to r (modify as needed)
        
        # Calculate energy density
        rho = (b_prime - self.rho_0) / (4 * np.pi * (b_r - r))
        return rho

    def radial_pressure(self, r):
        """
        Calculate the radial pressure p_r at a given radial coordinate r.
        
        Parameters:
        r : float
            Radial coordinate.
        
        Returns:
        float
            The radial pressure p_r.
        """
        b_r = self.shape_function(r)
        b_prime = 0  # Derivative of b(r) with respect to r (modify as needed)
        
        # Calculate radial pressure
        p_r = (b_prime - self.rho_0) / (4 * np.pi * (b_r - r)) - self.energy_density(r)
        return p_r

    def tangential_pressure(self, r):
        """
        Calculate the tangential pressure p_t at a given radial coordinate r.
        
        Parameters:
        r : float
            Radial coordinate.
        
        Returns:
        float
            The tangential pressure p_t.
        """
        return self.energy_density(r)  # p_t = rho in the Morris-Thorne model

    def stress_energy_tensor(self, r):
        """
        Calculate the stress-energy tensor T_mu_nu at a given radial coordinate r.
        
        Parameters:
        r : float
            Radial coordinate.
        
        Returns:
        np.ndarray
            The stress-energy tensor T_mu_nu.
        """
        rho = self.energy_density(r)
        p_r = self.radial_pressure(r)
        p_t = self.tangential_pressure(r)
        
        # Construct the stress-energy tensor
        T_mu_nu = np.array([[rho, 0, 0, 0],
                             [0, -p_r, 0, 0],
                             [0, 0, -p_t, 0],
                             [0, 0, 0, -p_t]])
        return T_mu_nu

# Example usage
if __name__ == "__main__":
    wormhole = Wormhole(rho_0=1.0)  # Initialize with a constant energy density
    r = 2.0  # Example radial coordinate
    T = wormhole.stress_energy_tensor(r)
    print("Stress-Energy Tensor T_mu_nu at r =", r)
    print(T)
