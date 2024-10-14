fn main() {
    let mut number = 3;

    if number < 5 {
        println!("Condition verified!");
    } else {
        println!("Condition not verified!");
    }

    if number != 0 {
        println!("Number is not 0")
    }

    if number % 4 == 0 {
        println!("Number is divisible by 4");
    } else if number % 2 == 0 {
        println!("Number is divisible by 2");
    } else {
        println!("Number not divisible by 2 or 4");
    }

    let new_number = if number % 2 == 0 { 0 } else { 1 };
    println!("The new number derived from the other is: {new_number}");

    //    loop {
    //        println!("Loop forever! press CTRL+C to stop");
    //    }

    let mut counter = 0;
    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        };
    };
    println!("The result is {result}");

    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");

    while number != 0 {
        println!("number = {number}");
        number -= 1;
    }

    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is {element}");
    }
}
