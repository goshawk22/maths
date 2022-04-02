
fn col_p(u_a: f64, u_b: f64, m_a_integer: i128, m_b_integer: i128) -> (f64, f64) {

    let m_a = m_a_integer as f64;
    let m_b = m_b_integer as f64;

    // Found by substituting the formula for restitution into the formula for conservation of momentum to cancel out v_b, then rearranging for v_a
    let final_velocity_a = (m_a*u_a + 2.0*m_b*u_b - m_b*u_a)/(m_a+m_b);
    // Same as above, but cancel out v_a and rearrange for v_b
    let final_velocity_b = (m_b*u_b + 2.0*m_a*u_a - m_a*u_b)/(m_a+m_b);

    return (final_velocity_a, final_velocity_b)
}

fn col_w(v_a: f64, v_b: f64, particle: bool) -> (f64, f64) {
    if particle {
        return (-v_a, v_b);
    } else {
        return (v_a, -v_a);
    }
}

fn check_velocity(v_a: f64, v_b: f64) -> bool {
    if v_a >= 0.0 && v_b >= 0.0 && v_a >= v_b {
        return true;
    } else {
        return false;
    }
}

fn main() {
    let n = 10_u32;
    let m_a: i128 = 100_i128.pow(n - 1);
    let m_b = 1_i128;

    let initial_velocity_a = -1_f64;
    let initial_velocity_b = 0_f64;

    let mut collisions: u128 = 0;
    
    println!("The initial velocity of particle A is {} m/s", initial_velocity_a);
    println!("The initial velocity of particle B is {} m/s", initial_velocity_b);
    println!("The initial mass of particle A is {} kg", m_a);
    println!("The initial mass of particle B is {} kg", m_b);

    let mut v_a = initial_velocity_a;
    let mut v_b = initial_velocity_b;

    loop {
        (v_a, v_b) = col_p(v_a, v_b, m_a, m_b);
        collisions += 1;
        if check_velocity(v_a, v_b) {
            break;
        }

        (v_a, v_b) = col_w(v_a, v_b, true);
        collisions += 1;
        if check_velocity(v_a, v_b) {
            break;
        }
    }

    let pi: f64 = (collisions as f64)/(10_u64.pow(n - 1)) as f64;
    println!("The final velocity of particle A is {} m/s", v_a);
    println!("The final velocity of particle B is {} m/s", v_b);
    println!("There were {}", collisions);
    println!("Pi to {} significant figures is {}", n, pi);
}
