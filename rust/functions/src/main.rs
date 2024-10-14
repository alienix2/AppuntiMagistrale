fn main() {
    println!("Hello, world!");

    another_function(5);
    print_labeled_measuremenet(5, 'a');

    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is: {y}");

    let x = five();
    println!("Using the function five() I get: {x}");
}

fn another_function(x: i32) {
    println!("Another function, value of x is {x}");
}

fn print_labeled_measuremenet(value: i32, unit_label: char) {
    println!("The measurement is: {value} {unit_label}");
}

fn five() -> i32 {
    5
}
