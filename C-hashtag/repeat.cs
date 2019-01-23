using System;

namespace Testbed{
  class TestA{
      static void Main(string[] args){
      int x = 0;
      
      while (x < 10){
        Console.WriteLine("This is message: {0}", x);
        x++;
      }
    Console.ReadLine();
    }
  }
}
