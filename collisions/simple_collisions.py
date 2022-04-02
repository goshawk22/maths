import time

# Simulating the collision between both particles, assuming the coefficient of restitution is 1
# Input vec: a vector representing v_a, v_b

# Formula for restitution when e = 1: v_b + -v_a = u_a - u_b
# Formula for conservation of momentum: m_a*u_a + m_b*u_b = m_a*v_a + m_b*v_b

def col_p(vec, mass_vector):
    u_a = vec[0]
    u_b = vec[1]
    m_a = mass_vector[0]
    m_b = mass_vector[1]
    
    # Found by substituting the formula for restitution into the formula for conservation of momentum to cancel out v_b, then rearranging for v_a
    final_velocity_a = (m_a*u_a + 2*m_b*u_b - m_b*u_a)/(m_a+m_b)
    # Same as above, but cancel out v_a and rearrange for v_b
    final_velocity_b = (m_b*u_b + 2*m_a*u_a - m_a*u_b)/(m_a+m_b)

    return [final_velocity_a, final_velocity_b]

# Simulating the collision between a particle and the magical wall, again assuming the coefficient of restitution is 1. particle is either 0 (a) or 1 (b).
def col_w(vec, particle):
    if particle == 0:
        return [-vec[0], vec[1]]
    else:
        return [vec[0], -vec[1]]
    # That was easy :)

# Check if no more collisions will occur
def check_velocity(vec):
    if (vec[0] >= 0) and (vec[1] >= 0):
        if vec[0] > vec[1]:
            return True
    
    return False

def main(n, verbose=True):
    n = n # Number of significant figures of pi to calculate

    m_a = 100**(n-1) # Mass of particle a
    m_b = 1 # Mass of particle b

    mass_vector = [m_a, m_b]

    initial_velocity_a = -1
    initial_velocity_b = 0
    vec = [initial_velocity_a, initial_velocity_b]
    collisions = 0
    while True:
        # Collision between particles
        vec = col_p(vec, mass_vector)
        collisions += 1
        if check_velocity(vec):
            break

        # Collision between wall and particle
        vec = col_w(vec, 1) # Only particle b can collide with wall as it is between the wall and particle a
        collisions += 1
        if check_velocity(vec):
            break
    
    if verbose:
        print("The mass of Particle A is: " + str(m_a) + "kg")
        print("The mass of Particle B is: " + str(m_b) + "kg")

        print("The initial velocity of Particle A was " + str(initial_velocity_a) + "m/s")
        print("The initial velocity of Particle B was " + str(initial_velocity_b) + "m/s")

        print("The final velocity of Particle A was " + str(vec[0]) + "m/s")
        print("The final velocity of Particle B was " + str(vec[1]) + "m/s")

        print("The total number of collisions was " + str(collisions))
        print("This means that Pi to " + str(n) + " significant figures is " + str(collisions/(10**(n-1))))

    return collisions

main(5)

# Timing function
# Time taken increases by roughly a factor of 10 for each extra significant figure.
for n in range(1, 10):

    start = time.time()
    pi = main(n, verbose=False)
    end = time.time()
    print("Calculating pi to " + str(n) + " significant figures gave result " + str(pi/(10**(n-1))) + " and took " + str(end-start) + " seconds.")

