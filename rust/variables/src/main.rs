fn main() {
    //Shadowing
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
    const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
    println!("The number of seconds in 3 hourse is always: {THREE_HOURS_IN_SECONDS}");

    let x1 = 5;

    let x1 = x1 + 1;

    {
        let x1 = x1 * 2;
        println!("The value of x1 in the inner scope is {x1}")
    }

    println!("The value of x1 is {x1}");

    let tup: (i32, f64, u8) = (500, 6.4, 1);

    let (_x, y, _z) = tup;
    println!("The value of y is: {y}");

    x = tup.0;
    println!("The value of x is: {x}");

    let a = [1, 2, 3, 4, 5];
    let b: [i32; 5] = [1, 2, 3, 4, 5];

    let first_a = a[0];
    println!("The first element in a is: {first_a}");

    let second_b = b[1];
    println!("The second element in b is: {second_b}");
}
