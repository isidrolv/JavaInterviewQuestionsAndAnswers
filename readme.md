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

- 16 . Are all String’s immutable?
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
  Method overloading in Java is a feature that allows a class to have more than one method with the same name, provided
  their parameter lists are different. This means that the methods must differ in the type, number, or order of their
  parameters. Method overloading is a compile-time polymorphism technique, enabling different methods to perform similar
  operations with varying inputs. It enhances code readability and reusability by allowing the same method name to be
  used for different tasks, based on the arguments passed. Overloaded methods can have different return types, but this
  alone is not enough for overloading; the parameter list must be different.
- 34 . What is method overriding?
- 35 . Can super class reference variable can hold an object of sub class?
- 36 . Is multiple inheritance allowed in Java?
- 37 . What is an interface?
  An interface in Java is a reference type, similar to a class, that can contain only constants, method signatures,
  default methods, static methods, and nested types. Interfaces cannot contain instance fields or constructors. They are
  used to specify a set of methods that a class must implement. An interface is a way to achieve abstraction and
  multiple inheritance in Java.

Here is an example of an interface:

```java
public interface Animal {
    void eat();

    void sleep();

}
```

A class that implements this interface must provide implementations for the `eat` and `sleep` methods:

```java
public class Dog implements Animal {
    @Override
    public void eat() {
        System.out.println("Dog is eating");
    }

    @Override
    public void sleep() {
        System.out.println("Dog is sleeping");
    }

}
```

- 38 . How do you define an interface?

  An interface in Java is defined using the `interface` keyword. It can contain abstract methods, default methods,
  static methods, and constants. Here is an example:

  ```java
  public interface Animal {
      void eat();
      void sleep();
  }
  ```
- 39 . How do you implement an interface?
  To implement an interface in Java, a class must use the `implements` keyword and provide concrete implementations for
  all the methods declared in the interface. Here is an example:

    ```java
    public interface Animal {
        void eat();
        void sleep();
    }
    
    public class Dog implements Animal {
        @Override
        public void eat() {
            System.out.println("Dog is eating");
        }
    
        @Override
        public void sleep() {
            System.out.println("Dog is sleeping");
        }
    }
    ```

  In this example:
    - The `Animal` interface declares two methods: `eat` and `sleep`.
    - The `Dog` class implements the `Animal` interface and provides concrete implementations for the `eat` and `sleep`
      methods.

- 40 . Can you explain a few tricky things about interfaces?
  Here are a few tricky things about interfaces in Java:

    1. **Default Methods**: Interfaces can have default methods with a body. This allows adding new methods to
       interfaces without breaking existing implementations.
        ```java
        public interface MyInterface {
            void existingMethod();
          
            default void newMethod() {
                System.out.println("New default method");
            }
        }
        ```

    2. **Static Methods**: Interfaces can also have static methods. These methods belong to the interface and not to the
       instance of the class implementing the interface.
        ```java
        public interface MyInterface {
            static void staticMethod() {
                System.out.println("Static method in interface");
            }
        }
        ```

    3. **Multiple Inheritance**: A class can implement multiple interfaces, allowing for a form of multiple inheritance.
       However, if two interfaces have default methods with the same signature, the implementing class must override the
       method to resolve the conflict.
        ```java
        public interface InterfaceA {
            default void commonMethod() {
                System.out.println("InterfaceA");
            }
        }
  
        public interface InterfaceB {
            default void commonMethod() {
                System.out.println("InterfaceB");
            }
        }
  
        public class MyClass implements InterfaceA, InterfaceB {
            @Override
            public void commonMethod() {
                InterfaceA.super.commonMethod(); // or InterfaceB.super.commonMethod();
            }
        }
        ```

    4. **Private Methods**: Since Java 9, interfaces can have private methods. These methods can be used to share code
       between default methods.
        ```java
        public interface MyInterface {
            default void defaultMethod() {
                privateMethod();
            }
  
            private void privateMethod() {
                System.out.println("Private method in interface");
            }
        }
        ```

    5. **Inheritance of Constants**: Interfaces can declare constants, which are implicitly `public`, `static`, and
       `final`. Implementing classes can access these constants directly.
        ```java
        public interface MyInterface {
            int CONSTANT = 100;
        }
  
        public class MyClass implements MyInterface {
            public void printConstant() {
                System.out.println(CONSTANT);
            }
        }
        ```
- 41 . Can you extend an interface?
  Yes, in Java, an interface can extend another interface. This allows the extending interface to inherit the abstract
  methods of the parent interface. Here is an example:

    ```java
    public interface Animal {
        void eat();
        void sleep();
    }
    
    public interface Dog extends Animal {
        void bark();
    }
    ```
  In this example, the `Dog` interface extends the `Animal` interface, inheriting its methods (`eat` and `sleep`) and
  adding a new method (`bark`).

- 42 . Can a class extend multiple interfaces?
  Yes, in Java, a class can implement multiple interfaces. This allows the class to inherit the abstract methods of all
  the interfaces it implements. Here is an example:

    ```java
    public interface Animal {
        void eat();
        void sleep();
    }
    
    public interface Pet {
        void play();
    }
    
    public class Dog implements Animal, Pet {
        @Override
        public void eat() {
            System.out.println("Dog is eating");
        }
    
        @Override
        public void sleep() {
            System.out.println("Dog is sleeping");
        }
    
        @Override
        public void play() {
            System.out.println("Dog is playing");
        }
    }
    ```
  In this example, the `Dog` class implements both the `Animal` and `Pet` interfaces, providing concrete implementations
  for all the methods declared in the interfaces.
- 43 . What is an abstract class?
  An abstract class in Java is a class that cannot be instantiated on its own and is meant to be subclassed by other
  classes. It can contain abstract methods, which are declared but not implemented, as well as concrete methods with
  implementations. Abstract classes are used to define a common interface for subclasses and to provide default behavior
  that can be overridden by subclasses.

  Here is an example of an abstract class:

    ```java
    public abstract class Animal {
        public abstract void eat();
        public void sleep() {
            System.out.println("Animal is sleeping");
        }
    }
    ```

  In this example, the `Animal` class is declared
- 44 . When do you use an abstract class?
  You should use an abstract class in Java when you want to define a common interface for a group of subclasses and
  provide default behavior that can be overridden by the subclasses. Abstract classes are useful when you have a set of
  classes that share common methods or fields, but each class may implement those methods differently. By defining an
  abstract class with abstract methods, you can ensure that all subclasses provide their own implementations for those
  methods.

  Here are some common scenarios where you might use an abstract class:
    - When you want to define a template for a group of related classes.
    - When you want to provide default implementations for some methods that can be overridden by subclasses.
    - When you want to define a common interface for a group of classes that share similar behavior.

  Abstract classes are a powerful tool in Java for creating hierarchies of classes with shared behavior and structure.
- 45 . How do you define an abstract method?
  An abstract method in Java is a method that is declared but not implemented in an abstract class. Abstract methods do
  not have a body and are meant to be implemented by subclasses. To define an abstract method, you use the `abstract`
  keyword in the method signature. Here is an example:

    ```java
    public abstract class Animal {
        public abstract void eat();
    }
    ```

  In this example, the `eat` method is declared as abstract in the `Animal` class, meaning that any subclass of `Animal`
  must provide an implementation for the `eat` method.
- 46 . Compare abstract class vs interface?
    - **Abstract Class**:
        - Can have both abstract and concrete methods.
        - Can have instance variables.
        - Can provide method implementations.
        - Can have constructors.
        - Supports single inheritance.
        - Can have access modifiers for methods and variables.

    - **Interface**:
        - Can only have abstract methods (until Java 8, which introduced default and static methods).
        - Cannot have instance variables (only constants).
        - Cannot provide method implementations (except default and static methods from Java 8).
        - Cannot have constructors.
        - Supports multiple inheritance.
        - All methods are implicitly public and abstract (except default and static methods).
- 47 . What is a constructor?
  A constructor in Java is a special type of method that is used to initialize objects. It is called when an object of a
  class is created using the `new` keyword. Constructors have the same name as the class and do not have a return type.
  They can have parameters to initialize the object's state.

  There are two types of constructors in Java:
    - **Default Constructor**: A constructor with no parameters is called a default constructor. If a class does not
      have
      any constructor defined, a default constructor is provided by the compiler.
    - **Parameterized Constructor**: A constructor with parameters is called a parameterized constructor. It allows you
      to
      pass values to initialize the object's state.

  Here is an example of a constructor:

    ```java
    public class Person {
        private String name;
        private int age;
    
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
    }
    ```

  In this example, the `Person` class has a parameterized constructor that initializes the `name` and `age` fields of
  the `Person` object.
- 48 . What is a default constructor?
  A default constructor in Java is a constructor that is automatically provided by the compiler if a class does not have
  any constructor defined. It is a no-argument constructor that initializes the object with default values. The default
  constructor is used when an object is created without passing any arguments to the constructor.

  Here is an example of a default constructor:

    ```java
    public class Person {
        private String name;
        private int age;
    
        // Default constructor provided by the compiler
        public Person() {
            this.name = "Unknown";
            this.age = 0;
        }
    }
    ```

  In this example, the `Person` class does not have any constructor defined, so the compiler provides a default
  constructor that initializes the `name` and `age` fields with default values.
- 49 . Will this code compile?
  Here is an example of a Java code segment that will not compile due to a missing semicolon:

    ```java
    public class Example {
        public static void main(String[] args) {
            System.out.println("Hello, World!") // Missing semicolon here
        }
    }
    ```
  Here is an example of a Java code segment that will compile successfully:

    ```java
    public class Example {
        public static void main(String[] args) {
            System.out.println("Hello, World!");
        }
    }
    ```
- 50 . How do you call a super class constructor from a constructor?
  In Java, you can call a superclass constructor from a subclass constructor using the `super` keyword. This is useful
  when you want to initialize the superclass part of the object before initializing the subclass part. The `super`
  keyword must be the first statement in the subclass constructor
  To call a superclass constructor from a constructor in Java, you use the `super` keyword followed by the appropriate
  arguments. This must be the first statement in the subclass constructor.

  Here is an example:

    ```java
    public class SuperClass {
        public SuperClass(String message) {
            System.out.println(message);
        }
    }
    
    public class SubClass extends SuperClass {
        public SubClass() {
            super("Hello from SuperClass");
        }
    }
    ```

  In this example, the `SubClass` constructor calls the `SuperClass` constructor with the argument
  `"Hello from SuperClass"`.
- 51 . Will this code compile?
- 52 . What is the use of this()?
- 53 . Can a constructor be called directly from a method?
  No, a constructor cannot be called directly from a method. Constructors are special methods that are called only when
  an object is created. However, you can call another constructor from a constructor using `this()` or `super()`. If you
  need to initialize an object within a method, you should create a new instance of the class using the `new` keyword.
- 54 . Is a super class constructor called even when there is no explicit call from a sub class constructor?
  Yes, a superclass constructor is always called, even if there is no explicit call from a subclass constructor. If a
  subclass constructor does not explicitly call a superclass constructor using `super()`, the Java compiler
  automatically inserts a call to the no-argument constructor of the superclass. If the superclass does not have a
  no-argument constructor, a compilation error will occur. This ensures that the superclass part of the object is.

### Advanced object oriented concepts

- 55 . What is polymorphism?
  Polymorphism in Java is the ability of an object to take on many forms. It allows one interface to be used for a
  general class of actions. The specific action is determined by the exact nature of the situation. Polymorphism is
  mainly achieved through method overriding and method overloading.

    - **Method Overriding**: When a subclass provides a specific implementation of a method that is already defined in
      its superclass.
    - **Method Overloading**: When multiple methods have the same name but different parameters within the same class.

  Polymorphism allows for flexibility and the ability to define methods that can be used interchangeably, making the
  code more modular and easier to maintain.
- 56 . What is the use of instanceof operator in Java?
  The `instanceof` operator in Java is used to test whether an object is an instance of a specific class or implements a
  specific interface. It returns `true` if the object is an instance of the specified class or interface, and `false`
  otherwise. This operator is useful for type checking before performing type-specific operations.

  Here is an example:

    ```java
    public class Main {
        public static void main(String[] args) {
            Animal animal = new Dog();
            
            if (animal instanceof Dog) {
                Dog dog = (Dog) animal;
                dog.bark();
            }
        }
    }
    
    class Animal {
        // Animal class code
    }
    
    class Dog extends Animal {
        public void bark() {
            System.out.println("Woof!");
        }
    }
    ```

  In this example, the `instanceof` operator checks if the `animal` object is an instance of the `Dog` class before
  casting it to `Dog` and calling the `bark` method.
- 57 . What is coupling?
  Coupling in software engineering refers to the degree of direct knowledge that one module has about another. It
  measures how closely connected two routines or modules are. High coupling means that modules are highly dependent on
  each other, which can make the system more difficult to understand, maintain, and modify. Low coupling, on the other
  hand, means that modules are more independent, which can lead to a more modular and flexible system.
  Coupling in Java refers to the degree of interdependence between classes or modules. It measures how closely classes
  are connected or dependent on each other. Low coupling is desirable as it promotes modularity, reusability, and
  maintainability of code. High coupling can lead to code that is difficult to change, test, and maintain.

  There are different types of coupling:
    - **Tight Coupling**: Classes are highly dependent on each other, making changes in one class affect other classes.
    - **Loose Coupling**: Classes are independent and interact through well-defined interfaces, reducing dependencies.

  To reduce coupling, it is important to follow good design principles like encapsulation, abstraction, and separation
  of concerns.
- 58 . What is cohesion?
  Cohesion in software engineering refers to the degree to which the elements inside a module belong together. It
  measures how closely related the responsibilities of a single module are. High cohesion means that the elements within
  a module are strongly related and work together to achieve a common goal. Low cohesion, on the other hand, means that
  the elements within a module are loosely related and may not work well together.

  Cohesion in Java refers to the degree to which the methods in a class are related and work together to achieve a
  common purpose. High cohesion is desirable as it promotes code that is easier to understand, maintain, and test. Low
  cohesion can lead to code that is difficult to follow, modify, and debug.
- 59 . What is encapsulation?
  Encapsulation in Java is a fundamental object-oriented programming concept that involves bundling the data (fields)
  and the methods (functions) that operate on the data into a single unit, called a class. It restricts direct access to
  some of the object's components, which can help prevent the accidental modification of data. Encapsulation is achieved
  by:

    1. Declaring the fields of a class as private.
    2. Providing public getter and setter methods to access and update the value of the private fields.

  Here is an example:

    ```java
    public class Person {
        private String name;
        private int age;
    
        // Getter method for name
        public String getName() {
            return name;
        }
    
        // Setter method for name
        public void setName(String name) {
            this.name = name;
        }
    
        // Getter method for age
        public int getAge() {
            return age;
        }
    
        // Setter method for age
        public void setAge(int age) {
            this.age = age;
        }
    }
    ```

  In this example, the `name` and `age` fields are private, and they can only be accessed and modified through the
  public getter and setter methods. This ensures that the internal state of the object is protected and can only be
  changed in a controlled manner.
- 60 . What is an inner class?
  An inner class in Java is a class that is defined within another class. Inner classes can access the members (
  including private members) of the outer class. There are four types of inner classes in Java:

    1. **Member Inner Class**: A class defined within another class.
    2. **Static Nested Class**: A static class defined within another class.
    3. **Local Inner Class**: A class defined within a method.
    4. **Anonymous Inner Class**: A class without a name, defined and instantiated in a single statement.

  Here is an example of a member inner class:

    ```java
    public class OuterClass {
        private int outerField = 10;
    
        class InnerClass {
            void display() {
                System.out.println("Outer field value: " + outerField);
            }
        }
    
        public static void main(String[] args) {
            OuterClass outer = new OuterClass();
            OuterClass.InnerClass inner = outer.new InnerClass();
            inner.display();
        }
    }
    ```

  In this example, `InnerClass` is an inner class within `OuterClass` and can access the `outerField` of `OuterClass`.
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
  The `final` modifier on a class in Java is used to prevent the class from being subclassed. This means that no other
  class can extend a `final` class. It is often used to create immutable classes or to ensure that the implementation of
  the class cannot be altered through inheritance.

  Example:
    ```java
    public final class MyClass {
        // class implementation
    }
    ```

  In this example, `MyClass` cannot be extended by any other class.
- 74 . What is the use of a final modifier on a method?
  The `final` modifier on a method in Java is used to prevent the method from being overridden by subclasses. This
  ensures that the implementation of the method remains unchanged in any subclass.

  Here is an example:

    ```java
    public class SuperClass {
        public final void display() {
            System.out.println("This is a final method.");
        }
    }
    
    public class SubClass extends SuperClass {
        // This will cause a compilation error
        // public void display() {
        //     System.out.println("Trying to override a final method.");
        // }
    }
    ```

  In this example, the `display` method in `SuperClass` is marked as `final`, so it cannot be overridden in `SubClass`.
- 75 . What is a final variable?
- 76 . What is a final argument?
  A final argument in Java is a method parameter that is declared with the `final` keyword. This means that once the
  parameter is assigned a value, it cannot be changed within the method. This is useful for ensuring that the parameter
  remains constant throughout the method execution.

  Here is an example:

    ```java
    public void exampleMethod(final int finalParam) {
        // finalParam cannot be reassigned
        // finalParam = 10; // This would cause a compilation error
        System.out.println(finalParam);
    }
    ```

  In this example, `finalParam` is a final argument, and any attempt to reassign it within the method will result in a
  compilation error.
- 77 . What happens when a variable is marked as volatile?
  When a variable is marked as `volatile` in Java, it ensures that the value of the variable is always read from and
  written to the main memory, rather than being cached in a thread's local memory. This guarantees visibility of changes
  to the variable across all threads. The `volatile` keyword is used to prevent memory consistency errors in concurrent
  programming.
- 78 . What is a static variable?
  A static variable in Java is a variable that is shared among all instances of a class. It is declared using the
  `static` keyword and belongs to the class rather than any specific instance. This means that there is only one copy of
  the static variable, regardless of how many instances of the class are created. Static variables are often used for
  constants or for sharing data among instances.

  Here is an example:

    ```java
    public class Example {
        // Static variable
        static int staticVariable = 10;
    
        public static void main(String[] args) {
            // Accessing static variable
            System.out.println(Example.staticVariable);
        }
    }
    ```

  In this example, `staticVariable` is a static variable that can be accessed using the class name `Example`.

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
  Errors and exceptions are both types of problems that can occur during the execution of a program, but they are
  handled differently in Java:

    - **Error**: Errors are serious issues that are typically outside the control of the program and indicate problems
      with the environment in which the application is running. Examples include `OutOfMemoryError`,
      `StackOverflowError`, and `VirtualMachineError`. Errors are usually not recoverable and should not be caught or
      handled by the application.

    - **Exception**: Exceptions are conditions that a program might want to catch and handle. They are divided into two
      main categories:
        - **Checked Exceptions**: These are exceptions that are checked at compile-time. The programmer is required to
          handle these exceptions, either by using a `try-catch` block or by declaring them in the method signature
          using the `throws` keyword. Examples include `IOException`, `SQLException`, and `FileNotFoundException`.
        - **Unchecked Exceptions**: These are exceptions that are not checked at compile-time but occur during runtime.
          They are subclasses of `RuntimeException` and do not need to be declared or caught. Examples include
          `NullPointerException`, `ArrayIndexOutOfBoundsException`, and `IllegalArgumentException`.
- 101 . How do you throw an exception from a method?
  To throw an exception from a method in Java, you use the `throw` keyword followed by an instance of the exception
  class.
  This allows you to create and throw custom exceptions or to re-throw exceptions that were caught earlier. Here is an
  example:

    ```java
    public void exampleMethod() {
        throw new RuntimeException("An error occurred");
    }
    ```

  In this example, the `exampleMethod` throws a `RuntimeException` with the message `"An error occurred"`.
- 102 . What happens when you throw a checked exception from a method?\
  When you throw a checked exception from a method in Java, you must either catch the exception using a `try-catch`
  block or declare the exception using the `throws` keyword in the method signature. If you throw a checked exception
  without handling it, the code will not compile, and you will get a compilation error. Checked exceptions are checked
  at
  compile-time to ensure that they are handled properly.
- 103 . What are the options you have to eliminate compilation errors when handling checked exceptions?\
    When handling checked exceptions in Java, you have several options to eliminate compilation errors:

    1. **Catch the Exception**: Use a `try-catch` block to catch the exception and handle it within the method.
    2. **Declare the Exception**: Use the `throws` keyword in the method signature to declare the exception and pass the
       responsibility of handling it to the calling method.
    3. **Handle the Exception**: Use a combination of catching and declaring the exception to handle it at different
       levels of the call stack.
    4. **Wrap the Exception**: Wrap the checked exception in a runtime exception and re-throw it to avoid the need for
       handling or declaring the exception.
    5. **Use a Lambda Expression**: Use a lambda expression to handle the exception in a functional interface that does
       not declare checked exceptions.
- 104 . How do you create a custom exception?
- 105 . How do you handle multiple exception types with same exception handling block?
- 106 . Can you explain about try with resources?
- 107 . How does try with resources work?
- 108 . Can you explain a few exception handling best practices?

### Miscellaneous topics

- 109 . What are the default values in an array? \
    In Java, when an array is created, the elements are initialized to default values based on the type of the array. The
    default values for primitive types are as follows:

    - **byte**: 0
    - **short**: 0
    - **int**: 0
    - **long**: 0L
    - **float**: 0.0f
    - **double**: 0.0d
    - **char**: '\u0000'
    - **boolean**: false

  For reference types (objects), the default value is `null`. For example, the default value of an `int` array is `0`.
- 110 . How do you loop around an array using enhanced for loop?
- 111 . How do you print the content of an array?
- 112 . How do you compare two arrays? \
    In Java, you can compare two arrays using the `Arrays.equals` method from the `java.util` package. This method
    compares the contents of two arrays to determine if they are equal. It takes two arrays as arguments and returns
    `true` if the arrays are equal and `false` otherwise. The comparison is done element by element, so the arrays must
    have the same length and contain the same elements in the same order.

    Here is an example:

    ```java
    import java.util.Arrays;

    public class Main {
        public static void main(String[] args) {
            int[] array1 = {1, 2, 3, 4, 5};
            int[] array2 = {1, 2, 3, 4, 5};

            boolean isEqual = Arrays.equals(array1, array2);
            System.out.println("Arrays are equal: " + isEqual);
        }
    }
    ```

    In this example, the `Arrays.equals` method is used to compare the `array1` and `array2` arrays, and the result is
    printed to the console.
- 113 . What is an enum? \
    An enum in Java is a special data type that represents a group of constants (unchangeable variables). It is used to
    define a set of named constants that can be used in place of integer values. Enumerations are defined using the
    `enum` keyword and can contain constructors, methods, and fields.

    Here is an example of an enum:

    ```java
    public enum Day {
        SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
    }
    ```

    In this example, the `Day` enum defines a set of constants representing the days of the week. Each constant is
    implicitly declared as a public static final field of the `Day` enum. 
- 114 . Can you use a switch statement around an enum? \
    Yes, you can use a switch statement around an enum in Java. Enumerations are often used with switch statements to
    provide a more readable and type-safe alternative to using integer values. Each constant in the enum can be used as a
    case label in the switch statement.

    Here is an example:

    ```java
    public enum Day {
        SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
    }

    public class Main {
        public static void main(String[] args) {
            Day day = Day.MONDAY;

            switch (day) {
                case SUNDAY:
                    System.out.println("It's Sunday");
                    break;
                case MONDAY:
                    System.out.println("It's Monday");
                    break;
                case TUESDAY:
                    System.out.println("It's Tuesday");
                    break;
                case WEDNESDAY:
                    System.out.println("It's Wednesday");
                    break;
                case THURSDAY:
                    System.out.println("It's Thursday");
                    break;
                case FRIDAY:
                    System.out.println("It's Friday");
                    break;
                case SATURDAY:
                    System.out.println("It's Saturday");
                    break;
                default:
                    System.out.println("Invalid day");
            }
        }
    }
    ```

    In this example, the `Day` enum is used with a switch statement to print the day of the week based on the value of the
    `day` variable. 
- 115 . What are variable arguments or varargs? \
    Variable arguments, also known as varargs, allow you to pass a variable number of arguments to a method. This
    feature was introduced in Java 5 and is denoted by an ellipsis (`...`) after the type of the last parameter in the
    method signature. Varargs are represented as an array within the method and can be used to pass any number of
    arguments of the specified type.

    Here is an example:

    ```java
    public class Main {
        public static void main(String[] args) {
            printNumbers(1, 2, 3, 4, 5);
        }

        public static void printNumbers(int... numbers) {
            for (int number : numbers) {
                System.out.println(number);
            }
        }
    }
    ```

    In this example, the `printNumbers` method accepts a variable number of `int` arguments using varargs. The method
    can be called with any number of `int` values, and they will be treated as an array within the method.
- 116 . What are asserts used for?
- 117 . When should asserts be used?
- 118 . What is garbage collection?
- 119 . Can you explain garbage collection with an example?
- 120 . When is garbage collection run?
- 121 . What are best practices on garbage collection?
- 122 . What are initialization blocks?
- 123 . What is a static initializer?
- 124 . What is an instance initializer block?
- 125 . What is tokenizing? \
    Tokenizing in Java refers to the process of breaking a string into smaller parts, called tokens. This is often done
    to extract individual words, numbers, or other elements from a larger string. Tokenizing is commonly used in parsing
    and text processing tasks to analyze and manipulate text data.

    Here is an example of tokenizing a string:

    ```java
    public class Main {
        public static void main(String[] args) {
            String sentence = "Hello, world! This is a sentence.";
            String[] tokens = sentence.split(" ");

            for (String token : tokens) {
                System.out.println(token);
            }
        }
    }
    ```

    In this example, the `split` method is used to tokenize the `sentence` string by splitting it into individual words
    based on the space character. The resulting tokens are then printed to the console.
- 126 . Can you give an example of tokenizing?
- 127 . What is serialization?
- 128 . How do you serialize an object using serializable interface?
- 129 . How do you de-serialize in Java?
- 130 . What do you do if only parts of the object have to be serialized?
- 131 . How do you serialize a hierarchy of objects?
- 132 . Are the constructors in an object invoked when it is de-serialized?
- 133 . Are the values of static variables stored when an object is serialized?

### Collections

- 134 . Why do we need collections in Java? \
    Collections in Java are used to store, retrieve, manipulate, and process groups of objects. They provide a way to
    organize and manage data in a structured and efficient manner. Collections offer a wide range of data structures and
    algorithms that can be used to perform common operations like searching, sorting, and iterating over elements. By
    using collections, developers can write more efficient and maintainable code, as well as take advantage of
    pre-built data structures and algorithms provided by the Java Collections Framework.

    Some key reasons why we need collections in Java include:
    - **Efficient Data Storage**: Collections provide efficient data structures for storing and organizing large amounts
      of data.
    - **Data Manipulation**: Collections offer methods for adding, removing, and updating elements in a structured
      manner.
    - **Algorithms and Operations**: Collections provide algorithms and operations for common tasks like searching,
      sorting, and iterating over elements.
    - **Type Safety**: Collections ensure type safety by providing generic classes that can store specific types of
      objects.
    - **Code Reusability**: Collections allow developers to reuse pre-built data structures and algorithms, saving time
      and effort in implementing common tasks.
    - **Scalability**: Collections can scale to handle large amounts of data and provide efficient performance for
      various operations.
    - **Flexibility**: Collections offer a wide range of data structures and interfaces that can be used to meet
      different requirements and use cases.
- 135 . What are the important interfaces in the collection hierarchy? \
    The Java Collections Framework provides a set of interfaces that define the core functionality of collections in
    Java. Some of the important interfaces in the collection hierarchy include:

    - **Collection**: The root interface in the collection hierarchy that defines basic operations for working with
      collections of objects.
    - **List**: An interface that extends `Collection` and represents an ordered collection of elements that allows
      duplicates.
    - **Set**: An interface that extends `Collection` and represents a collection of unique elements with no duplicates.
    - **Queue**: An interface that extends `Collection` and represents a collection of elements in a specific order for
      processing.
    - **Deque**: An interface that extends `Queue` and represents a double-ended queue that allows elements to be added
      or removed from both ends.
    - **Map**: An interface that represents a collection of key-value pairs where each key is unique and maps to a
      single value.
    - **SortedSet**: An interface that extends `Set` and represents a set of elements sorted in a specific order.
    - **SortedMap**: An interface that extends `Map` and represents a map of key-value pairs sorted by the keys.
    - **NavigableSet**: An interface that extends `SortedSet` and provides navigation methods for accessing elements in
      a set.
    - **NavigableMap**: An interface that extends `SortedMap` and provides navigation methods for accessing key-value
      pairs in a map.

    These interfaces define common methods and behaviors that are shared by different types of collections in Java.
- 136 . What are the important methods that are declared in the collection interface? \
    The `Collection` interface in Java defines a set of common methods that are shared by all classes that implement the
    interface. Some of the important methods declared in the `Collection` interface include:

    - **add(E e)**: Adds the specified element to the collection.
    - **addAll(Collection<? extends E> c)**: Adds all elements from the specified collection to the collection.
    - **clear()**: Removes all elements from the collection.
    - **contains(Object o)**: Returns `true` if the collection contains the specified element.
    - **containsAll(Collection<?> c)**: Returns `true` if the collection contains all elements from the specified
      collection.
    - **isEmpty()**: Returns `true` if the collection is empty.
    - **iterator()**: Returns an iterator over the elements in the collection.
    - **remove(Object o)**: Removes the specified element from the collection.
    - **removeAll(Collection<?> c)**: Removes all elements from the collection that are also present in the specified
      collection.
    - **retainAll(Collection<?> c)**: Retains only the elements in the collection that are also present in the specified
      collection.
    - **size()**: Returns the number of elements in the collection.
    - **toArray()**: Returns an array containing all elements in the collection.

    These methods provide basic functionality for working with collections in Java and are implemented by classes that
    implement the `Collection` interface.
- 137 . Can you explain briefly about the List interface? \
    The `List` interface in Java extends the `Collection` interface and represents an ordered collection of elements
    that allows duplicates. Lists maintain the insertion order of elements and provide methods for accessing, adding,
    removing, and updating elements at specific positions. Some of the key features of the `List` interface include:

    - **Ordered Collection**: Lists maintain the order in which elements are added and allow duplicate elements.
    - **Indexed Access**: Elements in a list can be accessed using an index, starting from zero.
    - **Positional Operations**: Lists provide methods for adding, removing, and updating elements at specific positions.
    - **Iterating Over Elements**: Lists can be iterated over using an iterator or enhanced for loop.
    - **Sublist Operations**: Lists support operations for creating sublists of elements based on specific ranges.
    - **Sorting**: Lists can be sorted using the `Collections.sort` method.

    The `List` interface is implemented by classes like `ArrayList`, `LinkedList`, and `Vector` in the Java Collections
    Framework. It provides a flexible and efficient way to work with ordered collections of elements.
- 138 . Explain about ArrayList with an example? \
    The `ArrayList` class in Java is a resizable array implementation of the `List` interface. It provides dynamic
    resizing, fast random access, and efficient insertion and deletion of elements. `ArrayList` is part of the Java
    Collections Framework and is commonly used to store and manipulate collections of objects.

    Here is an example of using `ArrayList`:

    ```java
    import java.util.ArrayList;

    public class Main {
        public static void main(String[] args) {
            // Create an ArrayList of integers
            ArrayList<Integer> numbers = new ArrayList<>();

            // Add elements to the ArrayList
            numbers.add(1);
            numbers.add(2);
            numbers.add(3);

            // Access elements by index
            System.out.println("Element at index 1: " + numbers.get(1));

            // Remove an element
            numbers.remove(1);

            // Iterate over the elements
            for (Integer number : numbers) {
                System.out.println(number);
            }
        }
    }
    ```

    In this example, an `ArrayList` of integers is created, and elements are added, accessed, and removed from the list.
    The `ArrayList` class provides a flexible and efficient way to work with collections of objects in Java.
- 139 . Can an ArrayList have duplicate elements? \
    Yes, an `ArrayList` in Java can have duplicate elements. Unlike a `Set`, which does not allow duplicates, an
    `ArrayList` allows elements to be added multiple times. This means that an `ArrayList` can contain duplicate elements
    at different positions in the list. The order of elements in an `ArrayList` is maintained, so duplicate elements will
    appear in the list in the order in which they were added.
- 140 . How do you iterate around an ArrayList using iterator? \
    To iterate over an `ArrayList` using an iterator in Java, you can use the `iterator` method provided by the
    `ArrayList` class. The `iterator` method returns an `Iterator` object that can be used to traverse the elements in the
    list. Here is an example:

    ```java
    import java.util.ArrayList;
    import java.util.Iterator;

    public class Main {
        public static void main(String[] args) {
            // Create an ArrayList of strings
            ArrayList<String> names = new ArrayList<>();
            names.add("Alice");
            names.add("Bob");
            names.add("Charlie");

            // Get an iterator for the ArrayList
            Iterator<String> iterator = names.iterator();

            // Iterate over the elements using the iterator
            while (iterator.hasNext()) {
                String name = iterator.next();
                System.out.println(name);
            }
        }
    }
    ```

    In this example, an `ArrayList` of strings is created, and an iterator is obtained using the `iterator` method. The
    iterator is then used to iterate over the elements in the list and print them to the console.
- 141 . How do you sort an ArrayList? \
    To sort an `ArrayList` in Java, you can use the `Collections.sort` method provided by the `java.util.Collections`
    class. The `Collections.sort` method sorts the elements in the list in ascending order based on their natural order or
    a custom comparator. Here is an example:

    ```java
    import java.util.ArrayList;
    import java.util.Collections;

    public class Main {
        public static void main(String[] args) {
            // Create an ArrayList of integers
            ArrayList<Integer> numbers = new ArrayList<>();
            numbers.add(3);
            numbers.add(1);
            numbers.add(2);

            // Sort the ArrayList
            Collections.sort(numbers);

            // Print the sorted elements
            for (Integer number : numbers) {
                System.out.println(number);
            }
        }
    }
    ```

    In this example, an `ArrayList` of integers is created, and the `Collections.sort` method is used to sort the elements
    in the list. The sorted elements are then printed to the console in ascending order.
- 142 . How do you sort elements in an ArrayList using comparable interface? \
    To sort elements in an `ArrayList` using the `Comparable` interface in Java, you need to implement the `Comparable`
    interface in the class of the elements you want to sort. The `Comparable` interface defines a `compareTo` method that
    compares the current object with another object and returns a negative, zero, or positive value based on their
    ordering. Here is an example:

    ```java
    import java.util.ArrayList;
    import java.util.Collections;

    public class Person implements Comparable<Person> {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        @Override
        public int compareTo(Person other) {
            return this.age - other.age;
        }

        public static void main(String[] args) {
            // Create an ArrayList of Person objects
            ArrayList<Person> people = new ArrayList<>();
            people.add(new Person("Alice", 25));
            people.add(new Person("Bob", 30));
            people.add(new Person("Charlie", 20));

            // Sort the ArrayList using the Comparable interface
            Collections.sort(people);

            // Print the sorted elements
            for (Person person : people) {
                System.out.println(person.name + " - " + person.age);
            }
        }
    }
    ```

    In this example, the `Person` class implements the `Comparable` interface and defines a `compareTo` method that
    compares `Person` objects based on their age. The `Collections.sort` method is then used to sort the `ArrayList` of
    `Person` objects based on their age.
- 143 . How do you sort elements in an ArrayList using comparator interface? \
    To sort elements in an `ArrayList` using the `Comparator` interface in Java, you need to create a custom comparator
    class that implements the `Comparator` interface. The `Comparator` interface defines a `compare` method that compares
    two objects and returns a negative, zero, or positive value based on their ordering. Here is an example:

    ```java
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.Comparator;

    public class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public static void main(String[] args) {
            // Create an ArrayList of Person objects
            ArrayList<Person> people = new ArrayList<>();
            people.add(new Person("Alice", 25));
            people.add(new Person("Bob", 30));
            people.add(new Person("Charlie", 20));

            // Create a custom comparator to sort by name
            Comparator<Person> nameComparator = Comparator.comparing(Person::getName);

            // Sort the ArrayList using the Comparator interface
            Collections.sort(people, nameComparator);

            // Print the sorted elements
            for (Person person : people) {
                System.out.println(person.name + " - " + person.age);
            }
        }

        public String getName() {
            return name;
        }
    }
    ```

    In this example, a custom comparator class is created using the `Comparator.comparing` method to sort `Person` objects
    based on their name. The `Collections.sort` method is then used to sort the `ArrayList` of `Person` objects using the
    custom comparator.
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
