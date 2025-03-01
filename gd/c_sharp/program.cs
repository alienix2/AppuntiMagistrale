internal class Program
{
  static void SayHello(string name){
    Console.WriteLine("Hello " + name);
  }

  static void SayHello(string name, int age){
    Console.WriteLine("Hello " + name + " you are " + age + " years old");
  }

  static void SayHello(string name, double age){
      Console.WriteLine("Hello " + name + " you are " + age + " years old precisely");
  }

  private static void Main(string[] args){  
    Console.WriteLine("Hello game dev!");
    // int userName = Convert.ToInt32(Console.ReadLine());
    // Console.WriteLine("Hello " + userName);
    string[] names = {"John", "Doe", "Jane"};
    // for (int i = 0; i < names.Length; i++){
    //   Console.WriteLine("Hello " + names[i]);
    // }
    foreach (string name in names){
      Console.WriteLine("Hello " + name);
    }
    SayHello("Method hello");
    SayHello("Method hello", 25.3); // Method overloading and dynamic method lookup
  }
}
