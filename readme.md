# Java Interview Questions and Answers

[![Image](https://www.springboottutorial.com/images/Course-Java-Interview-Guide-200-Interview-Questions-and-Answers.png "Java Interview Guide : 200+ Interview Questions and Answers")](https://www.udemy.com/course/java-interview-questions-and-answers/)

## Expectations

- Good Java Knowledge

## Complete Course Link

- https://www.udemy.com/course/java-interview-questions-and-answers/?couponCode=NOVEMBER-2019

## Things You Need to Know

### Github Repository

https://github.com/in28minutes/JavaInterviewQuestionsAndAnswers

### PDF Guide

Available in the resources for the course

### Installing Eclipse, Java and Maven

- PDF : https://github.com/in28minutes/SpringIn28Minutes/blob/master/InstallationGuide-JavaEclipseAndMaven_v2.pdf
- Video : https://www.youtube.com/playlist?list=PLBBog2r6uMCSmMVTW_QmDLyASBvovyAO3
- GIT Repository : https://github.com/in28minutes/getting-started-in-5-steps

## Interview Questions

### Java Platform

- 1 . Why is Java so popular?
    - Java is popular for several reasons:

    1. **Platform Independence**: Java programs can run on any device that has the Java Virtual Machine (JVM), making it
       highly portable.
    2. **Object-Oriented**: Java's object-oriented nature allows for modular programs and reusable code.
    3. **Robust and Secure**: Java has strong memory management, exception handling, and security features.
    4. **Rich API**: Java provides a vast standard library that simplifies many programming tasks.
    5. **Community Support**: Java has a large and active community, providing extensive resources and support.
    6. **Performance**: Java's performance has improved significantly with Just-In-Time (JIT) compilers and other
       optimizations.
    7. **Enterprise Use**: Java is widely used in enterprise environments, particularly for server-side applications.
- 2 . What is platform independence?
  Platform independence refers to the ability of a programming language or software to run on various types of computer
  systems without modification. In the context of Java, platform independence is achieved through the use of the Java
  Virtual Machine (JVM). Java programs are compiled into bytecode, which can be executed on any device that has a JVM,
  regardless of the underlying hardware and operating system. This allows Java applications to be written once and run
  anywhere.
- 3 . What is bytecode?
  Bytecode is an intermediate representation of a Java program. When a Java program is compiled, it is converted into
  bytecode, which is a set of instructions that can be executed by the Java Virtual Machine (JVM). Bytecode is
  platform-independent, meaning it can run on any device that has a JVM, regardless of the underlying hardware and
  operating system. This allows Java programs to be written once and run anywhere.
- 4 . Compare JDK vs JVM vs JRE
    - **JDK (Java Development Kit)**: A software development kit used to develop Java applications. It includes the JRE,
      an interpreter/loader (Java), a compiler (javac), an archiver (jar), a documentation generator (Javadoc), and
      other tools needed for Java development.
    - **JVM (Java Virtual Machine)**: An abstract machine that enables your computer to run a Java program. When you run
      a Java program, the JVM is responsible for converting the bytecode into machine-specific code. It provides
      platform independence.
    - **JRE (Java Runtime Environment)**: A package of software that provides the class libraries, JVM, and other
      components to run applications written in Java. It does not include development tools like compilers or debuggers.
- 5 . What are the important differences between C++ and Java?
    - **Memory Management**: C++ uses manual memory management with pointers, while Java uses automatic garbage
      collection.
    - **Platform Independence**: Java is platform-independent due to the JVM, whereas C++ is platform-dependent and
      needs to be compiled for each platform.
    - **Multiple Inheritance**: C++ supports multiple inheritance, while Java does not. Java uses interfaces to achieve
      similar functionality.
    - **Pointers**: C++ supports pointers, allowing direct memory access. Java does not support pointers explicitly,
      enhancing security and simplicity.
    - **Standard Library**: Java has a rich standard library with built-in support for networking, threading, and GUI
      development. C++ has a standard library but with less built-in support for these features.
    - **Compilation and Execution**: C++ is compiled directly to machine code, while Java is compiled to bytecode and
      executed by the JVM.
    - **Operator Overloading**: C++ supports operator overloading, while Java does not.
    - **Templates vs. Generics**: C++ uses templates for generic programming, while Java uses generics.

### Wrapper Classes

- 7 . What are Wrapper classes?
  Wrapper classes in Java are classes that encapsulate a primitive data type into an object. They provide a way to use
  primitive data types (like `int`, `char`, etc.) as objects. Each primitive type has a corresponding wrapper class:

    - `byte` -> `Byte`
    - `short` -> `Short`
    - `int` -> `Integer`
    - `long` -> `Long`
    - `float` -> `Float`
    - `double` -> `Double`
    - `char` -> `Character`
    - `boolean` -> `Boolean`

  Wrapper classes are useful because they allow primitives to be used in contexts that require objects, such as in
  collections like `ArrayList`, and they provide utility methods for converting between types and performing operations
  on the values.
- 8 . Why do we need Wrapper classes in Java?
  Wrapper classes in Java are needed for the following reasons:
    1. **Object-Oriented Programming**: Wrapper classes allow primitive data types to be treated as objects, enabling
       them to be used in object-oriented programming contexts.
    2. **Collections**: Collections in Java, such as `ArrayList`, can only store objects. Wrapper classes allow
       primitive types to be stored in collections.
    3. **Utility Methods**: Wrapper classes provide utility methods for converting between types and performing
       operations on the values.
    4. **Default Values**: Wrapper classes can be used to represent default values (e.g., `null` for an `Integer`),
       which is not possible with primitive types.
    5. **Type Safety**: Wrapper classes enable type safety in generic programming, ensuring that only the correct type
       of objects are used.
- 9 . What are the different ways of creating Wrapper class instances?
  There are two main ways to create instances of Wrapper classes in Java:
    1. **Using Constructors**:
       Each wrapper class has a constructor that takes a primitive type or a String as an argument.
       ```java
       Integer intObj1 = new Integer(10);
       Integer intObj2 = new Integer("10");
       ```
    2. **Using Static Factory Methods**:
       The wrapper classes provide static factory methods like `valueOf` to create instances.
       ```java
       Integer intObj1 = Integer.valueOf(10);
       Integer intObj2 = Integer.valueOf("10");
       ```
- 10 . What are differences in the two ways of creating Wrapper classes?
  The two ways of creating Wrapper class instances in Java are using constructors and using static factory methods. Here
  are the differences:

    1. **Using Constructors**:
        - Each wrapper class has a constructor that takes a primitive type or a `String` as an argument.
        - Example:
          ```java
          Integer intObj1 = new Integer(10);
          Integer intObj2 = new Integer("10");
          ```
    2. **Using Static Factory Methods**:
        - Wrapper classes provide static factory methods like `valueOf` to create instances.
        - Example:
          ```java
          Integer intObj1 = Integer.valueOf(10);
          Integer intObj2 = Integer.valueOf("10");
          ```
  **Differences**:
    - **Performance**: Static factory methods are generally preferred over constructors because they can cache
      frequently requested values, improving performance.
        - **Readability**: Using `valueOf` is often more readable and expressive.
        - **Deprecation**: Some constructors in wrapper classes are deprecated in favor of static factory methods.
- 11 . What is auto boxing?
  Autoboxing in Java is the automatic conversion that the Java compiler makes between the primitive types and their
  corresponding object wrapper classes. For example, converting an `int` to an `Integer`, a `double` to a `Double`, and
  so on. This feature was introduced in Java 5 to simplify the process of working with primitive types in contexts that
  require objects, such as collections.

  Example:
    ```java
    int primitiveInt = 5;
    Integer wrappedInt = primitiveInt; // Autoboxing
    ```

  In this example, the primitive `int` is automatically converted to an `Integer` object.
- 12 . What are the advantages of auto boxing?
  Autoboxing in Java provides several advantages:
    1. **Simplicity**: Autoboxing simplifies the process of working with primitive types in contexts that require
       objects,
       such as collections.
    2. **Readability**: Autoboxing makes the code more readable and expressive by automatically converting between
       primitive types and their corresponding object wrapper classes.
    3. **Convenience**: Autoboxing eliminates the need for manual conversion between primitive types and objects,
       reducing
       boilerplate code.
    4. **Compatibility**: Autoboxing allows code written with primitive types to be used in contexts that require
       objects,
       without the need for explicit conversion.
- 13 . What is casting?
  Casting in Java is the process of converting a value of one data type to another. There are two types of casting:
    1. **Implicit Casting**: When a smaller data type is converted to a larger data type, Java automatically performs
       the
       conversion. For example, converting an `int` to a `double`.
    2. **Explicit Casting**: When a larger data type is converted to a smaller data type, or when converting between
       incompatible types, explicit casting is required. For example, converting a `double` to an `int`.

  Example:
  ```java
  int intValue = 10;
  double doubleValue = intValue; // Implicit casting
  double doubleValue = 10.5;
  int intValue = (int) doubleValue; // Explicit casting
  ```
- 14 . What is implicit casting?
  Implicit casting in Java is the automatic conversion of a smaller data type to a larger data type. Java performs
  implicit casting when the target data type can accommodate the source data type without loss of precision. For
  example, converting an `int` to a `double` or a `float` to a `double`.

  Example:
  ```java
  int intValue = 10;
  double doubleValue = intValue; // Implicit casting
  ```
- 15 . What is explicit casting?
  Explicit casting in Java is the manual conversion of a larger data type to a smaller data type, or when converting
  between incompatible types. Java requires explicit casting when the target data type may lose precision or range
  when accommodating the source data type. For example, converting a `double` to an `int`.

  Example:
  ```java
  double doubleValue = 10.5;
  int intValue = (int) doubleValue; // Explicit casting
  ```

### Strings

-
    16. Are all String’s immutable?
        No, not all `String` objects are immutable. In Java, `String` objects are immutable, meaning once a `String`
        object is created, its value cannot be changed. However, there are other classes like `StringBuilder`
        and `StringBuffer` that provide mutable alternatives to `String`. These classes allow you to modify the contents
        of the string without creating new objects.
- 17 . Where are String values stored in memory?
  In Java, `String` values are stored in a special memory area called the **String Pool**. The String Pool is part of
  the Java heap memory and is used to store unique `String` literals. When a `String` literal is created, the JVM checks
  the String Pool to see if an identical `String` already exists. If it does, the reference to the existing `String` is
  returned. If not, the new `String` is added to the pool. This process helps in saving memory and improving performance
  by reusing immutable `String` objects.
- 18 . Why should you be careful about String concatenation(+) operator in loops?
  String concatenation using the `+` operator in loops can be inefficient due to the immutability of `String` objects.
  Each time a `String` is concatenated using the `+` operator, a new `String` object is created, resulting in
  unnecessary memory allocation and garbage collection. This can lead to performance issues, especially in loops where
  multiple concatenations are performed. To improve performance, it is recommended to use `StringBuilder`
  or `StringBuffer`
  for string concatenation in loops, as these classes provide mutable alternatives to `String` and are more efficient
  for
  building strings.
- 19 . How do you solve above problem?
  To solve the problem of inefficient string concatenation using the `+` operator in loops, you should
  use `StringBuilder` or `StringBuffer`. These classes provide mutable alternatives to `String` and are more efficient
  for building strings.
  Here is an example of how to use `StringBuilder` for string concatenation in a loop:

  Example using `StringBuilder`:
  ```java
  StringBuilder sb = new StringBuilder();
  for (int i = 0; i < 10; i++) {
      sb.append(i);
  }
  String result = sb.toString();
  ```

- 20 . What are the differences between `String` and `StringBuffer`?
    - **Mutability**: `String` objects are immutable, meaning their values cannot be changed once
      created. `StringBuffer` objects are mutable, allowing their values to be modified.
    - **Thread Safety**: `StringBuffer` is synchronized, making it thread-safe. `String` is not synchronized.
    - **Performance**: Due to immutability, `String` operations can be slower as they create new objects. `StringBuffer`
      is faster for concatenation and modification operations.
    - **Usage**: Use `String` when the value does not change. Use `StringBuffer` when the value changes frequently and
      thread safety is required.
- 22 . Can you give examples of different utility methods in String class?
  The `String` class in Java provides various utility methods. Here are some examples:

  ```java
  // Example of length() method
  String str = "Hello, World!";
  int length = str.length(); // Returns 13

  // Example of charAt() method
  char ch = str.charAt(0); // Returns 'H'

  // Example of substring() method
  String substr = str.substring(7, 12); // Returns "World"

  // Example of contains() method
  boolean contains = str.contains("World"); // Returns true

  // Example of equals() method
  boolean isEqual = str.equals("Hello, World!"); // Returns true

  // Example of toUpperCase() method
  String upperStr = str.toUpperCase(); // Returns "HELLO, WORLD!"

  // Example of trim() method
  String trimmedStr = "  Hello, World!  ".trim(); // Returns "Hello, World!"

  // Example of replace() method
  String replacedStr = str.replace("World", "Java"); // Returns "Hello, Java!"

  // Example of split() method
  String[] parts = str.split(", "); // Returns ["Hello", "World!"]
  ```

### Object oriented programming basics

- 23 . What is a class?
  A class in Java is a blueprint for creating objects. It defines a set of properties (fields) and methods that the
  created objects will have. A class encapsulates data for the object and methods to manipulate that data. It serves as
  a template from which individual objects are instantiated.
- 25 . What is state of an object?
  The state of an object in Java refers to the data or values stored in its fields (instance variables) at any given
  time. The state represents the current condition of the object, which can change over time as the values of its fields
  are modified through methods or operations.
- 26 . What is behavior of an object?
  The behavior of an object in Java refers to the actions or operations that the object can perform. These behaviors are
  defined by the methods in the object's class. The methods manipulate the object's state and can interact with other
  objects. The behavior of an object is what it can do, such as calculating a value, modifying its state, or interacting
  with other objects.
- 28 . Explain about toString method ?
  The `toString` method in Java is a method that returns a string representation of an object. It is defined in
  the `Object` class, which is the superclass of all Java classes. By default, the `toString` method returns a string
  that consists of the class name followed by the `@` character and the object's hashcode in hexadecimal form.

  However, it is common practice to override the `toString` method in your classes to provide a more meaningful string
  representation of the object. This can be useful for debugging and logging purposes.

  Here is an example of how to override the `toString` method:

    ```java
    public class Person {
        private String name;
        private int age;
    
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
    
        @Override
        public String toString() {
            return "Person{name='" + name + "', age=" + age + "}";
        }
    
        public static void main(String[] args) {
            Person person = new Person("John", 30);
            System.out.println(person.toString()); // Output: Person{name='John', age=30}
        }
    }
    ```

  In this example, the `toString` method is overridden to return a string that includes the `name` and `age` of
  the `Person` object.

- 29 . What is the use of equals method in Java?
  The `equals` method in Java is used to compare the equality of two objects. It is defined in the `Object` class and
  can be overridden in subclasses to provide custom equality logic. By default, the `equals` method compares object
  references, checking if two references point to the same object in memory.

  When overriding the `equals` method, it is important to follow these guidelines:
    - **Reflexive**: `x.equals(x)` should return `true`.
    - **Symmetric**: If `x.equals(y)` returns `true`, then `y.equals(x)` should also return `true`.
    - **Transitive**: If `x.equals(y)` and `y.equals(z)` both return `true`, then `x.equals(z)` should also return
      `true`.
    - **Consistent**: Multiple invocations of `x.equals(y)` should consistently return the same result.
      The `equals` method in Java is used to compare two objects for equality. It is defined in the `Object` class and
      can be overridden by any Java class to provide a custom equality comparison. The default implementation
      of `equals` in the `Object` class compares the memory addresses of the objects, meaning it checks if the two
      references point to the same object.

  Here is an example of how to override the `equals` method:

    ```java
    public class Person {
        private String name;
        private int age;
    
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
    
        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null || getClass() != obj.getClass()) {
                return false;
            }
            Person person = (Person) obj;
            return age == person.age && Objects.equals(name, person.name);
        }
    
        @Override
        public int hashCode() {
            return Objects.hash(name, age);
        }
    }
    ```

  In this example, the `equals` method is overridden to compare the `name` and `age` fields of `Person` objects to
  determine if they are equal. The `hashCode` method is also overridden to ensure that equal objects have the same hash
  code, which is important when using objects in collections like `HashSet` or `HashMap`.

- 30 . What are the important things to consider when implementing `equals` method?
    - **Reflexive**: `x.equals(x)` should return `true`.
    - **Symmetric**: If `x.equals(y)` returns `true`, then `y.equals(x)` should also return `true`.
    - **Transitive**: If `x.equals(y)` and `y.equals(z)` both return `true`, then `x.equals(z)` should also
      return `true`.
    - **Consistent**: Multiple invocations of `x.equals(y)` should consistently return the same result.
    - **Non-nullity**: `x.equals(null)` should return `false`.
    - **Type Check**: Ensure the object being compared is of the correct type.
    - **Field Comparison**: Compare significant fields that determine equality.
- 31 . What is the Hashcode method used for in Java?
  The `hashCode` method in Java is used to generate a unique integer value for an object. It is defined in the `Object`
  class and can be overridden in subclasses to provide a custom hash code calculation. The `hashCode` method is used
  primarily for objects that are stored in collections like `HashSet` or `HashMap`, where the hash code is used to
  determine the object's bucket location.

  When overriding the `hashCode` method, it is important to follow these guidelines:
  - **Consistency**: The hash code should be consistent for equal objects.
  - **Equality**: Equal objects should have the same hash code.
  - **Performance**: The hash code calculation should be efficient to avoid performance issues.

  Here is an example of how to override the `hashCode` method:

        ```java
        public class Person {
            private String name;
            private int age;
        
            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }
        
            @Override
            public int hashCode() {
                return Objects.hash(name, age);
            }
        }
        ```

  In this example, the `hashCode` method is overridden to generate a hash code based on the `name` and `age` fields of
  `Person` objects. This ensures that equal objects have the same hash code, which is important for using objects in
  collections like `HashSet` or `HashMap`.
- 32 . Explain inheritance with examples.
  Inheritance in Java is a mechanism where one class (subclass) inherits the fields and methods of another class (
  superclass). It allows for code reuse and establishes a relationship between classes.

  Here is an example:

    ```java
    // Superclass
    public class Animal {
        public void eat() {
            System.out.println("This animal eats food.");
        }
    }
    
    // Subclass
    public class Dog extends Animal {
        public void bark() {
            System.out.println("The dog barks.");
        }
    }
    
    // Main class to demonstrate inheritance
    public class Main {
        public static void main(String[] args) {
            Dog dog = new Dog();
            dog.eat();  // Inherited method from Animal class
            dog.bark(); // Method from Dog class
        }
    }
    ```

  In this example:
    - `Animal` is the superclass with a method `eat()`.
    - `Dog` is the subclass that inherits the `eat()` method from `Animal` and also has its own method `bark()`.
    - In the `Main` class, an instance of `Dog` can call both `eat()` and `bark()` methods.

- 33 . What is method overloading?
- 34 . What is method overriding?
- 35 . Can super class reference variable can hold an object of sub class?
- 36 . Is multiple inheritance allowed in Java?
- 37 . What is an interface?
- 38 . How do you define an interface?
- 39 . How do you implement an interface?
- 40 . Can you explain a few tricky things about interfaces?
- 41 . Can you extend an interface?
- 42 . Can a class extend multiple interfaces?
- 43 . What is an abstract class?
- 44 . When do you use an abstract class?
- 45 . How do you define an abstract method?
- 46 . Compare abstract class vs interface?
- 47 . What is a constructor?
- 48 . What is a default constructor?
- 49 . Will this code compile?
- 50 . How do you call a super class constructor from a constructor?
- 51 . Will this code compile?
- 52 . What is the use of this()?
- 53 . Can a constructor be called directly from a method?
- 54 . Is a super class constructor called even when there is no explicit call from a sub class constructor?

### Advanced object oriented concepts

- 55 . What is polymorphism?
- 56 . What is the use of instanceof operator in Java?
- 57 . What is coupling?
- 58 . What is cohesion?
- 59 . What is encapsulation?
- 60 . What is an inner class?
- 61 . What is a static inner class?
- 62 . Can you create an inner class inside a method?
- 63 . What is an anonymous class?

### Modifiers

- 64 . What is default class modifier?
- 65 . What is private access modifier?
- 66 . What is default or package access modifier?
- 67 . What is protected access modifier?
- 68 . What is public access modifier?
- 69 . What access types of variables can be accessed from a class in same package?
- 70 . What access types of variables can be accessed from a class in different package?
- 71 . What access types of variables can be accessed from a sub class in same package?
- 72 . What access types of variables can be accessed from a sub class in different package?
- 73 . What is the use of a final modifier on a class?
- 74 . What is the use of a final modifier on a method?
- 75 . What is a final variable?
- 76 . What is a final argument?
- 77 . What happens when a variable is marked as volatile?
- 78 . What is a static variable?

### conditions & loops

- 79 . Why should you always use blocks around if statement?
- 80 . Guess the output
- 81 . Guess the output
- 82 . Guess the output of this switch block .
- 83 . Guess the output of this switch block?
- 84 . Should default be the last case in a switch statement?
- 85 . Can a switch statement be used around a String
- 86 . Guess the output of this for loop (P.S. there is an error as the output of given question should be
  0-1-2-3-4-5-6-7-8-9. So please ignore that.)
- 87 . What is an enhanced for loop?
- 88 . What is the output of the for loop below?
- 89 . What is the output of the program below?
- 90 . What is the output of the program below?

### Exception handling

- 91 . Why is exception handling important?
- 92 . What design pattern is used to implement exception handling features in most languages?
- 93 . What is the need for finally block?
- 94 . In what scenarios is code in finally not executed?
- 95 . Will finally be executed in the program below?
- 96 . Is try without a catch is allowed?
- 97 . Is try without catch and finally allowed?
- 98 . Can you explain the hierarchy of exception handling classes?
- 99 . What is the difference between error and exception?
- 100 . What is the difference between checked exceptions and unchecked exceptions?
- 101 . How do you throw an exception from a method?
- 102 . What happens when you throw a checked exception from a method?
- 103 . What are the options you have to eliminate compilation errors when handling checked exceptions?
- 104 . How do you create a custom exception?
- 105 . How do you handle multiple exception types with same exception handling block?
- 106 . Can you explain about try with resources?
- 107 . How does try with resources work?
- 108 . Can you explain a few exception handling best practices?

### Miscellaneous topics

- 109 . What are the default values in an array?
- 110 . How do you loop around an array using enhanced for loop?
- 111 . How do you print the content of an array?
- 112 . How do you compare two arrays?
- 113 . What is an enum?
- 114 . Can you use a switch statement around an enum?
- 115 . What are variable arguments or varargs?
- 116 . What are asserts used for?
- 117 . When should asserts be used?
- 118 . What is garbage collection?
- 119 . Can you explain garbage collection with an example?
- 120 . When is garbage collection run?
- 121 . What are best practices on garbage collection?
- 122 . What are initialization blocks?
- 123 . What is a static initializer?
- 124 . What is an instance initializer block?
- 125 . What is tokenizing?
- 126 . Can you give an example of tokenizing?
- 127 . What is serialization?
- 128 . How do you serialize an object using serializable interface?
- 129 . How do you de-serialize in Java?
- 130 . What do you do if only parts of the object have to be serialized?
- 131 . How do you serialize a hierarchy of objects?
- 132 . Are the constructors in an object invoked when it is de-serialized?
- 133 . Are the values of static variables stored when an object is serialized?

### Collections

- 134 . Why do we need collections in Java?
- 135 . What are the important interfaces in the collection hierarchy?
- 136 . What are the important methods that are declared in the collection interface?
- 137 . Can you explain briefly about the List interface?
- 138 . Explain about ArrayList with an example?
- 139 . Can an ArrayList have duplicate elements?
- 140 . How do you iterate around an ArrayList using iterator?
- 141 . How do you sort an ArrayList?
- 142 . How do you sort elements in an ArrayList using comparable interface?
- 143 . How do you sort elements in an ArrayList using comparator interface?
- 144 . What is vector class? How is it different from an ArrayList?
- 145 . What is linkedList? What interfaces does it implement? How is it different from an ArrayList?
- 146 . Can you briefly explain about the Set interface?
- 147 . What are the important interfaces related to the Set interface?
- 148 . What is the difference between Set and sortedSet interfaces?
- 149 . Can you give examples of classes that implement the Set interface?
- 150 . What is a HashSet?
- 151 . What is a linkedHashSet? How is different from a HashSet?
- 152 . What is a TreeSet? How is different from a HashSet?
- 153 . Can you give examples of implementations of navigableSet?
- 154 . Explain briefly about Queue interface?
- 155 . What are the important interfaces related to the Queue interface?
- 156 . Explain about the Deque interface?
- 157 . Explain the BlockingQueue interface?
- 158 . What is a priorityQueue?
- 159 . Can you give example implementations of the BlockingQueue interface?
- 160 . Can you briefly explain about the Map interface?
- 161 . What is difference between Map and sortedMap?
- 162 . What is a HashMap?
- 163 . What are the different methods in a Hash Map?
- 164 . What is a TreeMap? How is different from a HashMap?
- 165 . Can you give an example of implementation of navigableMap interface?
- 166 . What are the static methods present in the collections class?

### Advanced collections

- 167 . What is the difference between synchronized and concurrent collections in Java?
- 168 . Explain about the new concurrent collections in Java?
- 169 . Explain about copyonwrite concurrent collections approach?
- 170 . What is compareandswap approach?
- 171 . What is a lock? How is it different from using synchronized approach?
- 172 . What is initial capacity of a Java collection?
- 173 . What is load factor?
- 174 . When does a Java collection throw UnsupportedOperationException?
- 175 . What is difference between fail-safe and fail-fast iterators?
- 176 . What are atomic operations in Java?
- 177 . What is BlockingQueue in Java?

### Generics

- 178 . What are Generics?
- 179 . Why do we need Generics? Can you give an example of how Generics make a program more flexible?
- 180 . How do you declare a generic class?
- 181 . What are the restrictions in using generic type that is declared in a class declaration?
- 182 . How can we restrict Generics to a subclass of particular class?
- 183 . How can we restrict Generics to a super class of particular class?
- 184 . Can you give an example of a generic method?

### Multi threading

- 185 . What is the need for threads in Java?
- 186 . How do you create a thread?
- 187 . How do you create a thread by extending thread class?
- 188 . How do you create a thread by implementing runnable interface?
- 189 . How do you run a thread in Java?
- 190 . What are the different states of a thread?
- 191 . What is priority of a thread? How do you change the priority of a thread?
- 192 . What is executorservice?
- 193 . Can you give an example for executorservice?
- 194 . Explain different ways of creating executor services .
- 195 . How do you check whether an executionservice task executed successfully?
- 196 . What is callable? How do you execute a callable from executionservice?
- 197 . What is synchronization of threads?
- 198 . Can you give an example of a synchronized block?
- 199 . Can a static method be synchronized?
- 200 . What is the use of join method in threads?
- 201 . Describe a few other important methods in threads?
- 202 . What is a deadlock?
- 203 . What are the important methods in Java for inter-thread communication?
- 204 . What is the use of wait method?
- 205 . What is the use of notify method?
- 206 . What is the use of notifyall method?
- 207 . Can you write a synchronized program with wait and notify methods?

### Functional Programming - Lamdba expressions and Streams

- 208 . What is functional programming?
- 209 . Can you give an example of functional programming?
- 210 . What is a stream?
- 211 . Explain about streams with an example?
- what are intermediate operations in streams?
- 212 . What are terminal operations in streams?
- 213 . What are method references?
- 214 . What are lambda expressions?
- 215 . Can you give an example of lambda expression?
- 216 . Can you explain the relationship between lambda expression and functional interfaces?
- 217 . What is a predicate?
- 218 . What is the functional interface - function?
- 219 . What is a consumer?
- 220 . Can you give examples of functional interfaces with multiple arguments?

### New Features

- 221 . What are the new features in Java 5?
- 222 . What are the new features in Java 6?
- 223 . What are the new features in Java 7?
- 224 . What are the new features in Java 8?

### What you can do next?

- [Design Patterns] (https://www.youtube.com/watch?v=f5Rzr5mVNbY)
- [Maven] (https://courses.in28minutes.com/p/maven-tutorial-for-beginners-in-5-steps)
- [JSP Servlets] (https://www.youtube.com/watch?v=Vvnliarkw48)
- [Spring MVC] (https://www.youtube.com/watch?v=BjNhGaZDr0Y)

### Troubleshooting

- Refer our TroubleShooting
  Guide - https://github.com/in28minutes/in28minutes-initiatives/tree/master/The-in28Minutes-TroubleshootingGuide-And-FAQ

## Youtube Playlists - 500+ Videos

[Click here - 30+ Playlists with 500+ Videos on Spring, Spring Boot, REST, Microservices and the Cloud](https://www.youtube.com/user/rithustutorials/playlists?view=1&sort=lad&flow=list)

## Keep Learning in28Minutes

in28Minutes is creating amazing solutions for you to learn Spring Boot, Full Stack and the Cloud - Docker, Kubernetes,
AWS, React, Angular etc. - [Check out all our courses here](https://github.com/in28minutes/learn)
