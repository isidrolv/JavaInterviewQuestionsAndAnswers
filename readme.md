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

## 200+ Interview Questions

### Java Platform

- **1 . Why is Java so popular?**
    - Java is popular for several reasons:

        -
            1. **Platform Independence**: Java programs can run on any device that has the Java Virtual Machine (JVM),
               making it
               highly portable.
        -
            2. **Object-Oriented**: Java's object-oriented nature allows for modular programs and reusable code.
        -
            3. **Robust and Secure**: Java has strong memory management, exception handling, and security features.
        -
            4. **Rich API**: Java provides a vast standard library that simplifies many programming tasks.
        -
            5. **Community Support**: Java has a large and active community, providing extensive resources and support.
        -
            6. **Performance**: Java's performance has improved significantly with Just-In-Time (JIT) compilers and
               other
               optimizations.
        -
            7. **Enterprise Use**: Java is widely used in enterprise environments, particularly for server-side
               applications.
- **2 . What is platform independence?**
  Platform independence refers to the ability of a programming language or software to run on various types of computer
  systems without modification. In the context of Java, platform independence is achieved through the use of the Java
  Virtual Machine (JVM). Java programs are compiled into bytecode, which can be executed on any device that has a JVM,
  regardless of the underlying hardware and operating system. This allows Java applications to be written once and run
  anywhere.
- **3 . What is bytecode?**
  Bytecode is an intermediate representation of a Java program. When a Java program is compiled, it is converted into
  bytecode, which is a set of instructions that can be executed by the Java Virtual Machine (JVM). Bytecode is
  platform-independent, meaning it can run on any device that has a JVM, regardless of the underlying hardware and
  operating system. This allows Java programs to be written once and run anywhere.
- **4 . Compare JDK vs JVM vs JRE**
    - **JDK (Java Development Kit)**: A software development kit used to develop Java applications. It includes the JRE,
      an interpreter/loader (Java), a compiler (javac), an archiver (jar), a documentation generator (Javadoc), and
      other tools needed for Java development.
    - **JVM (Java Virtual Machine)**: An abstract machine that enables your computer to run a Java program. When you run
      a Java program, the JVM is responsible for converting the bytecode into machine-specific code. It provides
      platform independence.
    - **JRE (Java Runtime Environment)**: A package of software that provides the class libraries, JVM, and other
      components to run applications written in Java. It does not include development tools like compilers or debuggers.
- **5 . What are the important differences between C++ and Java?**
    - **Memory Management**: C++ uses manual memory management with pointers, while Java uses automatic garbage
      collection.
    - **Platform Independence**: Java is platform-independent due to the JVM, whereas C++ is platform-dependent and
      needs to be compiled for each platform.
    - **Multiple Inheritance**: C++ supports multiple inheritance, while Java does not. Java uses interfaces to achieve
      similar functionality.
    - **Pointers**: C++ supports pointe rs, allowing direct memory access. Java does not support pointers explicitly,
      enhancing security and simplicity.
    - **Standard Library**: Java has a rich standard library with built-in support for networking, threading, and GUI
      development. C++ has a standard library but with less built-in support for these features.
    - **Compilation and Execution**: C++ is compiled directly to machine code, while Java is compiled to bytecode and
      executed by the JVM.
    - **Operator Overloading**: C++ supports operator overloading, while Java does not.
    - **Templates vs. Generics**: C++ uses templates for generic programming, while Java uses generics.

### Wrapper Classes

- **7 . What are Wrapper classes?**
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
- **8 . Why do we need Wrapper classes in Java?**
  Wrapper classes in Java are needed for the following reasons:
    -
        1. **Object-Oriented Programming**: Wrapper classes allow primitive data types to be treated as objects,
           enabling
           them to be used in object-oriented programming contexts.
    -
        2. **Collections**: Collections in Java, such as `ArrayList`, can only store objects. Wrapper classes allow
           primitive types to be stored in collections.
    -
        3. **Utility Methods**: Wrapper classes provide utility methods for converting between types and performing
           operations on the values.
    -
        4. **Default Values**: Wrapper classes can be used to represent default values (e.g., `null` for an `Integer`),
           which is not possible with primitive types.
    -
        5. **Type Safety**: Wrapper classes enable type safety in generic programming, ensuring that only the correct
           type
           of objects are used.
- **9 . What are the different ways of creating Wrapper class instances?**
  There are two main ways to create instances of Wrapper classes in Java:
    - a). **Using Constructors**:
      Each wrapper class has a constructor that takes a primitive type or a String as an argument.
       ```java
       Integer intObj1 = 10;
       Integer intObj2 = Integer.valueOf("10");
       ```
    - b). **Using Static Factory Methods**:
      The wrapper classes provide static factory methods like `valueOf` to create instances.
       ```java
       Integer intObj1 = 10;
       Integer intObj2 = Integer.valueOf("10");
       ```
- **10 . What are differences in the two ways of creating Wrapper classes?** \
  The two ways of creating Wrapper class instances in Java are using constructors and using static factory methods. Here
  are the differences:

    -
        1. **Using Constructors**:
           Each wrapper class has a constructor that takes a primitive type or a `String` as an argument. \
           Example:
            ```java
            Integer intObj1 = new Integer(10);
            Integer intObj2 = new Integer("10");
            ```
    -
        2. **Using Static Factory Methods**:
           Wrapper classes provide static factory methods like `valueOf` to create instances.\
           Example:
            ```java
            Integer intObj1 = Integer.valueOf(10);
            Integer intObj2 = Integer.valueOf("10");
            ```
  **Differences**:
    - **Performance**: Static factory methods are generally preferred over constructors because they can cache
      frequently requested values, improving performance.
    - **Readability**: Using `valueOf` is often more readable and expressive.
    - **Deprecation**: Some constructors in wrapper classes are deprecated in favor of static factory methods.
- **11 . What is auto boxing?**
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
- **12 . What are the advantages of auto boxing?**
  Autoboxing in Java provides several advantages:
    -
        1. **Simplicity**: Autoboxing simplifies the process of working with primitive types in contexts that require
           objects,
           such as collections.
    -
        2. **Readability**: Autoboxing makes the code more readable and expressive by automatically converting between
           primitive types and their corresponding object wrapper classes.
    -
        3. **Convenience**: Autoboxing eliminates the need for manual conversion between primitive types and objects,
           reducing
           boilerplate code.
    -
        4. **Compatibility**: Autoboxing allows code written with primitive types to be used in contexts that require
           objects, without the need for explicit conversion.
- **13 . What is casting?**
  Casting in Java is the process of converting a value of one data type to another. There are two types of casting:
    -
        1. **Implicit Casting**: When a smaller data type is converted to a larger data type, Java automatically
           performs
           the
           conversion. For example, converting an `int` to a `double`.
    -
        2. **Explicit Casting**: When a larger data type is converted to a smaller data type, or when converting between
           incompatible types, explicit casting is required. For example, converting a `double` to an `int`.

  Example:
  ```java
  int intValue = 10;
  double doubleValue = intValue; // Implicit casting
  double doubleValue = 10.5;
  int intValue = (int) doubleValue; // Explicit casting
  ```
- **14 . What is implicit casting?**
  Implicit casting in Java is the automatic conversion of a smaller data type to a larger data type. Java performs
  implicit casting when the target data type can accommodate the source data type without loss of precision. For
  example, converting an `int` to a `double` or a `float` to a `double`.

  Example:
  ```java
  int intValue = 10;
  double doubleValue = intValue; // Implicit casting
  ```
- **15 . What is explicit casting?**
  Explicit casting in Java is the manual conversion of a larger data type to a smaller data type, or when converting
  between incompatible types. Java requires explicit casting when the target data type may lose precision or range
  when accommodating the source data type. For example, converting a `double` to an `int`.

  Example:
  ```java
  double doubleValue = 10.5;
  int intValue = (int) doubleValue; // Explicit casting
  ```

### Strings

- **16 . Are all String**’s immutable?\
  No, not all `String` objects are immutable. In Java, `String` objects are immutable, meaning once a `String`
  object is created, its value cannot be changed. However, there are other classes like `StringBuilder`
  and `StringBuffer` that provide mutable alternatives to `String`. These classes allow you to modify the contents
  of the string without creating new objects.
- **17 . Where are String values stored in memory?**\
  In Java, `String` values are stored in a special memory area called the **String Pool**. The String Pool is part of
  the Java heap memory and is used to store unique `String` literals. When a `String` literal is created, the JVM checks
  the String Pool to see if an identical `String` already exists. If it does, the reference to the existing `String` is
  returned. If not, the new `String` is added to the pool. This process helps in saving memory and improving performance
  by reusing immutable `String` objects.
- **18 . Why should you be careful about String concatenation(+) operator in loops?**\
  String concatenation using the `+` operator in loops can be inefficient due to the immutability of `String` objects.
  Each time a `String` is concatenated using the `+` operator, a new `String` object is created, resulting in
  unnecessary memory allocation and garbage collection. This can lead to performance issues, especially in loops where
  multiple concatenations are performed. To improve performance, it is recommended to use `StringBuilder`
  or `StringBuffer`
  for string concatenation in loops, as these classes provide mutable alternatives to `String` and are more efficient
  for building strings.
- **19 . How do you solve above problem?**
  To solve the problem of inefficient string concatenation using the `+` operator in loops, you should
  use `StringBuilder` or `StringBuffer`. These classes provide mutable alternatives to `String` and are more efficient
  for building strings.
  Here is an example of how to use `StringBuilder` for string concatenation in a loop:

  Example using `StringBuilder`:
  ```java
  public class Main {
      public static void main(String[] args) {
          StringBuilder sb = new StringBuilder();
          for (int i = 0; i < 10; i++) {
              sb.append(i);
          }
          String result = sb.toString();
          System.out.println(result);
      }
  }
  ```
  In this example, a `StringBuilder` is used to concatenate integers in a loop, and the final result is obtained by
  calling the `toString` method. This approach is more efficient than using the `+` operator with `String` objects in a
  loop.
- **20 . What are the differences between `String` and `StringBuffer`?**
    - **Mutability**: `String` objects are immutable, meaning their values cannot be changed once
      created. `StringBuffer` objects are mutable, allowing their values to be modified.
    - **Thread Safety**: `StringBuffer` is synchronized, making it thread-safe. `String` is not synchronized.
    - **Performance**: Due to immutability, `String` operations can be slower as they create new objects. `StringBuffer`
      is faster for concatenation and modification operations.
    - **Usage**: Use `String` when the value does not change. Use `StringBuffer` when the value changes frequently and
      thread safety is required.
- **22 . Can you give examples of different utility methods in String class?**
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

- **23 . What is a class?**
  A class in Java is a blueprint for creating objects. It defines a set of properties (fields) and methods that the
  created objects will have. A class encapsulates data for the object and methods to manipulate that data. It serves as
  a template from which individual objects are instantiated.
- **25 . What is state of an object?**
  The state of an object in Java refers to the data or values stored in its fields (instance variables) at any given
  time. The state represents the current condition of the object, which can change over time as the values of its fields
  are modified through methods or operations.
- **26 . What is behavior of an object?**
  The behavior of an object in Java refers to the actions or operations that the object can perform. These behaviors are
  defined by the methods in the object's class. The methods manipulate the object's state and can interact with other
  objects. The behavior of an object is what it can do, such as calculating a value, modifying its state, or interacting
  with other objects.
- **28 . Explain about toString method ?**
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

- **29 . What is the use of equals method in Java?**
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

- **30 . What are the important things to consider when implementing `equals` method?**
    - **Reflexive**: `x.equals(x)` should return `true`.
    - **Symmetric**: If `x.equals(y)` returns `true`, then `y.equals(x)` should also return `true`.
    - **Transitive**: If `x.equals(y)` and `y.equals(z)` both return `true`, then `x.equals(z)` should also
      return `true`.
    - **Consistent**: Multiple invocations of `x.equals(y)` should consistently return the same result.
    - **Non-nullity**: `x.equals(null)` should return `false`.
    - **Type Check**: Ensure the object being compared is of the correct type.
    - **Field Comparison**: Compare significant fields that determine equality.
- **31 . What is the Hashcode method used for in Java?**
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
- **32 . Explain inheritance with examples**.
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

- **33 . What is method overloading?**
  Method overloading in Java is a feature that allows a class to have more than one method with the same name, provided
  their parameter lists are different. This means that the methods must differ in the type, number, or order of their
  parameters. Method overloading is a compile-time polymorphism technique, enabling different methods to perform similar
  operations with varying inputs. It enhances code readability and reusability by allowing the same method name to be
  used for different tasks, based on the arguments passed. Overloaded methods can have different return types, but this
  alone is not enough for overloading; the parameter list must be different.
- **34 . What is method overriding?**
  Method overriding in Java is a feature that allows a subclass to provide a specific implementation of a method that is
  already provided by its superclass. When a method in a subclass has the same name, return type, and parameters as a
  method in its superclass, it is said to override the superclass method. Method overriding is a runtime polymorphism
  technique, enabling a subclass to provide its own implementation of a method inherited from a superclass. This allows
  for more specific behavior to be defined in the subclass, while still maintaining a common interface with the
  superclass. Method overriding is used to achieve dynamic polymorphism in Java.
- **35 . Can super class reference variable can hold an object of sub class?**
  Yes, a superclass reference variable can hold an object of a subclass in Java. This is known as polymorphism and is a
  key feature of object-oriented programming. When a superclass reference variable holds an object of a subclass, it can
  only access the methods and fields that are defined in the superclass. If the subclass has additional methods or
  fields
  that are not present in the superclass, they cannot be accessed using the superclass reference variable. However, if
  the superclass reference variable is cast to the subclass type, it can access the subclass-specific methods and
  fields.
  Here is an example:

    ```java
    class Animal {
        void eat() {
            System.out.println("Animal is eating");
        }
    }

    class Dog extends Animal {
        void bark() {
            System.out.println("Dog is barking");
        }
    }

    public class Main {
        public static void main(String[] args) {
            Animal animal = new Dog(); // Superclass reference holding subclass object
            animal.eat(); // Accessing superclass method
            // animal.bark(); // Compilation error: Cannot access subclass-specific method
            Dog dog = (Dog) animal; // Casting to subclass type
            dog.bark(); // Accessing subclass-specific method
        }
    }
    ```

  In this example:
    - The `Animal` class has an `eat` method.
    - The `Dog` class extends `Animal` and has a `bark` method.
    - In the `Main` class, an `Animal` reference variable holds a `Dog` object.
    - The `eat` method can be accessed using the superclass reference variable.
    - The `bark` method cannot be accessed using the superclass reference variable, but it can be accessed after casting
      to the subclass type.
- **36 . Is multiple inheritance allowed in Java?**
  Java does not support multiple inheritance of classes, meaning a class cannot extend more than one class at a time.
  This is to avoid the "diamond problem," where conflicts can arise if two superclasses have methods with the same
  signature. However, Java does support multiple inheritance of interfaces, allowing a class to implement multiple
  interfaces. This provides a form of multiple inheritance by allowing a class to inherit the abstract methods of
  multiple interfaces. By using interfaces, Java achieves the benefits of multiple inheritance without the issues
  associated with multiple inheritance of classes.

  Here is an example of multiple inheritance of interfaces:

    ```java
    interface InterfaceA {
        void methodA();
    }

    interface InterfaceB {
        void methodB();
    }

    class MyClass implements InterfaceA, InterfaceB {
        public void methodA() {
            System.out.println("Method A");
        }

        public void methodB() {
            System.out.println("Method B");
        }
    }

    public class Main {
        public static void main(String[] args) {
            MyClass obj = new MyClass();
            obj.methodA();
            obj.methodB();
        }
    }
    ```

  In this example:
    - `InterfaceA` and `InterfaceB` are two interfaces with abstract methods.
    - The `MyClass` class implements both interfaces, providing concrete implementations for the abstract methods.
    - The `Main` class creates an instance of `MyClass` and calls the methods defined in the interfaces.
- **37 . What is an interface?**
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

- **38 . How do you define an interface?**

  An interface in Java is defined using the `interface` keyword. It can contain abstract methods, default methods,
  static methods, and constants. Here is an example:

  ```java
  public interface Animal {
      void eat();
      void sleep();
  }
  ```
- **39 . How do you implement an interface?**
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

- **40 . Can you explain a few tricky things about interfaces?**
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
- **41 . Can you extend an interface?**
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

- **42 . Can a class extend multiple interfaces?**
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
- **43 . What is an abstract class?**
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
- **44 . When do you use an abstract class?**
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
- **45 . How do you define an abstract method?**
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
- **46 . Compare abstract class vs interface?**
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
- **47 . What is a constructor?**
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
- **48 . What is a default constructor?**
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
- **49 . Will this code compile?**
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
- **50 . How do you call a super class constructor from a constructor?**
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
- **51 . Will this code compile?**

```java
  public class Example {
    public static void main(String[] args) {
        System.out.println("Hello, World!") // Missing semicolon here
    }

}
  ```

    No, this code will not compile due to a missing semicolon at the end of the `System.out.println` statement. In Java,

- **52 . What is the use of this**() keyword in Java?\
  The `this` keyword in Java is a reference to the current object within a method or constructor. It can be used to
  access instance variables, call other constructors, or pass the current object as a parameter to other methods. The
  use of `this` is optional, but it can help clarify code and avoid naming conflicts between instance variables and
  method parameters.

- **53 . Can a constructor be called directly from a method?**\
  No, a constructor cannot be called directly from a method. Constructors are special methods that are called only when
  an object is created. However, you can call another constructor from a constructor using `this()` or `super()`. If you
  need to initialize an object within a method, you should create a new instance of the class using the `new` keyword.

- **54 . Is a super class constructor called even when there is no explicit call from a sub class constructor?**\
  Yes, a superclass constructor is always called, even if there is no explicit call from a subclass constructor. If a
  subclass constructor does not explicitly call a superclass constructor using `super()`, the Java compiler
  automatically inserts a call to the no-argument constructor of the superclass. If the superclass does not have a
  no-argument constructor, a compilation error will occur. This ensures that the superclass part of the object is.

### Advanced object oriented concepts

- **55 . What is polymorphism?** \
  Polymorphism in Java is the ability of an object to take on many forms. It allows one interface to be used for a
  general class of actions. The specific action is determined by the exact nature of the situation. Polymorphism is
  mainly achieved through method overriding and method overloading.

    - **Method Overriding**: When a subclass provides a specific implementation of a method that is already defined in
      its superclass.
    - **Method Overloading**: When multiple methods have the same name but different parameters within the same class.

  Polymorphism allows for flexibility and the ability to define methods that can be used interchangeably, making the
  code more modular and easier to maintain.
- **56 . What is the use of instanceof operator in Java?**\
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
  casting it to `Dog` and calling the `bark` method. This helps prevent `ClassCastException` errors by ensuring that the
  object is of the correct type before performing type-specific operations.
- **57 . What is coupling?**\
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
- **58 . What is cohesion?**\
  Cohesion in software engineering refers to the degree to which the elements inside a module belong together. It
  measures how closely related the responsibilities of a single module are. High cohesion means that the elements within
  a module are strongly related and work together to achieve a common goal. Low cohesion, on the other hand, means that
  the elements within a module are loosely related and may not work well together.

  Cohesion in Java refers to the degree to which the methods in a class are related and work together to achieve a
  common purpose. High cohesion is desirable as it promotes code that is easier to understand, maintain, and test. Low
  cohesion can lead to code that is difficult to follow, modify, and debug.
- **59 . What is encapsulation?**\
  Encapsulation in Java is a fundamental object-oriented programming concept that involves bundling the data (fields)
  and the methods (functions) that operate on the data into a single unit, called a class. It restricts direct access to
  some of the object's components, which can help prevent the accidental modification of data. Encapsulation is achieved
  by:

    -
        1. Declaring the fields of a class as private.
    -
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
- **60 . What is an inner class?**\
  An inner class in Java is a class that is defined within another class. Inner classes can access the members (
  including private members) of the outer class. There are four types of inner classes in Java:

    -
        1. **Member Inner Class**: A class defined within another class.
    -
        2. **Static Nested Class**: A static class defined within another class.
    -
        3. **Local Inner Class**: A class defined within a method.
    -
        4. **Anonymous Inner Class**: A class without a name, defined and instantiated in a single statement.

  Inner classes are useful for grouping related classes together, improving encapsulation, and reducing code complexity.
-

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

- **61 . What is a static inner class?**\  
  A static inner class in Java is a nested class that is defined as a static member of the outer class. It does not have
  access to the instance variables and methods of the outer class, but it can access static members of the outer class.
  Static inner classes are useful for grouping related classes together and improving code organization.

  Here is an example of a static inner class:

    ```java
    public class OuterClass {
        private static int outerStaticField = 10;
    
        static class StaticInnerClass {
            void display() {
                System.out.println("Outer static field value: " + outerStaticField);
            }
        }
    
        public static void main(String[] args) {
            OuterClass.StaticInner inner = new OuterClass.StaticInner();
            inner.display();
        }
    }
    ```
  In this example, `StaticInnerClass` is a static inner class within `OuterClass` and can access the `outerStaticField`
  of `OuterClass`.

- **62 . Can you create an inner class inside a method?** \
  Yes, you can create an inner class inside a method in Java. This type of inner class is called a local inner class.
  Local inner classes are defined within a method and can only be accessed within that method. They have access to the
  variables and parameters of the enclosing method, but they must be declared before they are used.

  Here is an example of a local inner class:

    ```java
    public class OuterClass {
        private int outerField = 10;
    
        public void display() {
            class LocalInnerClass {
                void display() {
                    System.out.println("Outer field value: " + outerField);
                }
            }
    
            LocalInnerClass inner = new LocalInnerClass();
            inner.display();
        }
    
        public static void main(String[] args) {
            OuterClass outer = new OuterClass();
            outer.display();
        }
    }
    ```

  In this example, `LocalInnerClass` is a local inner class defined within the `display` method of `OuterClass`. It can
  access the `outerField` of `OuterClass` and is instantiated and used within the `display` method.
- **63 . What is an anonymous class?** \
  An anonymous class in Java is a class without a name that is defined and instantiated in a single statement. It is
  typically used for one-time use cases where a class needs to be defined and instantiated without creating a separate
  class file. Anonymous classes are often used for event handling, callbacks, and other situations where a class is
  needed for a specific purpose.

  Here is an example of an anonymous class:

    ```java
    public class Main {
        public static void main(String[] args) {
            Runnable runnable = new Runnable() {
                @Override
                public void run() {
                    System.out.println("Hello, World!");
                }
            };
    
            new Thread(runnable).start();
        }
    }
    ```
  here is the same example using a lambda expression:

    ```java
    public class Main {
        public static void main(String[] args) {
            Runnable runnable = () -> System.out.println("Hello, World!");
            new Thread(runnable).start();
        }
    }
    ```

  In this example, an anonymous class is defined and instantiated as an implementation of the `Runnable` interface. It
  is
  used to create a new `Thread` that prints "Hello, World!" when started.

### Modifiers

- **64 . What is default class modifier?** \
  The default class modifier in Java is package-private, which means that the class is only accessible within the same
  package. If no access modifier is specified for a class, it is considered to have default access. This means that the
  class can be accessed by other classes within the same package but not by classes in different packages.

  Here is an example of a class with default access:

    ```java
    class MyClass {
        // class implementation
    }
    ```

  In this example, `MyClass` has default access, so it can be accessed by other classes within the same package but not
  by classes in different packages. If you want a class to be accessible from other packages, you should use the
  `public` access modifier. If you want to restrict access to the class to only subclasses, you can use the `protected`
  access modifier. If you want to restrict access to only the class itself, you can use the `private` access modifier.
- **65 . What is private access modifier?** \
  The `private` access modifier in Java is the most restrictive access level. It is used to restrict access to members
  (fields, methods, constructors) of a class to only within the same class. This means that private members cannot be
  accessed by other classes, even subclasses. Private members are only accessible within the class in which they are
  declared.

  Here is an example of a private field:

    ```java
    public class MyClass {
        private int privateField;
    
        public void setPrivateField(int value) {
            privateField = value;
        }
    
        public int getPrivateField() {
            return privateField;
        }
    }
    ```

  In this example, `privateField` is a private field that can only be accessed and modified within the `MyClass` class.
  Any attempt to access or modify `privateField` from outside the class will result in a compilation error.
- **66 . What is default or package access modifier?** \
  The default or package access modifier in Java is the absence of an access modifier. It is also known as
  package-private
  access. This means that the class, method, or field with default access can only be accessed by classes within the
  same
  package. It is more restrictive than the `protected` access modifier but less restrictive than the `private` and
  `public` access modifiers.

  Here is an example of a class with default access:

    ```java
    class MyClass {
        // class implementation
    }
    ```

  In this example, `MyClass` has default access, so it can be accessed by other classes within the same package but not
  by classes in different packages. If you want a class to be accessible from other packages, you should use the
  `public` access modifier. If you want to restrict access to the class to only subclasses, you can use the `protected`
  access modifier. If you want to restrict access to only the class itself, you can use the `private` access modifier.
- **67 . What is protected access modifier?** \
  The `protected` access modifier in Java is used to restrict access to members (fields, methods, constructors) of a
  class to only within the same package or subclasses of the class. This means that protected members can be accessed by
  classes within the same package and by subclasses, even if they are in different packages. Protected members are not
  accessible by classes that are not in the same package or are not subclasses of the class.

  Here is an example of a protected field:

    ```java
    public class SuperClass {
        protected int protectedField;
    }
    
    public class SubClass extends SuperClass {
        public void setProtectedField(int value) {
            protectedField = value;
        }
    
        public int getProtectedField() {
            return protectedField;
        }
    }
    ```

  In this example, `protectedField` is a protected field in the `SuperClass` class. It can be accessed and modified by
  the `SubClass` class, which is a subclass of `SuperClass`. Any attempt to access or modify `protectedField` from a
  class that is not in the same package or is not a subclass of `SuperClass` will result in a compilation error.
- **68 . What is public access modifier?** \
  The `public` access modifier in Java is the least restrictive access level. It allows a class, method, or field to be
  accessed by any other class in the same project or in other projects. Public members are accessible from any other
  class, regardless of the package or inheritance relationship. This makes them useful for creating APIs and libraries
  that can be used by other developers.
- **69 . What access types of variables can be accessed from a class in same package?** \
  In Java, a class in the same package can access the following types of variables:
    - **Public Variables**: Public variables can be accessed by any class in the same package or in other packages.
    - **Protected Variables**: Protected variables can be accessed by any class in the same package or by subclasses in
      other packages.
    - **Default (Package-Private) Variables**: Default variables can be accessed by any class in the same package.
    - **Private Variables**: Private variables cannot be accessed by any other class, even in the same package.
- **70 . What access types of variables can be accessed from a class in different package?** \
  In Java, a class in a different package can access the following types of variables:
    - **Public Variables**: Public variables can be accessed by any class in any package.
    - **Protected Variables**: Protected variables can be accessed by subclasses in any package, but not by
      non-subclasses
      in different packages.
    - **Default (Package-Private) Variables**: Default variables cannot be accessed by classes in different packages.
    - **Private Variables**: Private variables cannot be accessed by any other class, even in a different package.
- **71 . What access types of variables can be accessed from a sub class in same package?** \
  In Java, a subclass in the same package can access the following types of variables:
    - **Public Variables**: Public variables can be accessed by any class in the same package or in other packages.
    - **Protected Variables**: Protected variables can be accessed by any class in the same package or by subclasses in
      other packages.
    - **Default (Package-Private) Variables**: Default variables can be accessed by any class in the same package.
    - **Private Variables**: Private variables cannot be accessed by any other class, even in the same package.
- **72 . What access types of variables can be accessed from a sub class in different package?** \
  In Java, a subclass in a different package can access the following types of variables:
    - **Public Variables**: Public variables can be accessed by any class in any package.
    - **Protected Variables**: Protected variables can be accessed by subclasses in any package, but not by
      non-subclasses
      in different packages.
    - **Default (Package-Private) Variables**: \Default variables cannot be accessed by classes in different packages.
    - **Private Variables**: Private variables cannot be accessed by any other class, even in a different package.
- **73 . What is the use of a final modifier on a class?** \
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
- **74 . What is the use of a final modifier on a method?**
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
  Any attempt to override the `display` method in `SubClass` will result in a compilation error. This is useful for
  ensuring that certain methods retain their behavior across subclasses.
- **75 . What is a final variable?** \
  A final variable in Java is a variable that cannot be reassigned once it has been initialized. The `final` keyword is
  used to declare a variable as final. This means that the value of the variable remains constant throughout the
  program. Final variables are often used for constants or for ensuring that a variable's value does not change.

  Here is an example:

    ```java
    public class Example {
        public static final int MAX_VALUE = 100;
    
        public static void main(String[] args) {
            // MAX_VALUE cannot be reassigned
            // MAX_VALUE = 200; // This would cause a compilation error
            System.out.println(MAX_VALUE);
        }
    }
    ```

  In this example, `MAX_VALUE` is a final variable that cannot be reassigned after it is initialized. Any attempt to
  reassign `MAX_VALUE` will result in a compilation error. This ensures that the value of `MAX_VALUE` remains constant
  in the program.
- **76 . What is a final argument?**\
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
- **77 . What happens when a variable is marked as volatile?**\
  When a variable is marked as `volatile` in Java, it ensures that the value of the variable is always read from and
  written to the main memory, rather than being cached in a thread's local memory. This guarantees visibility of changes
  to the variable across all threads. The `volatile` keyword is used to prevent memory consistency errors in concurrent
  programming.
- **78 . What is a static variable?**\
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

- **79 . Why should you always use blocks around if statement?** \
  It is a good practice to always use blocks around `if` statements in Java to improve code readability and avoid
  potential bugs. When an `if` statement is not enclosed in a block, only the next statement is considered part of the
  `if` block. This can lead to confusion and errors if additional statements are added later. By using blocks around
  `if`
  statements, you make it clear which statements are part of the conditional block and reduce the risk of errors.
- **80 . Guess the output**\
  Here is an example to guess the output:
    ```java
    public class GuessOutput {
        public static void main(String[] args) {
            int x = 5;
            int y = 10;
            int z = x++ + ++y;
            System.out.println("x = " + x);
            System.out.println("y = " + y);
            System.out.println("z = " + z);
        }
    }
    ```
  The output of this program will be:
    ```ruby
        x = 6 
        y = 11 
        z = 16 
    ```
- **81 . Guess the output**\
  Here is an example to guess the output:
    ```java
    public class GuessOutput {
        public static void main(String[] args) {
            int a = 3;
            int b = 7;
            int c = a-- - --b;
            System.out.println("a = " + a);
            System.out.println("b = " + b);
            System.out.println("c = " + c);
        }
    }
    ```
  The output of this program will be:
    ```ruby
        a = 2
        b = 6
        c = -3
    ```
- **82 . Guess the output of this switch block**\
  Here is an example to guess the output:
    ```java
    public class GuessOutput {
        public static void main(String[] args) {
            int day = 3;
            String dayString;
            switch (day) {
                case 1:
                    dayString = "Monday";
                    break;
                case 2:
                    dayString = "Tuesday";
                    break;
                case 3:
                    dayString = "Wednesday";
                    break;
                case 4:
                    dayString = "Thursday";
                    break;
                case 5:
                    dayString = "Friday";
                    break;
                case 6:
                    dayString = "Saturday";
                    break;
                case 7:
                    dayString = "Sunday";
                    break;
                default:
                    dayString = "Invalid day";
                    break;
            }
            System.out.println(dayString);
        }
    }
    ```
  The output of this program will be:
    ```ruby
        Wednesday
    ```
- **83 . Guess the output of this switch block?** \
  Here is an example to guess the output:
    ```java
    public class GuessOutput {
        public static void main(String[] args) {
            int x = 5;
            switch (x) {
                case 1:
                    System.out.println("One");
                case 2:
                    System.out.println("Two");
                case 3:
                    System.out.println("Three");
                case 4:
                    System.out.println("Four");
                case 5:
                    System.out.println("Five");
                default:
                    System.out.println("Default");
            }
        }
    }
    ```
  The output of this program will be:
    ```ruby
        Five
        Default
    ```
- **84 . Should default be the last case in a switch statement?** \
  No, the `default` case does not have to be the last case in a `switch` statement in Java. The `default` case is
  optional and can be placed anywhere within the `switch` statement. It is typically used as a catch-all case for values
  that do not match any of the other cases. Placing the `default` case at the end of the `switch` statement is a common
  practice to make it easier to identify and handle unexpected values, but it is not required.
  By example:
    ```java
    public class Example {
        public static void main(String[] args) {
            int x = 5;
            switch (x) {
                case 1:
                    System.out.println("One");
                    break;
                case 2:
                    System.out.println("Two");
                    break;
                default:
                    System.out.println("Default");
                    break;
                case 3:
                    System.out.println("Three");
                    break;
            }
        }
    }
    ```
  In this example, the `default` case is placed before the `case 3` statement. This is valid Java syntax, and the
  `default` case will be executed if the value of `x` does not match any of the other cases.
- **85 . Can a switch statement be used around a String** \
  Yes, a `switch` statement can be used with a `String` in Java starting from Java 7. Prior to Java 7, `switch`
  statements only supported `int`, `byte`, `short`, `char`, and `enum` types. With the introduction of the `String`
  `switch` feature in Java 7, you can now use `String` values as case labels in a `switch` statement.

  Here is an example:

    ```java
    public class Example {
        public static void main(String[] args) {
            String day = "Monday";
            switch (day) {
                case "Monday":
                    System.out.println("It's Monday!");
                    break;
                case "Tuesday":
                    System.out.println("It's Tuesday!");
                    break;
                default:
                    System.out.println("It's not Monday or Tuesday.");
                    break;
            }
        }
    }
    ```

  In this example, the `switch` statement uses a `String` value (`day`) as the expression and `String` case labels
  (`"Monday"` and `"Tuesday"`). This feature allows for more expressive and readable code when working with `String`
  values.
- **86 . Guess the output of this for loop** \
  Here is an example to guess the output:
  ```java
  public class GuessOutput {
      public static void main(String[] args) {
          for (int i = 0; i < 5; i++) {
              System.out.println("i = " + i);
          }
      }
  }
  ```
  The output of this program will be:
  ```ruby
      i = 0
      i = 1
      i = 2
      i = 3
      i = 4
  ```
- **87 . What is an enhanced for loop?** \
  An enhanced for loop, also known as a for-each loop, is a simplified way to iterate over elements in an array or a
  collection in Java. It provides a more concise syntax for iterating over elements without the need for explicit
  indexing or bounds checking. The enhanced for loop was introduced in Java 5 and is commonly used for iterating over
  arrays, lists, sets, and other collections.

  Here is an example of an enhanced for loop:

    ```java
    public class Example {
        public static void main(String[] args) {
            int[] numbers = {1, 2, 3, 4, 5};
            for (int number : numbers) {
                System.out.println(number);
            }
        }
    }
    ```

  In this example, the enhanced for loop iterates over the `numbers` array and prints each element to the console.
- **88 . What is the output of the for loop below?** \
  Here is an example to guess the output:
  ```java
  public class GuessOutput {
      public static void main(String[] args) {
          for (int i = 0; i < 5; i++) {
              if (i == 3) {
                  continue;
              }
              System.out.println("i = " + i);
          }
      }
  }
  ```
- **89 . What is the output of the program below?** \
  Here is an example to guess the output:
  ```java
  public class GuessOutput {
      public static void main(String[] args) {
          for (int i = 1; i < 15; i++) {
              if (i == 13) {
                  break;
              }
              System.out.println("i = " + i);
          }
      }
  }
  ```
- **90 . What is the output of the program below?** \
  Here is an example to guess the output:
  ```java
  public class GuessOutput {
      public static void main(String[] args) {
          for (int i = 0; i < 10; i++) {
              if (i == 13) {
                  break;
              }
              System.out.println("i = " + i);
          }
      }
  }
  ```

### Exception handling

- **91 . Why is exception handling important?** \
  Exception handling is important in Java for the following reasons:
    - **Error Handling**: Exception handling allows you to gracefully handle errors and exceptions that occur during
      program execution. This helps prevent the program from crashing and provides a way to recover from unexpected
      situations.
    - **Robustness**: Exception handling makes your code more robust by handling unexpected conditions and preventing
      them from causing the program to fail.
    - **Debugging**: Exception handling provides a way to catch and log errors, making it easier to debug and diagnose
      issues in the code.
    - **Maintainability**: Exception handling improves the maintainability of the code by separating error-handling
      logic
      from the main program logic. This makes the code easier to read, understand, and modify.
    - **Security**: Exception handling can help prevent security vulnerabilities by handling errors and exceptions that
      could be exploited by malicious users.
    - **User Experience**: Exception handling improves the user experience by providing informative error messages and
      handling errors in a user-friendly way.
- **92 . What design pattern is used to implement exception handling features in most languages?** \
  The most common design pattern used to implement exception handling features in most programming languages, including
  Java, is the `try-catch-finally` pattern. This pattern consists of three main components:

    - **Try Block**: The `try` block contains the code that may throw an exception. It is used to enclose the code that
      needs to be monitored for exceptions.
    - **Catch Block**: The `catch` block is used to handle exceptions that are thrown in the `try` block. It specifies
      the type of exception to catch and the code to execute when the exception occurs.
    - **Finally Block**: The `finally` block is used to execute code that should always run, regardless of whether an
      exception occurs. It is typically used to release resources or clean up after the `try` block.

  Here is an example of the `try-catch-finally` pattern in Java:

    ```java
        public class Example {
        
            public static void main(String[] args) {
                try {
                    // Code that may throw an exception
                    File file = new File("\+example.txt");   
                } catch (Exception e) {
                    // Handle the exception
                    e.printStackTrace();
                } finally {
                    // Cleanup code
                    System.out.println("Finally block executed");
                }
            }
        }
    ```

  In this example, the `try` block contains the code that may throw an exception, the `catch` block handles the
  exception, and the `finally` block contains cleanup code that should always run, regardless of whether an exception
  occurs.
- **93 . What is the need for finally block?** \
  The `finally` block in Java is used to execute code that should always run, regardless of whether an exception occurs.
  It is typically used to release resources, close connections, or perform cleanup operations that need to be done
  regardless of the outcome of the `try` block. The `finally` block is guaranteed to run, even if an exception is thrown
  and caught in the `try` block.

  Here is an example:

    ```java
    public class Example {
        public static void main(String[] args) {
            try {
                // Code that may throw an exception
                int result = 10 / 0;
            } catch (ArithmeticException e) {
                // Handle the exception
                e.printStackTrace();
            } finally {
                // Cleanup code
                System.out.println("Finally block executed");
            }
        }
    }
    ```

  In this example, the `finally` block contains cleanup code that should always run, regardless of whether an exception
  occurs in the `try` block. This ensures that resources are released and cleanup operations are performed, even if an
  exception is thrown.
- **94 . In what scenarios is code in finally not executed?** \
  The code in a `finally` block is not executed in the following scenarios:
    - **System.exit()**: If the `System.exit()` method is called in the `try` or `catch` block, the program will
      terminate immediately, and the code in the `finally` block will not be executed.
    - **Infinite Loop**: If the code in the `try` or `catch` block results in an infinite loop or hangs the program, the
      `finally` block will not be executed.
    - **JVM Shutdown**: If the JVM is shut down abruptly, such as by killing the process or a power failure, the code in
      the `finally` block may not be executed.
    - **Thread Interruption**: If the thread executing the `try` or `catch` block is interrupted, the code in the
      `finally` block may not be executed.
    - **StackOverflowError**: If a `StackOverflowError` occurs in the `try` or `catch` block, the code in the `finally`
      block may not be executed.
    - **OutOfMemoryError**: If an `OutOfMemoryError` occurs in the `try` or `catch` block, the code in the `finally`
      block
      may not be executed.
- **95 . Will finally be executed in the program below?** \
  Here is an example to determine if the `finally` block will be executed:
  ```java
  public class Example {
      public static void main(String[] args) {
          try {
              System.out.println("Try block");
              System.exit(0);
          } catch (Exception e) {
              System.out.println("Catch block");
          } finally {
              System.out.println("Finally block");
          }
      }
  }
  ```
  In this example, the `System.exit(0)` method is called in the `try` block, which will terminate the program
  immediately. As a result, the code in the `finally` block will not be executed.
- **96 . Is try without a catch is allowed?** \
  Yes, a `try` block without a `catch` block is allowed in Java. This is known as a try-with-resources statement and is
  used to automatically close resources that implement the `AutoCloseable` interface. The `try` block can be followed by
  one or more `catch` blocks or a `finally` block, but it is not required to have a `catch` block.

  Here is an example of a try-with-resources statement:

    ```java
    public class Example {
        public static void main(String[] args) {
            try (BufferedReader reader = new BufferedReader(new FileReader("example.txt"))) {
                String line = reader.readLine();
                System.out.println(line);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    ```

  In this example, the `try` block contains a `BufferedReader` resource that is automatically closed when the `try`
  block exits. The `catch` block handles any `IOException` that may occur while reading from the file.
- **97 . Is try without catch and finally allowed?** \
  Yes, a `try` block without a `catch` or `finally` block is allowed in Java. This is known as a try-with-resources
  statement and is used to automatically close resources that implement the `AutoCloseable` interface. The `try` block
  can be followed by one or more `catch` blocks or a `finally` block, but it is not required to have a `catch` or
  `finally` block.

  Here is an example of a try-with-resources statement without a `catch` or `finally` block:

    ```java
    public class Example {
        public static void main(String[] args) {
            try (BufferedReader reader = new BufferedReader(new FileReader("example.txt"))) {
                String line = reader.readLine();
                System.out.println(line);
            }
        }
    }
    ```

  In this example, the `try` block contains a `BufferedReader` resource that is automatically closed when the `try`
  block exits. There is no `catch` or `finally` block, as the resource is automatically closed by the try-with-resources
  statement.
- **98 . Can you explain the hierarchy of exception handling classes?** \
  In Java, exception handling is based on a hierarchy of classes that extend the `Throwable` class. The main classes in
  the exception handling hierarchy are:

    - **Throwable**: The `Throwable` class is the root class of the exception hierarchy. It has two main subclasses:
        - **Error**: Errors are serious issues that are typically outside the control of the program and indicate
          problems
          with the environment in which the application is running. Examples include `OutOfMemoryError`,
          `StackOverflowError`, and `VirtualMachineError`.
        - **Exception**: Exceptions are conditions that a program might want to catch and handle. They are divided into
          two
          main categories:
            - **Checked Exceptions**: These are exceptions that are checked at compile-time. The programmer is required
              to
              handle these exceptions, either by using a `try-catch` block or by declaring them in the method signature
              using the `throws` keyword. Examples include `IOException`, `SQLException`, and `FileNotFoundException`.
            - **Unchecked Exceptions**: These are exceptions that are not checked at compile-time but occur during
              runtime.
              They are subclasses of `RuntimeException` and do not need to be declared or caught. Examples include
              `NullPointerException`, `ArrayIndexOutOfBoundsException`, and `IllegalArgumentException`.

  The exception handling hierarchy allows for different types of exceptions to be caught and handled in a structured
  way. By understanding the hierarchy of exception handling classes, you can write more robust and reliable code that
  handles errors and exceptions effectively.
- **99 . What is the difference between error and exception?**
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
- **101 . How do you throw an exception from a method?**
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
- **102 . What happens when you throw a checked exception from a method?** \
  When you throw a checked exception from a method in Java, you must either catch the exception using a `try-catch`
  block or declare the exception using the `throws` keyword in the method signature. If you throw a checked exception
  without handling it, the code will not compile, and you will get a compilation error. Checked exceptions are checked
  at
  compile-time to ensure that they are handled properly.
- **103 . What are the options you have to eliminate compilation errors when handling checked exceptions?** \
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
- **104 . How do you create a custom exception?** \
  To create a custom exception in Java, you need to define a new class that extends the `Exception` class or one of its
  subclasses. You can add custom fields, constructors, and methods to the custom exception class to provide additional
  information about the exception.

  Here is an example of a custom exception class:

    ```java
    public class CustomException extends Exception {
        public CustomException(String message) {
            super(message);
        }
    }
    ```

  In this example, the `CustomException` class extends the `Exception` class and provides a constructor that takes a
  message as an argument. This allows you to create custom exceptions with a specific error message. You can also add
  the related mechanisms to handle the new custom exception to provide a more detailed error message, and also
  use the adequate processing of the exception by the logging system or the user interface.
  Note: most of the time all the exceptions and custom exceptions are sent to the logging system, and the user
  interface. The most popular is to log the exceptions using log4j or derivative logging systems like external logging
  apis for Splunk or ELK. Splunk is a popular tool for monitoring, searching, and analyzing machine-generated big data,
- **105 . How do you handle multiple exception types with same exception handling block?** \
  In Java, you can handle multiple exception types with the same exception handling block by using a multi-catch block.
  This allows you to catch multiple exceptions in a single `catch` block and handle them in a common way. The syntax for
  a multi-catch block is to specify the exception types separated by a vertical bar (`|`).

  Here is an example of a multi-catch block:

    ```java
    public class Example {
        public static void main(String[] args) {
            try {
                // Code that may throw exceptions
                int result = 10 / 0;
            } catch (ArithmeticException | NullPointerException e) {
                // Handle the exceptions
                e.printStackTrace();
            }
        }
    }
    ```

  In this example, the `catch` block catches both `ArithmeticException` and `NullPointerException` exceptions and
  handles
  them in a common way. This can help reduce code duplication and improve the readability of the exception handling
  code.
- **106 . Can you explain about try with resources?** \
  Try-with-resources is a feature introduced in Java 7 that simplifies resource management by automatically closing
  resources that implement the `AutoCloseable` interface. It eliminates the need for explicit `finally` blocks to close
  resources and ensures that resources are closed properly, even if an exception occurs.

  Here is an example of try-with-resources:

    ```java
    public class Example {
        public static void main(String[] args) {
            try (BufferedReader reader = new BufferedReader(new FileReader("example.txt"))) {
                String line = reader.readLine();
                System.out.println(line);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    ```

  In this example, the `try` block contains a `BufferedReader` resource that is automatically closed when the `try`
  block exits. The `BufferedReader` class implements the `AutoCloseable` interface, which allows it to be used with
  try-with-resources. If an `IOException` occurs while reading from the file, it is caught and handled in the `catch`
  block. The `BufferedReader` resource is automatically closed when the `try` block exits, ensuring that resources are
  released properly.
  The big advantage of try-with-resources is that it simplifies resource management and reduces the risk of resource
  leaks and other issues related to manual resource handling.
- **107 . How does try with resources work?** \
  Try-with-resources in Java works by automatically closing resources that implement the `AutoCloseable` interface when
  the `try` block exits. It simplifies resource management by eliminating the need for explicit `finally` blocks to
  close
  resources and ensures that resources are closed properly, even if an exception occurs.

  When using try-with-resources, the resources are declared and initialized within the parentheses of the `try`
  statement.
  The resources are automatically closed in the reverse order of their declaration when the `try` block exits. If an
  exception occurs during the execution of the `try` block, the resources are closed before the exception is propagated.

  Here is an example of try-with-resources:

    ```java
    public class Example {
        public static void main(String[] args) {
            try (BufferedReader reader = new BufferedReader(new FileReader("example.txt"))) {
                String line = reader.readLine();
                System.out.println(line);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    ```

  In this example, the `BufferedReader` resource is declared and initialized within the parentheses of the `try`
  statement. The `BufferedReader` resource is automatically closed when the `try` block exits, ensuring that resources
  are released properly. If an `IOException` occurs while reading from the file, it is caught and handled in the `catch`
  block. The `BufferedReader` resource is still automatically closed before the exception is propagated.
- **108 . Can you explain a few exception handling best practices?** \
  Some exception handling best practices in Java include:

    - **Catch Specific Exceptions**: Catch specific exceptions rather than catching the general `Exception` class. This
      allows you to handle different types of exceptions in a more targeted way.
    - **Use try-with-resources**: Use try-with-resources to automatically close resources that implement the
      `AutoCloseable` interface. This simplifies resource management and reduces the risk of resource leaks.
    - **Log Exceptions**: Log exceptions using a logging framework like log4j or SLF4J to capture information about
      errors and exceptions. This can help with debugging and diagnosing issues in the code.
    - **Handle Exceptions Appropriately**: Handle exceptions appropriately based on the context and severity of the
      error. This may involve logging the exception, displaying an error message to the user, or taking corrective
      action.
    - **Avoid Swallowing Exceptions**: Avoid swallowing exceptions by catching them and not doing anything with them.
      This can lead to silent failures and make it difficult to diagnose issues in the code.
    - **Use Checked Exceptions Wisely**: Use checked exceptions judiciously and only for conditions that the caller can
      reasonably be expected to handle. Consider using unchecked exceptions for exceptional conditions that are outside
      the control of the caller.
    - **Throw Custom Exceptions**: Throw custom exceptions to provide more context and information about the error. This
      can help with debugging and make it easier to handle specific types of errors.
    - **Follow the Principle of Least Surprise**: Follow the principle of least surprise by handling exceptions in a way
      that is consistent with the rest of the codebase and does not introduce unexpected behavior.
    - **Document Exception Handling**: Document exception handling in the code to explain why exceptions are being
      caught
      and how they are being handled. This can help other developers understand the intent behind the exception handling
      logic.
    - **Test Exception Handling**: Test exception handling code to ensure that it behaves as expected and handles errors
      correctly in different scenarios. This can help identify and fix issues before they reach production.
    - **Use Standard Error Codes**: Use standard error codes or messages to provide consistent and meaningful feedback
      to users when exceptions occur. This can help users understand the cause of the error and take appropriate action.
    - **Avoid Catching Throwable**: Avoid catching the `Throwable` class, as this can catch errors and other serious
      issues
      that should not be caught or handled by the application. Catch specific exceptions instead.

### Miscellaneous topics

- **109 . What are the default values in an array?** \
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
- **110 . How do you loop around an array using enhanced for loop?** \
  You can loop around an array using an enhanced for loop in Java. The enhanced for loop, also known as the for-each
  loop, provides a more concise syntax for iterating over elements in an array or a collection. It eliminates the need
  for explicit indexing and bounds checking and makes the code more readable.

  Here is an example of looping around an array using an enhanced for loop:

    ```java
    public class Example {
        public static void main(String[] args) {
            int[] numbers = {1, 2, 3, 4, 5};
            for (int number : numbers) {
                System.out.println(number);
            }
        }
    }
    ```

  In this example, the enhanced for loop iterates over the `numbers` array and prints each element to the console. The
  `number` variable represents the current element in the array during each iteration of the loop.
- **111 . How do you print the content of an array?** \
  You can print the content of an array in Java by iterating over the elements of the array and printing each element to
  the console. There are several ways to print the content of an array, including using a `for` loop, an enhanced `for`
  loop, or the `Arrays.toString` method from the `java.util` package.

  Here are some examples:

    - **Using a For Loop**:

      ```java
      public class Example {
          public static void main(String[] args) {
              int[] numbers = {1, 2, 3, 4, 5};
              for (int i = 0; i < numbers.length; i++) {
                  System.out.println(numbers[i]);
              }
          }
      }
      ```

    - **Using an Enhanced For Loop**:

      ```java
      public class Example {
          public static void main(String[] args) {
              int[] numbers = {1, 2, 3, 4, 5};
              for (int number : numbers) {
                  System.out.println(number);
              }
          }
      }
      ```

    - **Using Arrays.toString**:

      ```java
      import java.util.Arrays;

      public class Example {
          public static void main(String[] args) {
              int[] numbers = {1, 2, 3, 4, 5};
              System.out.println(Arrays.toString(numbers));
          }
      }
      ```

  In these examples, the content of the `numbers` array is printed to the console using different methods for iterating
  over the elements of the array.
- **112 . How do you compare two arrays?** \
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
- **113 . What is an enum?** \
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
- **114 . Can you use a switch statement around an enum?** \
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
- **115 . What are variable arguments or varargs?** \
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
- **116 . What are asserts used for?** \
  Asserts in Java are used to test assumptions in the code and validate conditions that should be true during program
  execution. They are typically used for debugging and testing purposes to catch errors and inconsistencies in the code.
  Asserts are disabled by default in Java and can be enabled using the `-ea` flag when running the JVM.

  Here is an example of using asserts:

    ```java
    public class Main {
        public static void main(String[] args) {
            int x = Integer.parseInt(args[0]);
            assert x > 0 : "x must be greater than 0";
        }
    }
    ```

  In this example, the `assert` statement checks if the value of `x` is greater than 0 and throws an `AssertionError`
  with the message `"x must be greater than 0"` if the condition is false. Asserts are typically used to validate
  assumptions and catch errors early in the development process.
- **117 . When should asserts be used?** \
  Asserts in Java should be used in the following scenarios:

    - **Debugging**: Use asserts to catch errors and inconsistencies in the code during development and testing. They
      can
      help identify issues early in the development process and provide feedback on incorrect assumptions.
    - **Testing**: Use asserts to validate conditions and assumptions in unit tests and integration tests. They can help
      ensure that the code behaves as expected and meets the requirements.
    - **Preconditions**: Use asserts to check preconditions and validate input parameters in methods. They can help
      ensure that the method is called with the correct arguments and that the conditions are met.
    - **Invariants**: Use asserts to check invariants and validate the state of objects or data structures. They can
      help
      ensure that the program is in a consistent state and that the data is valid.
    - **Performance**: Use asserts to check performance-related conditions and validate optimizations. They can help
      ensure that the code is efficient and performs as expected.
    - **Security**: Use asserts to check security-related conditions and validate access controls. They can help ensure
      that the code is secure and protected against vulnerabilities.

  Asserts should be used judiciously and in situations where they provide value in validating assumptions and catching
  errors. They are typically disabled in production code and enabled during development and testing to provide feedback
  on incorrect assumptions and conditions.
  Note: It is important to note that asserts are disabled by default in Java and should not be used as a replacement for
  proper error handling and validation in production code. They are intended for debugging and testing purposes and
  should be used judiciously to catch errors and inconsistencies during development and testing. Also the asserts are
  different from the asserts related to the unit testing framework because these last are particular validations for the
  output of a unit (method) and asserts in java are checks for correct use of the contract of a method.
- **118 . What is garbage collection?** \
  Garbage collection in Java is the process of automatically reclaiming memory that is no longer in use by the program.
  It is a key feature of the Java Virtual Machine (JVM) that manages memory allocation and deallocation for objects
  created during program execution. Garbage collection helps prevent memory leaks and ensures that memory is used
  efficiently by reclaiming unused memory and making it available for new objects.

  The garbage collection process involves several steps, including identifying unreferenced objects, reclaiming memory
  used by those objects, and compacting memory to reduce fragmentation. Garbage collection is performed by the JVM's
  garbage collector, which runs in the background and periodically checks for unused objects to reclaim memory.

  Garbage collection is an essential part of Java's memory management model and helps simplify memory management for
  developers by automating the process of memory allocation and deallocation. It allows developers to focus on writing
  code without having to worry about manual memory management and memory leaks.
- **119 . Can you explain garbage collection with an example?** \
  Garbage collection in Java is the process of automatically reclaiming memory that is no longer in use by the program.
  It helps prevent memory leaks and ensures that memory is used efficiently by reclaiming unused memory and making it
  available for new objects. Here is an example of garbage collection in Java:

    ```java
    public class Main {
        public static void main(String[] args) {
            // Create an object
            Object obj = new Object();

            // Set the reference to null
            obj = null;

            // Request garbage collection
            System.gc();
        }
    }
    ```

  In this example, an object `obj` is created and then set to `null` to remove the reference to the object. The
  `System.gc()` method is called to request garbage collection by the JVM. The garbage collector will identify the
  unreferenced object and reclaim the memory used by the object. This process helps free up memory that is no longer in
  use and makes it available for new objects.
- **120 . When is garbage collection run?** \
  Garbage collection in Java is run by the JVM's garbage collector at specific intervals or when certain conditions are
  met. The garbage collector runs in the background and periodically checks for unused objects to reclaim memory. The
  exact timing and frequency of garbage collection depend on the JVM implementation and the garbage collection
  algorithm used.

  Garbage collection is typically run when one of the following conditions is met:

    - **Memory Pressure**: When the JVM detects that the available memory is running low, it triggers garbage collection
      to reclaim memory and free up space for new objects.
    - **Idle Time**: When the JVM is idle or has spare CPU cycles, it may run garbage collection to reclaim memory and
      optimize memory usage.
    - **Explicit Request**: Garbage collection can be explicitly triggered by calling the `System.gc()` method or using
      JVM options like `-XX:+ExplicitGCInvokesConcurrent`.
    - **Generation Thresholds**: Garbage collection is run based on generation thresholds, such as the young generation
      and old generation, to optimize memory management and reduce the impact on application performance.
    - **Heap Size**: Garbage collection is run when the heap size exceeds a certain threshold, such as the maximum heap
      size specified by the `-Xmx` JVM option.

  The garbage collector uses various algorithms and strategies to determine when and how to reclaim memory based on the
  application's memory usage and requirements. By running garbage collection at specific intervals or when certain
  conditions are met, the JVM can optimize memory management and ensure that memory is used efficiently.
- **121 . What are best practices on garbage collection?** \
  Some best practices for garbage collection in Java include:

    - **Avoid Premature Optimization**: Avoid premature optimization of memory usage and garbage collection. Let the
      JVM's garbage collector manage memory automatically and optimize memory usage based on the application's
      requirements.
    - **Use Proper Data Structures**: Use appropriate data structures and algorithms to minimize memory usage and
      reduce the impact on garbage collection. Choose data structures that are efficient and optimized for memory
      management.
    - **Minimize Object Creation**: Minimize the creation of unnecessary objects and use object pooling or caching to
      reuse objects where possible. This can reduce the number of objects that need to be garbage collected and improve
      performance.
    - **Avoid Memory Leaks**: Avoid memory leaks by ensuring that objects are properly dereferenced and released when
      they are no longer needed. Be mindful of retaining references to objects that are no longer in use.
    - **Tune Garbage Collection**: Tune garbage collection settings and parameters based on the application's memory
      requirements and performance goals. Experiment with different garbage collection algorithms and options to
      optimize memory management.
    - **Monitor Memory Usage**: Monitor memory usage and garbage collection activity to identify potential issues and
      optimize memory management. Use tools like JVisualVM, VisualVM, or Java Mission Control to analyze memory usage
      and garbage collection behavior.
    - **Profile and Optimize**: Profile the application to identify memory bottlenecks and optimize memory usage. Use
      profiling tools to analyze memory allocation, object creation, and garbage collection patterns to improve
      performance.
    - **Use Finalizers Sparingly**: Use finalizers sparingly and avoid relying on them for resource cleanup. Finalizers
      can introduce performance overhead and may not be called in a timely manner. Consider using try-with-resources or
      other mechanisms for resource cleanup.
    - **Avoid Circular References**: Avoid circular references between objects, as they can prevent objects from being
      garbage collected. Break circular references by using weak references or other techniques to allow objects to be
      garbage collected when they are no longer needed.
    - **Optimize Object Lifecycle**: Optimize the lifecycle of objects to minimize memory usage and reduce the impact on
      garbage collection. Use object pooling, lazy initialization, and other techniques to manage object creation and
      destruction efficiently.
    - **Use Memory Profiling Tools**: Use memory profiling tools to analyze memory usage, object allocation, and garbage
      collection behavior. These tools can help identify memory leaks, performance bottlenecks, and areas for
      optimization.
- **122 . What are initialization blocks?** \
  Initialization blocks in Java are used to initialize instance variables of a class. There are two types of
  initialization blocks in Java: instance initializer blocks and static initializer blocks.

    - **Instance Initializer Block**: An instance initializer block is used to initialize instance variables of a class.
      It is executed when an instance of the class is created and can be used to perform complex initialization logic.
      Instance initializer blocks are defined within curly braces `{}` and are executed before the constructor of the
      class.

      Here is an example of an instance initializer block:

      ```java
      public class Example {
          private int x;
  
          {
              x = 10;
          }
  
          public Example() {
              System.out.println("Constructor called");
          }
  
          public static void main(String[] args) {
              Example example = new Example();
              System.out.println("Value of x: " + example.x);
          }
      }
      ```

    - **Static Initializer Block**: A static initializer block is used to initialize static variables of a class. It is
      executed when the class is loaded by the JVM and can be used to perform one-time initialization tasks. Static
      initializer blocks are defined with the `static` keyword and are executed before the class is used.

      Here is an example of a static initializer block:

      ```java
      public class Example {
          private static int x;
  
          static {
              x = 10;
          }
  
          public static void main(String[] args) {
              System.out.println("Value of x: " + x);
          }
      }
      ```

  In these examples, the instance initializer block is used to initialize the `x` instance variable, and the static
  initializer block is used to initialize the `x` static variable. Initialization blocks are useful for performing
  complex initialization logic and ensuring that variables are properly initialized when an instance of the class is
  created.
- **123 . What is a static initializer?** \
  A static initializer in Java is used to initialize static variables of a class. It is executed when the class is
  loaded
  by the JVM and can be used to perform one-time initialization tasks. Static initializer blocks are defined with the
  `static` keyword and are executed before the class is used.
- **124 . What is an instance initializer block?** \
  An instance initializer block in Java is used to initialize instance variables of a class. It is executed when an
  instance of the class is created and can be used to perform complex initialization logic. Instance initializer blocks
  are defined within curly braces `{}` and are executed before the constructor of the class.

  Here is an example of an instance initializer block:

    ```java
    public class Example {
        private int x;

        {
            x = 10;
        }

        public Example() {
            System.out.println("Constructor called");
        }

        public static void main(String[] args) {
            Example example = new Example();
            System.out.println("Value of x: " + example.x);
        }
    }
    ```

  In this example, the instance initializer block is used to initialize the `x` instance variable before the constructor
  is called. The instance initializer block is executed when an instance of the `Example` class is created and sets the
  value of `x` to `10`.
- **125 . What is tokenizing?** \
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
- **126 . Can you give an example of tokenizing?** \
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
- **127 . What is serialization?** \
  Serialization in Java is the process of converting an object into a stream of bytes that can be saved to a file,
  sent over a network, or stored in a database. Serialization allows objects to be persisted and transferred between
  different systems and platforms. The serialized object can be deserialized back into an object to restore its state
  and properties.

  Java provides the `Serializable` interface, which is used to mark classes as serializable. Classes that implement the
  `Serializable` interface can be serialized and deserialized using the `ObjectOutputStream` and `ObjectInputStream`
  classes.

  Here is an example of serializing and deserializing an object:

    ```java
    import java.io.*;

    public class Main {
        public static void main(String[] args) {
            // Serialize object
            try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("object.ser"))) {
                MyClass obj = new MyClass();
                out.writeObject(obj);
            } catch (IOException e) {
                e.printStackTrace();
            }

            // Deserialize object
            try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("object.ser"))) {
                MyClass obj = (MyClass) in.readObject();
                System.out.println(obj);
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
    }

    class MyClass implements Serializable {
        private static final long serialVersionUID = 1L;
    }
    ```

  In this example, the `MyClass` object is serialized to a file named `object.ser` using an `ObjectOutputStream`. The
  object is then deserialized back into an object using an `ObjectInputStream` and printed to the console.
- **128 . How do you serialize an object using serializable interface?** \
  To serialize an object in Java using the `Serializable` interface, follow these steps:

    1. Implement the `Serializable` interface in the class that you want to serialize. The `Serializable` interface is a
       marker interface that indicates that the class can be serialized.

    2. Create an instance of the `ObjectOutputStream` class and pass it a `FileOutputStream` or other output stream to
       write the serialized object to a file or other destination.

    3. Call the `writeObject` method on the `ObjectOutputStream` instance and pass the object that you want to serialize
       as an argument.

    4. Close the `ObjectOutputStream` to flush the output stream and release any system resources.

  Here is an example of serializing an object using the `Serializable` interface:

    ```java
    import java.io.*;

    public class Main {
        public static void main(String[] args) {
            try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("object.ser"))) {
                MyClass obj = new MyClass();
                out.writeObject(obj);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    class MyClass implements Serializable {
        private static final long serialVersionUID = 1L;
    }
    ```

  In this example, the `MyClass` object is serialized to a file named `object.ser` using an `ObjectOutputStream`. The
  `MyClass` class implements the `Serializable` interface, which allows it to be serialized and written to the output
  stream.
- **129 . How do you de-serialize in Java?** \
  To deserialize an object in Java, follow these steps:

    1. Create an instance of the `ObjectInputStream` class and pass it a `FileInputStream` or other input stream to read
       the serialized object from a file or other source.

    2. Call the `readObject` method on the `ObjectInputStream` instance to read the serialized object from the input
       stream.

    3. Cast the returned object to the appropriate class type to restore the object's state and properties.

    4. Close the `ObjectInputStream` to release any system resources.

  Here is an example of deserializing an object in Java:

    ```java
    import java.io.*;

    public class Main {
        public static void main(String[] args) {
            try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("object.ser"))) {
                MyClass obj = (MyClass) in.readObject();
                System.out.println(obj);
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
    }

    class MyClass implements Serializable {
        private static final long serialVersionUID = 1L;
    }
    ```

  In this example, the `MyClass` object is deserialized from a file named `object.ser` using an `ObjectInputStream`. The
  serialized object is read from the input stream and cast to the `MyClass` class type to restore its state and
  properties.
- **130 . What do you do if only parts of the object have to be serialized?** \
  If only parts of an object need to be serialized in Java, you can use the `transient` keyword to mark fields that
  should not be serialized. The `transient` keyword tells the JVM to skip the serialization of the marked field and
  exclude it from the serialized object.

  Here is an example of using the `transient` keyword to exclude fields from serialization:

    ```java
    import java.io.*;

    public class Main {
        public static void main(String[] args) {
            try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("object.ser"))) {
                MyClass obj = new MyClass();
                out.writeObject(obj);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    class MyClass implements Serializable {
        private static final long serialVersionUID = 1L;
        private transient int x = 10;
        private int y = 20;

        @Override
        public String toString() {
            return "MyClass{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }
    ```

  In this example, the `x` field is marked as `transient` in the `MyClass` class, which excludes it from serialization.
  When the `MyClass` object is serialized, the `x` field is skipped, and only the `y` field is serialized and
  deserialized.
- **131 . How do you serialize a hierarchy of objects?** \
  To serialize a hierarchy of objects in Java, follow these steps:

    1. Implement the `Serializable` interface in all classes in the hierarchy that need to be serialized. The
       `Serializable` interface is a marker interface that indicates that the class can be serialized.

    2. Create an instance of the `ObjectOutputStream` class and pass it a `FileOutputStream` or other output stream to
       write the serialized objects to a file or other destination.

    3. Call the `writeObject` method on the `ObjectOutputStream` instance and pass the root object of the hierarchy that
       you want to serialize.

    4. Close the `ObjectOutputStream` to flush the output stream and release any system resources.

  Here is an example of serializing a hierarchy of objects in Java:

    ```java
    import java.io.*;

    public class Main {
        public static void main(String[] args) {
            try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("object.ser"))) {
                Parent parent = new Parent();
                parent.child = new Child();
                out.writeObject(parent);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    class Parent implements Serializable {
        private static final long serialVersionUID = 1L;
        Child child;
    }

    class Child implements Serializable {
        private static final long serialVersionUID = 1L;
    }
    ```

  In this example, the `Parent` and `Child` classes implement the `Serializable` interface, allowing them to be
  serialized. The `Parent` class contains a reference to a `Child` object, creating a hierarchy of objects that can be
  serialized and deserialized.
- **132 . Are the constructors in an object invoked when it is de-serialized?** \
  When an object is deserialized in Java, the constructors of the object are not invoked. Instead, the object is
  restored from the serialized form, and its state and properties are reconstructed based on the serialized data. The
  deserialization process uses the serialized data to recreate the object's state without calling the constructor.

  If the class being deserialized has a `readObject` method, the `readObject` method is called during deserialization to
  restore the object's state. The `readObject` method can be used to perform custom deserialization logic and initialize
  transient fields that were excluded from serialization.

  Here is an example of deserializing an object in Java without invoking the constructor:

    ```java
    import java.io.*;

    public class Main {
        public static void main(String[] args) {
            try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("object.ser"))) {
                MyClass obj = (MyClass) in.readObject();
                System.out.println(obj);
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
    }

    class MyClass implements Serializable {
        private static final long serialVersionUID = 1L;

        public MyClass() {
            System.out.println("Constructor called");
        }

        @Override
        public String toString() {
            return "MyClass{}";
        }
    }
    ``` 
- **133 . Are the values of static variables stored when an object is serialized?** \
  When an object is serialized in Java, the values of static variables are not stored as part of the serialized object.
  Static variables are associated with the class itself rather than individual instances of the class, so they are not
  serialized along with the object. When an object is deserialized, the static variables are initialized based on the
  class definition and are not restored from the serialized data.

  Here is an example that demonstrates that static variables are not stored when an object is serialized:

    ```java
    import java.io.*;

    public class Main {
        public static void main(String[] args) {
            try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("object.ser"))) {
                MyClass obj = new MyClass();
                out.writeObject(obj);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    class MyClass implements Serializable {
        private static final long serialVersionUID = 1L;
        private static int x = 10;

        @Override
        public String toString() {
            return "MyClass{" +
                    "x=" + x +
                    '}';
        }
    }
    ```

  In this example, the `MyClass` object is serialized to a file named `object.ser`, but the value of the `x` static
  variable is not stored as part of the serialized object. When the object is deserialized, the `x` static variable is
  initialized based on the class definition and is not restored from the serialized data.

### Collections

- **134 . Why do we need collections in Java?** \
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
- **135 . What are the important interfaces in the collection hierarchy?** \
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
- **136 . What are the important methods that are declared in the collection interface?** \
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
- **137 . Can you explain briefly about the List interface?** \
  The `List` interface in Java extends the `Collection` interface and represents an ordered collection of elements
  that allows duplicates. Lists maintain the insertion order of elements and provide methods for accessing, adding,
  removing, and updating elements at specific positions. Some of the key features of the `List` interface include:

    - **Ordered Collection**: Lists maintain the order in which elements are added and allow duplicate elements.
    - **Indexed Access**: Elements in a list can be accessed using an index, starting from zero.
    - **Positional Operations**: Lists provide methods for adding, removing, and updating elements at specific
      positions.
    - **Iterating Over Elements**: Lists can be iterated over using an iterator or enhanced for loop.
    - **Sublist Operations**: Lists support operations for creating sublists of elements based on specific ranges.
    - **Sorting**: Lists can be sorted using the `Collections.sort` method.

  The `List` interface is implemented by classes like `ArrayList`, `LinkedList`, and `Vector` in the Java Collections
  Framework. It provides a flexible and efficient way to work with ordered collections of elements.
- **138 . Explain about ArrayList with an example?** \
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
- **139 . Can an ArrayList have duplicate elements?** \
  Yes, an `ArrayList` in Java can have duplicate elements. Unlike a `Set`, which does not allow duplicates, an
  `ArrayList` allows elements to be added multiple times. This means that an `ArrayList` can contain duplicate elements
  at different positions in the list. The order of elements in an `ArrayList` is maintained, so duplicate elements will
  appear in the list in the order in which they were added.
- **140 . How do you iterate around an ArrayList using iterator?** \
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
- **141 . How do you sort an ArrayList?** \
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
- **142 . How do you sort elements in an ArrayList using comparable interface?** \
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
- **143 . How do you sort elements in an ArrayList using comparator interface?** \
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
- **144 . What is vector class? How is it different from an ArrayList?** \
  The `Vector` class in Java is a legacy collection class that is similar to an `ArrayList` but is synchronized. This
  means that access to a `Vector` is thread-safe, making it suitable for use in multi-threaded environments. The
  `Vector` class provides methods for adding, removing, and accessing elements in the list, as well as for iterating
  over the elements.

  Some key differences between `Vector` and `ArrayList` include:
    - **Synchronization**: `Vector` is synchronized, while `ArrayList` is not. This means that access to a `Vector` is
      thread-safe, but it can be slower in single-threaded applications.
    - **Performance**: `ArrayList` is generally faster than `Vector` because it is not synchronized. In single-threaded
      applications, `ArrayList` is preferred for its better performance.
    - **Legacy**: `Vector` is a legacy class that was introduced in Java 1.0, while `ArrayList` is part of the Java
      Collections Framework introduced in Java 2. `ArrayList` is the preferred choice for most applications due to its
      better performance and flexibility.

  Despite these differences, both `Vector` and `ArrayList` provide similar functionality for working with collections of
  objects in Java.
- **145 . What is linkedList? What interfaces does it implement? How is it different from an ArrayList?** \
  The `LinkedList` class in Java is a doubly-linked list implementation of the `List` interface. It provides efficient
  insertion and deletion of elements at the beginning, middle, and end of the list. `LinkedList` implements the `List`,
  `Deque`, and `Queue` interfaces, making it suitable for a wide range of operations.

  Some key differences between `LinkedList` and `ArrayList` include:
    - **Underlying Data Structure**: `ArrayList` uses an array to store elements, while `LinkedList` uses a
      doubly-linked
      list. This makes `LinkedList` more efficient for adding and removing elements in the middle of the list.
    - **Performance**: `ArrayList` is generally faster than `LinkedList` for random access and iteration, as it provides
      constant-time access to elements. `LinkedList` is more efficient for adding and removing elements in the middle of
      the list.
    - **Memory Overhead**: `LinkedList` has higher memory overhead than `ArrayList` due to the additional pointers
      required for the linked list structure. This can impact performance and memory usage in large collections.

  Despite these differences, both `LinkedList` and `ArrayList` provide similar functionality for working with
  collections of objects in Java, and the choice between them depends on the specific requirements of the application.
- **146 . Can you briefly explain about the Set interface?** \
  The `Set` interface in Java extends the `Collection` interface and represents a collection of unique elements with no
  duplicates. Sets do not allow duplicate elements, and they maintain no specific order of elements. The `Set`
  interface provides methods for adding, removing, and checking the presence of elements in the set.

  Some key features of the `Set` interface include:
    - **Unique Elements**: Sets do not allow duplicate elements, ensuring that each element is unique.
    - **No Specific Order**: Sets do not maintain the order of elements, so the order in which elements are added may
      not
      be preserved.
    - **Fast Lookup**: Sets provide fast lookup operations for checking the presence of elements.
    - **Iterating Over Elements**: Sets can be iterated over using an iterator or enhanced for loop.
    - **Implementations**: The `Set` interface is implemented by classes like `HashSet`, `LinkedHashSet`, and `TreeSet`
      in the Java Collections Framework.

  The `Set` interface is commonly used to store collections of unique elements and perform operations like union,
  intersection, and difference on sets. It provides a flexible and efficient way to work with sets of objects in Java.
- **147 . What are the important interfaces related to the Set interface?** \
  The `Set` interface in Java is related to several other interfaces in the Java Collections Framework that provide
  additional functionality for working with sets of elements. Some of the important interfaces related to the `Set`
  interface include:

    - **SortedSet**: An interface that extends `Set` and represents a set of elements sorted in a specific order. Sorted
      sets maintain the order of elements based on their natural ordering or a custom comparator.
    - **NavigableSet**: An interface that extends `SortedSet` and provides navigation methods for accessing elements in
      a
      set. Navigable sets support operations like finding the closest element, finding subsets, and performing range
      queries.

  These interfaces build on the functionality provided by the `Set` interface and offer additional features for working
  with sets of elements in Java.
- **148 . What is the difference between Set and sortedSet interfaces?** \
  The `Set` and `SortedSet` interfaces in Java are related interfaces in the Java Collections Framework that represent
  collections of unique elements with no duplicates. The main difference between `Set` and `SortedSet` is the ordering
  of elements:

    - **Set**: The `Set` interface does not maintain the order of elements and does not provide any guarantees about the
      order in which elements are stored. Sets are typically implemented using hash-based data structures like `HashSet`
      and `LinkedHashSet`.
    - **SortedSet**: The `SortedSet` interface extends `Set` and represents a set of elements sorted in a specific
      order.
      Sorted sets maintain the order of elements based on their natural ordering or a custom comparator. Common
      implementations of `SortedSet` include `TreeSet` and `ConcurrentSkipListSet`.

  In summary, `Set` is a general interface for collections of unique elements, while `SortedSet` is a specialized
  interface for sets that maintain the order of elements based on a specific ordering.
- **149 . Can you give examples of classes that implement the Set interface?** \
  The `Set` interface in Java is implemented by several classes in the Java Collections Framework that provide
  different implementations of sets. Some of the common classes that implement the `Set` interface include:

    - **HashSet**: A class that implements the `Set` interface using a hash table data structure. `HashSet` provides
      constant-time performance for basic operations like adding, removing, and checking the presence of elements.
    - **LinkedHashSet**: A class that extends `HashSet` and maintains the order of elements based on their insertion
      order. `LinkedHashSet` provides predictable iteration order and constant-time performance for basic operations.
    - **TreeSet**: A class that implements the `SortedSet` interface using a red-black tree data structure. `TreeSet`
      maintains the order of elements based on their natural ordering or a custom comparator and provides log-time
      performance for basic operations.

  These classes provide different implementations of sets with varying performance characteristics and ordering
  guarantees.
- **150 . What is a HashSet? How is it different from a TreeSet?** \
  `HashSet` and `TreeSet` are two common implementations of the `Set` interface in Java that provide different
  characteristics for working with sets of elements. The main differences between `HashSet` and `TreeSet` include:

    - **Underlying Data Structure**: `HashSet` uses a hash table data structure to store elements, providing constant
      time performance for basic operations like adding, removing, and checking the presence of elements. `TreeSet` uses
      a red-black tree data structure to maintain the order of elements based on their natural ordering or a custom
      comparator.
    - **Ordering**: `HashSet` does not maintain the order of elements and does not provide any guarantees about the
      order in which elements are stored. `TreeSet` maintains the order of elements based on their natural ordering or a
      custom comparator, allowing elements to be sorted in a specific order.
    - **Performance**: `HashSet` provides constant-time performance for basic operations, making it efficient for
      adding, removing, and checking the presence of elements. `TreeSet` provides log-time performance for basic
      operations, making it efficient for maintaining the order of elements and performing range queries.

  In summary, `HashSet` is a hash-based set implementation with no ordering guarantees, while `TreeSet` is a tree-based
  set implementation that maintains the order of elements based on their natural ordering or a custom comparator.
- **151 . What is a linkedHashSet? How is different from a HashSet?** \
  `LinkedHashSet` is a class in Java that extends `HashSet` and maintains the order of elements based on their insertion
  order. Unlike `HashSet`, which does not maintain the order of elements, `LinkedHashSet` provides predictable iteration
  order and constant-time performance for basic operations. `LinkedHashSet` is implemented using a hash table with a
  linked list that maintains the order of elements as they are added to the set.

  Some key differences between `LinkedHashSet` and `HashSet` include:
    - **Ordering**: `LinkedHashSet` maintains the order of elements based on their insertion order, providing
      predictable
      iteration order. `HashSet` does not maintain the order of elements and does not provide any guarantees about the
      order in which elements are stored.
    - **Underlying Data Structure**: `LinkedHashSet` uses a hash table with a linked list to maintain the order of
      elements, while `HashSet` uses a hash table data structure. This linked list allows `LinkedHashSet` to provide
      constant-time performance for maintaining the order of elements.

  In summary, `LinkedHashSet` is a hash-based set implementation that maintains the order of elements based on their
  insertion order, providing predictable iteration order and constant-time performance for basic operations.
- **152 . What is a TreeSet? How is different from a HashSet?** \
  `TreeSet` is a class in Java that implements the `SortedSet` interface using a red-black tree data structure.
  `TreeSet`
  maintains the order of elements based on their natural ordering or a custom comparator, allowing elements to be sorted
  in a specific order. Unlike `HashSet`, which does not maintain the order of elements, `TreeSet` provides log-time
  performance for basic operations like adding, removing, and checking the presence of elements.

  Some key differences between `TreeSet` and `HashSet` include:
    - **Ordering**: `TreeSet` maintains the order of elements based on their natural ordering or a custom comparator,
      allowing elements to be sorted in a specific order. `HashSet` does not maintain the order of elements and does
      not provide any guarantees about the order in which elements are stored.
    - **Underlying Data Structure**: `TreeSet` uses a red-black tree data structure to maintain the order of elements,
      while `HashSet` uses a hash table data structure. This tree structure allows `TreeSet` to provide log-time
      performance for maintaining the order of elements.

  In summary, `TreeSet` is a tree-based set implementation that maintains the order of elements based on their natural
  ordering or a custom comparator, providing efficient sorting and range query operations. `HashSet` is a hash-based set
  implementation with no ordering guarantees.
- **153 . Can you give examples of implementations of navigableSet?** \
  The `NavigableSet` interface in Java is implemented by the `TreeSet` and `ConcurrentSkipListSet` classes in the Java
  Collections Framework. These classes provide implementations of navigable sets that support navigation methods for
  accessing elements in a set. Some examples of implementations of `NavigableSet` include:

    - **TreeSet**: A class that implements the `NavigableSet` interface using a red-black tree data structure. `TreeSet`
      maintains the order of elements based on their natural ordering or a custom comparator and provides navigation
      methods for accessing elements in the set.
    - **ConcurrentSkipListSet**: A class that implements the `NavigableSet` interface using a skip list data structure.
      `ConcurrentSkipListSet` provides a scalable and concurrent implementation of a navigable set that supports
      efficient navigation and access to elements.

  These classes provide efficient and flexible implementations of navigable sets that allow elements to be accessed,
  added, and removed based on their order in the set.
- **154 . Explain briefly about Queue interface?** \
  The `Queue` interface in Java represents a collection of elements in a specific order for processing. Queues follow
  the First-In-First-Out (FIFO) order, meaning that elements are added to the end of the queue and removed from the
  front of the queue. The `Queue` interface provides methods for adding, removing, and accessing elements in the queue,
  as well as for checking the presence of elements.

  Some key features of the `Queue` interface include:
    - **FIFO Order**: Queues maintain the order in which elements are added and remove elements in the order they were
      added.
    - **Adding and Removing Elements**: Queues provide methods for adding elements to the end of the queue and removing
      elements from the front of the queue.
    - **Iterating Over Elements**: Queues can be iterated over using an iterator or enhanced for loop.
    - **Implementations**: The `Queue` interface is implemented by classes like `LinkedList`, `ArrayDeque`, and
      `PriorityQueue` in the Java Collections Framework.

  The `Queue` interface is commonly used to represent collections of elements that need to be processed in a specific
  order, such as tasks in a job queue or messages in a message queue. It provides a flexible and efficient way to work
  with queues of objects in Java.
- **155 . What are the important interfaces related to the Queue interface?** \
  The `Queue` interface in Java is related to several other interfaces in the Java Collections Framework that provide
  additional functionality for working with queues of elements. Some of the important interfaces related to the `Queue`
  interface include:

    - **Deque**: An interface that extends `Queue` and represents a double-ended queue that allows elements to be added
      or removed from both ends. Deques provide methods for adding, removing, and accessing elements at the front and
      back of the queue.
    - **BlockingQueue**: An interface that extends `Queue` and represents a queue that supports blocking operations for
      adding and removing elements. Blocking queues provide methods for waiting for elements to become available or
      space to become available in the queue.

  These interfaces build on the functionality provided by the `Queue` interface and offer additional features for
  working
  with queues of elements in Java.
- **156 . Explain about the Deque interface?** \
  The `Deque` interface in Java represents a double-ended queue that allows elements to be added or removed from both
  ends. Deques provide methods for adding, removing, and accessing elements at the front and back of the queue, making
  them suitable for a wide range of operations. The `Deque` interface extends the `Queue` interface and provides
  additional methods for working with double-ended queues.

  Some key features of the `Deque` interface include:
    - **Double-Ended Queue**: Deques allow elements to be added or removed from both the front and back of the queue.
    - **Adding and Removing Elements**: Deques provide methods for adding elements to the front and back of the queue
      and removing elements from the front and back.
    - **Iterating Over Elements**: Deques can be iterated over using an iterator or enhanced for loop.
    - **Implementations**: The `Deque` interface is implemented by classes like `ArrayDeque` and `LinkedList` in the
      Java
      Collections Framework.

  The `Deque` interface is commonly used to represent double-ended queues that require efficient insertion and removal
  of elements at both ends. It provides a flexible and efficient way to work with double-ended queues of objects in
  Java.
- **157 . Explain the BlockingQueue interface?** \
  The `BlockingQueue` interface in Java represents a queue that supports blocking operations for adding and removing
  elements. Blocking queues provide methods for waiting for elements to become available or space to become available in
  the queue, allowing threads to block until the desired condition is met. The `BlockingQueue` interface extends the
  `Queue` interface and provides additional methods for blocking operations.

  Some key features of the `BlockingQueue` interface include:
    - **Blocking Operations**: Blocking queues support blocking operations for adding and removing elements, allowing
      threads to wait until the desired condition is met.
    - **Waiting for Elements**: Blocking queues provide methods for waiting for elements to become available in the
      queue, ensuring that threads can block until elements are ready to be processed.
    - **Waiting for Space**: Blocking queues also provide methods for waiting for space to become available in the
      queue,
      allowing threads to block until there is room to add new elements.
    - **Implementations**: The `BlockingQueue` interface is implemented by classes like `ArrayBlockingQueue`,
      `LinkedBlockingQueue`, and `PriorityBlockingQueue` in the Java Collections Framework.

  The `BlockingQueue` interface is commonly used in multi-threaded applications to coordinate the processing of elements
  between producer and consumer threads. It provides a flexible and efficient way to work with blocking queues of
  objects in Java.
- **158 . What is a priorityQueue? How is it different from a normal queue?** \
  `PriorityQueue` is a class in Java that implements the `Queue` interface using a priority heap data structure. Unlike
  a normal queue, which follows the First-In-First-Out (FIFO) order, a `PriorityQueue` maintains elements in a priority
  order based on their natural ordering or a custom comparator. Elements with higher priority are dequeued before
  elements with lower priority.

  Some key differences between `PriorityQueue` and a normal queue include:
    - **Ordering**: `PriorityQueue` maintains elements in a priority order based on their natural ordering or a custom
      comparator, while a normal queue follows the FIFO order.
    - **Priority-Based Dequeue**: `PriorityQueue` dequeues elements based on their priority, with higher priority
      elements
      dequeued before lower priority elements. A normal queue dequeues elements in the order they were added.
    - **Underlying Data Structure**: `PriorityQueue` uses a priority heap data structure to maintain the order of
      elements,
      while a normal queue uses a different data structure like an array or linked list.

  In summary, `PriorityQueue` is a priority-based queue implementation that maintains elements in a priority order,
  while
  a normal queue follows the FIFO order. `PriorityQueue` is commonly used in applications that require elements to be
  processed based on their priority level.
- **159 . Can you give example implementations of the BlockingQueue interface?** \
  The `BlockingQueue` interface in Java is implemented by several classes in the Java Collections Framework that provide
  different implementations of blocking queues. Some examples of implementations of `BlockingQueue` include:

    - **ArrayBlockingQueue**: A class that implements the `BlockingQueue` interface using an array-based data structure.
      `ArrayBlockingQueue` provides a fixed-size blocking queue that supports blocking operations for adding and
      removing
      elements.
    - **LinkedBlockingQueue**: A class that implements the `BlockingQueue` interface using a linked list data structure.
      `LinkedBlockingQueue` provides an unbounded blocking queue that supports blocking operations for adding and
      removing
      elements.
    - **PriorityBlockingQueue**: A class that implements the `BlockingQueue` interface using a priority heap data
      structure.
      `PriorityBlockingQueue` provides a priority-based blocking queue that maintains elements in a priority order.

  These classes provide different implementations of blocking queues with varying characteristics and performance
  guarantees. They are commonly used in multi-threaded applications to coordinate the processing of elements between
  producer and consumer threads.
- **160 . Can you briefly explain about the Map interface?** \
  The `Map` interface in Java represents a collection of key-value pairs where each key is unique and maps to a single
  value. Maps provide methods for adding, removing, and accessing key-value pairs, as well as for checking the presence
  of keys or values. The `Map` interface does not extend the `Collection` interface and provides a separate set of
  methods for working with key-value pairs.

  Some key features of the `Map` interface include:
    - **Key-Value Pairs**: Maps store key-value pairs, allowing values to be associated with unique keys.
    - **Unique Keys**: Keys in a map are unique, meaning that each key maps to a single value.
    - **Adding and Removing Entries**: Maps provide methods for adding, removing, and updating key-value pairs.
    - **Iterating Over Entries**: Maps can be iterated over using an iterator or enhanced for loop to access key-value
      pairs.
    - **Implementations**: The `Map` interface is implemented by classes like `HashMap`, `TreeMap`, and `LinkedHashMap`
      in the Java Collections Framework.

  The `Map` interface is commonly used to store and manipulate key-value pairs in Java, providing a flexible and
  efficient
  way to work with mappings of objects.
- **161 . What is difference between Map and SortedMap?** \
  The `Map` and `SortedMap` interfaces in Java are related interfaces in the Java Collections Framework that represent
  collections of key-value pairs. The main difference between `Map` and `SortedMap` is the ordering of keys:

    - **Map**: The `Map` interface does not maintain the order of keys and does not provide any guarantees about the
      order in which keys are stored. Maps are typically implemented using hash-based data structures like `HashMap` and
      `LinkedHashMap`.
    - **SortedMap**: The `SortedMap` interface extends `Map` and represents a map of key-value pairs sorted in a
      specific
      order. Sorted maps maintain the order of keys based on their natural ordering or a custom comparator. Common
      implementations of `SortedMap` include `TreeMap` and `ConcurrentSkipListMap`.

  In summary, `Map` is a general interface for collections of key-value pairs, while `SortedMap` is a specialized
  interface for maps that maintain the order of keys based on a specific ordering.
- **162 . What is a HashMap? How is it different from a TreeMap?** \
  `HashMap` and `TreeMap` are two common implementations of the `Map` interface in Java that provide different
  characteristics for working with key-value pairs. The main differences between `HashMap` and `TreeMap` include:

    - **Underlying Data Structure**: `HashMap` uses a hash table data structure to store key-value pairs, providing
      constant-time performance for basic operations like adding, removing, and accessing entries. `TreeMap` uses a
      red-black
      tree data structure to maintain the order of keys based on their natural ordering or a custom comparator.
    - **Ordering**: `HashMap` does not maintain the order of keys and does not provide any guarantees about the order in
      which keys are stored. `TreeMap` maintains the order of keys based on their natural ordering or a custom
      comparator,
      allowing keys to be sorted in a specific order.
    - **Performance**: `HashMap` provides constant-time performance for basic operations, making it efficient for
      adding,
      removing, and accessing entries. `TreeMap` provides log-time performance for basic operations, making it efficient
      for maintaining the order of keys and performing range queries.

  In summary, `HashMap` is a hash-based map implementation with no ordering guarantees, while `TreeMap` is a tree-based
  map implementation that maintains the order of keys based on their natural ordering or a custom comparator. `HashMap`
  is commonly used in applications that require fast access to key-value pairs, while `TreeMap` is used when keys need
  to be sorted in a specific order.
- **163 . What are the different methods in a Hash Map?** \
  The `HashMap` class in Java provides a variety of methods for working with key-value pairs stored in a hash table
  data structure. Some of the common methods provided by the `HashMap` class include:

    - **`put(key, value)`**: Adds a key-value pair to the map, replacing the existing value if the key is already
      present.
    - **`get(key)`**: Retrieves the value associated with the specified key, or `null` if the key is not present.
    - **`containsKey(key)`**: Checks if the map contains the specified key.
    - **`containsValue(value)`**: Checks if the map contains the specified value.
    - **`remove(key)`**: Removes the key-value pair associated with the specified key from the map.
    - **`size()`**: Returns the number of key-value pairs in the map.
    - **`isEmpty()`**: Checks if the map is empty.
    - **`keySet()`**: Returns a set of all keys in the map.
    - **`values()`**: Returns a collection of all values in the map.
    - **`entrySet()`**: Returns a set of key-value pairs in the map.

  These methods provide a flexible and efficient way to work with key-value pairs stored in a `HashMap` in Java.
    - **164 . What is a TreeMap? How is different from a HashMap?** \
      `TreeMap` is a class in Java that implements the `SortedMap` interface using a red-black tree data structure.
      `TreeMap`
      maintains the order of keys based on their natural ordering or a custom comparator, allowing keys to be sorted in
      a
      specific order. Unlike `HashMap`, which does not maintain the order of keys, `TreeMap` provides log-time
      performance
      for basic operations like adding, removing, and accessing entries.

      Some key differences between `TreeMap` and `HashMap` include:
        - **Underlying Data Structure**: `TreeMap` uses a red-black tree data structure to maintain the order of keys,
          while
          `HashMap` uses a hash table data structure. This tree structure allows `TreeMap` to provide log-time
          performance
          for maintaining the order of keys.
        - **Ordering**: `TreeMap` maintains the order of keys based on their natural ordering or a custom comparator,
          allowing keys to be sorted in a specific order. `HashMap` does not maintain the order of keys and does not
          provide
          any guarantees about the order in which keys are stored.
        - **Performance**: `TreeMap` provides log-time performance for basic operations, making it efficient for
          maintaining
          the order of keys and performing range queries. `HashMap` provides constant-time performance for basic
          operations,
          making it efficient for adding, removing, and accessing entries.

      In summary, `TreeMap` is a tree-based map implementation that maintains the order of keys based on their natural
      ordering or a custom comparator, while `HashMap` is a hash-based map implementation with no ordering guarantees.
      `TreeMap` is commonly used in applications that require keys to be sorted in a specific order. `HashMap` is used
      when a fast access to key-value pairs is required.
- **165 . Can you give an example of implementation of NavigableMap interface?** \
  The `NavigableMap` interface in Java is implemented by the `TreeMap` class in the Java Collections Framework.
  `TreeMap`
  provides a navigable map of key-value pairs sorted in a specific order, allowing elements to be accessed, added, and
  removed based on their order in the map. Here is an example of using `TreeMap` to implement a `NavigableMap`:

    ```java
    import java.util.NavigableMap;
    import java.util.TreeMap;

    public class NavigableMapExample {
        public static void main(String[] args) {
            // Create a NavigableMap using TreeMap
            NavigableMap<Integer, String> map = new TreeMap<>();

            // Add key-value pairs to the map
            map.put(1, "One");
            map.put(2, "Two");
            map.put(3, "Three");
            map.put(4, "Four");
            map.put(5, "Five");

            // Print the key-value pairs in ascending order
            System.out.println("Ascending Order:");
            for (Integer key : map.keySet()) {
                System.out.println(key + " - " + map.get(key));
            }

            // Print the key-value pairs in descending order
            System.out.println("Descending Order:");
            for (Integer key : map.descendingKeySet()) {
                System.out.println(key + " - " + map.get(key));
            }
        }
    }
    ```

  In this example, a `NavigableMap` is created using a `TreeMap` and key-value pairs are added to the map. The key-value
  pairs are then printed in ascending order and descending order using the `keySet` and `descendingKeySet` methods of
  the `NavigableMap` interface.
- **166 . What are the static methods present in the collections class?** \
  The `Collections` class in Java provides a variety of static methods for working with collections in the Java
  Collections Framework. Some of the common static methods provided by the `Collections` class include:

    - **`sort(List<T> list)`**: Sorts the elements in the specified list in ascending order.
    - **`reverse(List<?> list)`**: Reverses the order of elements in the specified list.
    - **`shuffle(List<?> list)`**: Randomly shuffles the elements in the specified list.
    - **`binarySearch(List<? extends Comparable<? super T>> list, T key)`**: Searches for the specified key in the
      specified list using a binary search algorithm.
    - **`unmodifiableCollection(Collection<? extends T> c)`**: Returns an unmodifiable view of the specified collection.
    - **`synchronizedCollection(Collection<T> c)`**: Returns a synchronized (thread-safe) view of the specified
      collection.
    - **`singleton(T o)`**: Returns an immutable set containing only the specified object.
    - **`emptyList()`**: Returns an empty list.
    - **`emptySet()`**: Returns an empty set.
    - **`emptyMap()`**: Returns an empty map.

  These static methods provide a convenient way to perform common operations on collections in Java.

### Advanced collections

- **167 . What is the difference between synchronized and concurrent collections in Java?** \
  Synchronized collections and concurrent collections in Java are two approaches to handling thread safety in
  multi-threaded applications. The main difference between synchronized and concurrent collections is how they achieve
  thread safety:

    - **Synchronized Collections**: Synchronized collections use explicit synchronization to make the collection
      thread-safe. This is typically done by wrapping the collection with synchronized blocks or using synchronized
      methods to ensure that only one thread can access the collection at a time. Synchronized collections are
      synchronized at the collection level, meaning that all operations on the collection are synchronized.
    - **Concurrent Collections**: Concurrent collections use non-blocking algorithms and data structures to achieve
      thread safety. Concurrent collections are designed to be thread-safe without the need for explicit
      synchronization.
      They use techniques like compare-and-swap (CAS) operations and lock-free algorithms to allow multiple threads to
      access the collection concurrently.

  Some key differences between synchronized and concurrent collections include:
    - **Performance**: Synchronized collections can be slower than concurrent collections due to the overhead of
      explicit
      synchronization. Concurrent collections are designed for high concurrency and can provide better performance in
      multi-threaded applications.
    - **Scalability**: Concurrent collections are more scalable than synchronized collections because they allow
      multiple
      threads to access the collection concurrently. Synchronized collections can suffer from contention and bottlenecks
      when multiple threads access the collection.
    - **Ease of Use**: Synchronized collections require explicit synchronization, which can be error-prone and complex.
      Concurrent collections provide built-in thread safety and are easier to use in multi-threaded applications.

  In general, concurrent collections are preferred for high-concurrency scenarios where performance and scalability are
  important. Synchronized collections are suitable for simpler applications where thread safety is required but
  high-concurrency is not a concern.
- **168 . Explain about the new concurrent collections in Java?** \
  Java provides a set of concurrent collections in the `java.util.concurrent` package that are designed for high
  concurrency and thread safety in multi-threaded applications. Some of the new concurrent collections introduced in
  Java include:

    - **`ConcurrentHashMap`**: A hash table-based map implementation that provides thread-safe access to key-value
      pairs.
      `ConcurrentHashMap` allows multiple threads to read and write to the map concurrently without the need for
      explicit
      synchronization.
    - **`ConcurrentSkipListMap`**: A skip list-based map implementation that provides thread-safe access to key-value
      pairs. `ConcurrentSkipListMap` maintains the order of keys and allows multiple threads to access the map
      concurrently.
    - **`ConcurrentLinkedQueue`**: A linked list-based queue implementation that provides thread-safe access to
      elements.
      `ConcurrentLinkedQueue` allows multiple threads to add and remove elements from the queue concurrently.
    - **`ConcurrentLinkedDeque`**: A linked list-based double-ended queue implementation that provides thread-safe
      access
      to elements at both ends. `ConcurrentLinkedDeque` allows multiple threads to add and remove elements from the
      front
      and back of the queue concurrently.

  These concurrent collections are designed to be highly scalable and efficient in multi-threaded applications,
  providing
  built-in thread safety and high concurrency support. They are suitable for scenarios where multiple threads need to
  access and modify collections concurrently.
- **169 . Explain about copyOnWrite concurrent collections approach?** \
  The copy-on-write (COW) approach is a concurrency control technique used in Java to provide thread-safe access to
  collections. In the copy-on-write approach, a new copy of the collection is created whenever a modification is made,
  ensuring that the original collection remains unchanged and can be safely accessed by other threads. This approach
  eliminates the need for explicit synchronization and provides high concurrency and thread safety.

  Some key features of the copy-on-write approach include:
    - **Immutable Collections**: The copy-on-write approach uses immutable collections to ensure that the original
      collection is not modified when a write operation is performed. This allows multiple threads to read from the
      collection concurrently without the risk of data corruption.
    - **Copy on Write**: When a modification is made to the collection, a new copy of the collection is created with the
      updated elements. This copy is then made visible to other threads, ensuring that modifications are isolated and
      do not affect other threads.
    - **Read-Heavy Workloads**: The copy-on-write approach is well-suited for scenarios where reads are more frequent
      than writes. It provides efficient read access to collections and minimizes contention between threads.

  The copy-on-write approach is commonly used in scenarios where high concurrency and thread safety are required, such
  as in read-heavy workloads or applications with multiple readers and few writers. It provides a simple and efficient
  way to achieve thread safety without the need for explicit synchronization.
- **170 . What is compareAndSwap approach?** \
  The compare-and-swap (CAS) operation is an atomic operation used in concurrent programming to implement lock-free
  algorithms and data structures. The CAS operation allows a thread to update a value in memory if it matches an
  expected
  value, ensuring that the update is performed atomically without the need for explicit synchronization.

  The CAS operation typically consists of three steps:
    - **Read**: The current value of the memory location is read.
    - **Compare**: The current value is compared with an expected value.
    - **Swap**: If the current value matches the expected value, a new value is written to the memory location.

  The CAS operation is commonly used in concurrent collections and data structures to implement lock-free algorithms
  that allow multiple threads to access and modify shared data without the risk of data corruption or lost updates. CAS
  is a key building block for implementing efficient and scalable concurrent algorithms in Java and other programming
  languages.
- **171 . What is a lock? How is it different from using synchronized approach?** \
  A lock is a synchronization mechanism used in Java to control access to shared resources in multi-threaded
  applications. Locks provide a way to coordinate the execution of threads and ensure that only one thread can access a
  shared resource at a time. Locks are more flexible and powerful than the `synchronized` keyword in Java and provide
  additional features for managing concurrency.

  Some key differences between locks and the `synchronized` approach include:
    - **Explicit Control**: Locks provide explicit control over locking and unlocking operations, allowing threads to
      acquire and release locks at specific points in the code. The `synchronized` keyword automatically acquires and
      releases locks based on synchronized blocks or methods.
    - **Reentrant Locking**: Locks support reentrant locking, meaning that a thread can acquire the same lock multiple
      times without deadlocking. The `synchronized` keyword does not support reentrant locking.
    - **Condition Variables**: Locks provide condition variables that allow threads to wait for specific conditions to
      be met before proceeding. Condition variables are not available with the `synchronized` keyword.
    - **Fairness**: Locks can be configured to provide fairness in thread scheduling, ensuring that threads are granted
      access to the lock in the order they requested it. The `synchronized` keyword does not provide fairness
      guarantees.

  In general, locks are more flexible and powerful than the `synchronized` keyword and provide additional features for
  managing concurrency in multi-threaded applications. Locks are commonly used in scenarios where fine-grained control
  over synchronization is required or when additional features like reentrant locking or condition variables are needed.
- **172 . What is initial capacity of a Java collection?** \
  The initial capacity of a Java collection refers to the number of elements that the collection can initially store
  before resizing is required. When a collection is created, an initial capacity is specified to allocate memory for
  storing elements. If the number of elements exceeds the initial capacity, the collection is resized to accommodate
  additional elements.

  The initial capacity of a collection is typically set when the collection is created using a constructor that accepts
  an initial capacity parameter. For example, the `ArrayList` class in Java has a constructor that allows an initial
  capacity to be specified:

    ```java
    List<String> list = new ArrayList<>(10);
    ```

  In this example, an `ArrayList` is created with an initial capacity of 10 elements. This means that the `ArrayList`
  can store up to 10 elements before resizing is required. Setting an appropriate initial capacity can help improve
  performance by reducing the number of resize operations and memory allocations needed as elements are added to the
  collection.
- **173 . What is load factor?** \
  The load factor of a Java collection is a value that determines when the collection should be resized to accommodate
  additional elements. The load factor is used in hash-based collections like `HashMap` and `HashSet` to control the
  number of elements that can be stored in the collection before resizing is required. When the number of elements in
  the collection exceeds the load factor multiplied by the current capacity, the collection is resized to increase its
  capacity.

  The load factor is typically a value between 0 and 1, representing a percentage of the current capacity at which the
  collection should be resized. For example, a load factor of 0.75 means that the collection should be resized when it
  is 75% full. Resizing the collection allows it to accommodate additional elements and maintain efficient performance
  for adding, removing, and accessing elements.

  The load factor is an important parameter in hash-based collections to balance memory usage and performance. Setting
  an appropriate load factor can help optimize the performance of the collection by reducing the frequency of resize
  operations and ensuring that the collection remains efficient as elements are added and removed.
- **174 . When does a Java collection throw `UnsupportedOperationException`?** \
  A Java collection throws an `UnsupportedOperationException` when an operation is not supported by the collection. This
  exception is typically thrown when an attempt is made to modify an immutable or read-only collection, or when an
  operation is not implemented by the specific collection implementation.

  Some common scenarios where a `UnsupportedOperationException` may be thrown include:
    - **Modifying an Immutable Collection**: Attempting to add, remove, or modify elements in an immutable collection
      like
      `Collections.unmodifiableList` or `Collections.unmodifiableMap` will result in an `UnsupportedOperationException`.
    - **Unsupported Operations**: Some collection implementations do not support certain operations, such as adding or
      removing elements, and will throw an `UnsupportedOperationException` if these operations are attempted.
    - **Read-Only Views**: Collections that provide read-only views of other collections may throw an
      `UnsupportedOperationException` if modification operations are attempted on the read-only view.

  The `UnsupportedOperationException` is a runtime exception that indicates that an operation is not supported by the
  collection. It is typically thrown to prevent modifications to collections that are intended to be read-only or
  immutable.
- **175 . What is difference between fail-safe and fail-fast iterators?** \
  Fail-safe and fail-fast iterators are two different approaches to handling concurrent modifications to collections in
  Java. The main difference between fail-safe and fail-fast iterators is how they respond to modifications made to a
  collection while iterating over it:

    - **Fail-Safe Iterators**: Fail-safe iterators make a copy of the collection when it is created and iterate over
      the
      copy rather than the original collection. This ensures that the iterator is not affected by modifications made to
      the collection during iteration. Fail-safe iterators do not throw `ConcurrentModificationException` and provide a
      consistent view of the collection.
    - **Fail-Fast Iterators**: Fail-fast iterators detect concurrent modifications to the collection while iterating and
      throw a `ConcurrentModificationException` to indicate that the collection has been modified. Fail-fast iterators
      provide immediate feedback when a concurrent modification occurs and help prevent data corruption or
      inconsistencies.

  In general, fail-safe iterators are used in concurrent collections like `ConcurrentHashMap` and
  `ConcurrentSkipListMap`
  to provide a consistent view of the collection during iteration. Fail-fast iterators are used in non-concurrent
  collections like `ArrayList` and `HashMap` to detect and prevent concurrent modifications that could lead to data
  corruption. The choice between fail-safe and fail-fast iterators depends on the requirements of the application and
  the level of concurrency expected.
- **176 . What are atomic operations in Java?** \
  Atomic operations in Java are operations that are performed atomically, meaning that they are indivisible and
  uninterruptible. Atomic operations are used in concurrent programming to ensure that shared data is accessed and
  modified safely by multiple threads without the risk of data corruption or lost updates. Java provides a set of
  atomic classes and operations in the `java.util.concurrent.atomic` package to support atomic operations.

  Some common atomic operations in Java include:
    - **AtomicInteger**: Provides atomic operations on integer values, such as `get`, `set`, `incrementAndGet`, and
      `compareAndSet`.
    - **AtomicLong**: Provides atomic operations on long values, such as `get`, `set`, `incrementAndGet`, and
      `compareAndSet`.
    - **AtomicReference**: Provides atomic operations on object references, such as `get`, `set`, and `compareAndSet`.
    - **AtomicBoolean**: Provides atomic operations on boolean values, such as `get`, `set`, and `compareAndSet`.

  Atomic operations are commonly used in multi-threaded applications to ensure that shared data is accessed and modified
  safely by multiple threads. They provide a simple and efficient way to implement lock-free algorithms and data
  structures that require atomicity and thread safety.
- **177 . What is BlockingQueue in Java?** \
  A `BlockingQueue` in Java is a type of queue that supports blocking operations for adding and removing elements. A
  blocking queue provides methods for waiting for elements to become available or space to become available in the
  queue, allowing threads to block until the desired condition is met. Blocking queues are commonly used in
  multi-threaded applications to coordinate the processing of elements between producer and consumer threads.

  Some key features of a `BlockingQueue` include:
    - **Blocking Operations**: Blocking queues support blocking operations for adding and removing elements, allowing
      threads to wait until the desired condition is met.
    - **Waiting for Elements**: Blocking queues provide methods for waiting for elements to become available in the
      queue, ensuring that threads can block until elements are ready to be processed.
    - **Waiting for Space**: Blocking queues also provide methods for waiting for space to become available in the
      queue, allowing threads to block until there is room to add new elements.
    - **Thread Safety**: Blocking queues are thread-safe data structures that provide built-in support for
      synchronization and coordination between threads.

  Blocking queues are commonly used in scenarios where multiple threads need to coordinate the processing of elements
  in a queue. They provide a flexible and efficient way to work with queues of objects in Java.

### Generics

- **178 . What are Generics? Why do we need Generics?** \
  Generics in Java are a feature that allows classes and methods to be parameterized by one or more types. Generics
  provide a way to create reusable and type-safe code by allowing classes and methods to work with generic types that
  are specified at compile time. Generics enable the creation of classes, interfaces, and methods that can work with
  different types without sacrificing type safety.

  Some key reasons for using generics in Java include:
    - **Type Safety**: Generics provide compile-time type checking, ensuring that the correct types are used in
      classes and methods. This helps prevent runtime errors and improves code reliability.
    - **Code Reusability**: Generics allow classes and methods to be parameterized by types, making them more
      flexible and reusable. This reduces code duplication and improves maintainability.
    - **Performance**: Generics can improve performance by avoiding the need for type casting and providing
      compile-time optimizations. This can lead to faster and more efficient code.

  Generics are an important feature of the Java language that provide a way to create flexible, reusable, and
  type-safe code. They are commonly used in collections, data structures, and algorithms to work with generic types
  and improve code quality.
- **179 . Why do we need Generics? Can you give an example of how Generics make a program more flexible?** \
  Generics in Java are a feature that allows classes and methods to be parameterized by one or more types. Generics
  provide a way to create reusable and type-safe code by allowing classes and methods to work with generic types that
  are specified at compile time. Generics enable the creation of classes, interfaces, and methods that can work with
  different types without sacrificing type safety.

  Generics make a program more flexible by allowing classes and methods to work with generic types that are specified
  at compile time. This flexibility allows code to be written in a generic and reusable way, reducing code duplication
  and improving maintainability. For example, consider a generic `Pair` class that can store a pair of values of any
  type:

    ```java
    public class Pair<T, U> {
        private T first;
        private U second;

        public Pair(T first, U second) {
            this.first = first;
            this.second = second;
        }

        public T getFirst() {
            return first;
        }

        public U getSecond() {
            return second;
        }

        public static void main(String[] args) {
            Pair<String, Integer> pair1 = new Pair<>("Hello", 42);
            Pair<Integer, Double> pair2 = new Pair<>(123, 3.14);

            System.out.println(pair1.getFirst() + " " + pair1.getSecond());
            System.out.println(pair2.getFirst() + " " + pair2.getSecond());
        }
    }
    ```

  In this example, a generic `Pair` class is created that can store a pair of values of any type. The `Pair` class is
  parameterized by two types `T` and `U`, allowing it to work with different types of values. This flexibility makes
  the `Pair` class more generic and reusable, allowing it to store pairs of values of different types without
  sacrificing type safety.
- **180 . How do you declare a generic class?** \
  A generic class in Java is declared by specifying one or more type parameters in angle brackets (`<>`) after the class
  name. The type parameters are used to represent generic types that can be specified at compile time when creating
  instances of the class. Here is an example of declaring a generic class in Java:

    ```java
    public class Box<T> {
        private T value;

        public Box(T value) {
            this.value = value;
        }

        public T getValue() {
            return value;
        }

        public static void main(String[] args) {
            Box<String> box1 = new Box<>("Hello");
            Box<Integer> box2 = new Box<>(42);

            System.out.println(box1.getValue());
            System.out.println(box2.getValue());
        }
    }
    ```

  In this example, a generic `Box` class is declared with a type parameter `T`. The `Box` class can store a value of any
  type specified by the type parameter `T`. Instances of the `Box` class are created by specifying the type parameter
  when creating the instance, such as `Box<String>` or `Box<Integer`. This allows the `Box` class to work with different
  types of values while maintaining type safety.
- **181 . What are the restrictions in using generic type that is declared in a class declaration?** \
  When using a generic type that is declared in a class declaration, there are some restrictions and limitations that
  must be considered:

    - **Type Erasure**: Generics in Java use type erasure, which means that the actual type information is erased at
      compile time and is not available at runtime. This can lead to limitations in working with generic types, such as
      not being able to create instances of generic types directly or access the type information at runtime.
    - **Type Bounds**: Generic types can be bounded by specifying upper bounds, lower bounds, or multiple bounds. These
      bounds restrict the types that can be used with the generic type and provide compile-time type checking to ensure
      type safety.
    - **Type Inference**: Java supports type inference for generic types, allowing the compiler to infer the type
      arguments based on the context. This can help reduce the need for explicit type declarations and make code more
      concise and readable.
    - **Type Compatibility**: Generic types must be compatible with the specified type arguments, ensuring that the
      types used with the generic type are consistent and compatible with the declared type parameters.

  These restrictions and limitations help ensure type safety and consistency when working with generic types in Java.
- **182 . How can we restrict Generics to a subclass of particular class?** \
  In Java, it is possible to restrict generics to a subclass of a particular class by using bounded type parameters. By
  specifying an upper bound for the generic type parameter, you can restrict the types that can be used with the generic
  class to subclasses of a specific class. Here is an example of restricting generics to a subclass of a particular
  class:

    ```java
    public class Box<T extends Number> {
        private T value;

        public Box(T value) {
            this.value = value;
        }

        public T getValue() {
            return value;
        }

        public static void main(String[] args) {
            Box<Integer> box1 = new Box<>(42);
            Box<Double> box2 = new Box<>(3.14);
            // Box<String> box3 = new Box<>("Hello"); // Compilation error
        }
    }
    ```

  In this example, the `Box` class is declared with a type parameter `T` that is bounded by `Number`. This means that
  the generic type `T` must be a subclass of `Number`, such as `Integer`, `Double`, or `Float`. Instances of the `Box`
  class can be created with types that are subclasses of `Number`, but not with types that are not subclasses of
  `Number`.
- **183 . How can we restrict Generics to a super class of particular class?** \
  In Java, it is possible to restrict generics to a super class of a particular class by using bounded type parameters.
  By specifying a lower bound for the generic type parameter, you can restrict the types that can be used with the
  generic class to superclasses of a specific class. Here is an example of restricting generics to a superclass of a
  particular class:

    ```java
    public class Box<T super Integer> {
        private T value;

        public Box(T value) {
            this.value = value;
        }

        public T getValue() {
            return value;
        }

        public static void main(String[] args) {
            Box<Integer> box1 = new Box<>(42);
            Box<Object> box2 = new Box<>("Hello");
            // Box<String> box3 = new Box<>("Hello"); // Compilation error
        }
    }
    ```

  In this example, the `Box` class is declared with a type parameter `T` that is bounded by `super Number`. This means
  that the generic type `T` must be a superclass of `Number`, such as `Object` or `Serializable`. Instances of the
  `Box` class can be created with types that are superclasses of `Number`, but not with types that are not superclasses
  of `Number`.
- **184 . Can you give an example of a generic method?** \
  A generic method in Java is a method that is parameterized by one or more types. Generic methods provide a way to
  create methods that can work with different types of arguments without sacrificing type safety. Here is an example of
  a generic method that swaps the elements of an array:

    ```java
    public class ArrayUtils {
        public static <T> void swap(T[] array, int i, int j) {
            T temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }

        public static void main(String[] args) {
            Integer[] numbers = {1, 2, 3, 4, 5};
            swap(numbers, 0, 4);

            for (Integer number : numbers) {
                System.out.print(number + " ");
            }
        }
    }
    ```

  In this example, the `swap` method is declared as a generic method with a type parameter `T`. The `swap` method takes
  an array of type `T`, along with two indices `i` and `j`, and swaps the elements at the specified indices. The
  `swap` method can work with arrays of any type, allowing elements to be swapped in a type-safe way.

### Multi threading

- **185 . What is the need for threads in Java?** \
  Threads in Java are used to achieve concurrent execution of tasks within a single process. Threads allow multiple
  operations to be performed simultaneously, enabling applications to take advantage of multi-core processors and
  improve performance. Threads are lightweight processes that share the same memory space and resources of a process,
  allowing them to run concurrently and perform tasks in parallel.

  Some key reasons for using threads in Java include:
    - **Concurrency**: Threads enable multiple tasks to be executed concurrently, improving performance and
      responsiveness
      of applications.
    - **Parallelism**: Threads allow tasks to be executed
- **186 . How do you create a thread?** \
  There are two main ways to create a thread in Java:
    - **Extending the `Thread` class**: You can create a thread by extending the `Thread` class and overriding the
      `run` method. This approach allows you to define the behavior of the thread by implementing the `run` method.
    - **Implementing the `Runnable` interface**: You can create a thread by implementing the `Runnable` interface and
      passing an instance of the class to the `Thread` constructor. This approach separates the thread logic from the
      class definition and allows for better code reusability.

  Here is an example of creating a thread by extending the `Thread` class:

    ```java
    public class MyThread extends Thread {
        @Override
        public void run() {
            System.out.println("Hello from a thread!");
        }

        public static void main(String[] args) {
            MyThread thread = new MyThread();
            thread.start();
        }
    }
    ```

  In this example, a `MyThread` class is created by extending the `Thread` class and overriding the `run` method. An
  instance of the `MyThread` class is then created, and the `start` method is called to start the thread.

  Here is an example of creating a thread by implementing the `Runnable` interface:

    ```java
    public class MyRunnable implements Runnable {
        @Override
        public void run() {
            System.out.println("Hello from a thread!");
        }

        public static void main(String[] args) {
            MyRunnable runnable = new MyRunnable();
            Thread thread = new Thread(runnable);
            thread.start();
        }
    }
    ```

  In this example, a `MyRunnable` class is created by implementing the `Runnable` interface and defining the `run`
  method. An instance of the `MyRunnable` class is then passed to the `Thread` constructor, and the `start` method is
  called to start the thread.
- **187 . How do you create a thread by extending thread class?** \
  You can create a thread in Java by extending the `Thread` class and overriding the `run` method. This approach allows
  you to define the behavior of the thread by implementing the `run` method. Here is an example:

    ```java
    public class MyThread extends Thread {
        @Override
        public void run() {
            System.out.println("Hello from a thread!");
        }

        public static void main(String[] args) {
            MyThread thread = new MyThread();
            thread.start();
        }
    }
    ```

  In this example, a `MyThread` class is created by extending the `Thread` class and overriding the `run` method. An
  instance of the `MyThread` class is then created, and the `start` method is called to start the thread.
- **188 . How do you create a thread by implementing runnable interface?** \
  You can create a thread in Java by implementing the `Runnable` interface and passing an instance of the class to the
  `Thread` constructor. This approach separates the thread logic from the class definition and allows for better code
  reusability. Here is an example:

    ```java
    public class MyRunnable implements Runnable {
        @Override
        public void run() {
            System.out.println("Hello from a thread!");
        }

        public static void main(String[] args) {
            MyRunnable runnable = new MyRunnable();
            Thread thread = new Thread(runnable);
            thread.start();
        }
    }
    ```

  In this example, a `MyRunnable` class is created by implementing the `Runnable` interface and defining the `run`
  method. An instance of the `MyRunnable` class is then passed to the `Thread` constructor, and the `start` method is
  called to start the thread.
- **189 . How do you run a thread in Java?** \
  There are two main ways to run a thread in Java:
    - **Extending the `Thread` class**: You can create a thread by extending the `Thread` class and overriding the `run`
      method. This approach allows you to define the behavior of the thread by implementing the `run` method. You can
      then
      create an instance of the class and call the `start` method to run the thread.
    - **Implementing the `Runnable` interface**: You can create a thread by implementing the `Runnable` interface and
      passing an instance of the class to the `Thread` constructor. This approach separates the thread logic from the
      class definition and allows for better code reusability. You can then create an instance of the class and call the
      `start` method to run the thread.

  Here is an example of running a thread by extending the `Thread` class:

    ```java
    public class MyThread extends Thread {
        @Override
        public void run() {
            System.out.println("Hello from a thread!");
        }

        public static void main(String[] args) {
            MyThread thread = new MyThread();
            thread.start();
        }
    }
    ```

  In this example, a `MyThread` class is created by extending the `Thread` class and overriding the `run` method. An
  instance of the `MyThread` class is then created, and the `start` method is called to run the thread.

  Here is an example of running a thread by implementing the `Runnable` interface:

    ```java
    public class MyRunnable implements Runnable {
        @Override
        public void run() {
            System.out.println("Hello from a thread!");
        }

        public static void main(String[] args) {
            MyRunnable runnable = new MyRunnable();
            Thread thread = new Thread(runnable);
            thread.start();
        }
    }
    ```

  In this example, a `MyRunnable` class is created by implementing the `Runnable` interface and defining the `run`
  method. An instance of the `MyRunnable` class is then passed to the `Thread` constructor, and the `start` method is
  called to run the thread.
- **190 . What are the different states of a thread?** \
  Threads in Java can be in different states during their lifecycle. The main states of a thread in Java are:
    - **New**: A thread is in the new state when it is created but has not yet started.
    - **Runnable**: A thread is in the runnable state when it is ready to run but is waiting for a processor to execute
    - **191 . What is priority of a thread? How do you change the priority of a thread?** \
      The priority of a thread in Java is an integer value that determines the scheduling priority of the thread.
      Threads
      with higher priority values are given preference by the thread scheduler and are more likely.
- **192 . What is ExecutorService?** \
  `ExecutorService` is an interface in the Java Concurrency API that provides a higher-level abstraction for managing
  and executing tasks asynchronously using a pool of threads. `ExecutorService` extends the `Executor` interface and
  provides additional methods for managing the lifecycle of the executor, submitting tasks for execution, and
  controlling
  the execution of tasks.

  Some key features of `ExecutorService` include:
    - **Task Execution**: `ExecutorService` allows you to submit tasks for execution using methods like `submit` and
      `invokeAll`.
    - **Thread Pool Management**: `ExecutorService` manages a pool of worker threads that can be reused for executing
      tasks.
    - **Asynchronous
- **193 . Can you give an example for ExecutorService?** \
  Here is an example of using `ExecutorService` to execute tasks asynchronously in Java:

    ```java
    import java.util.concurrent.ExecutorService;
    import java.util.concurrent.Executors;

    public class Main {
        public static void main(String[] args) {
            // Create an ExecutorService with a fixed thread pool size
            ExecutorService executor = Executors.newFixedThreadPool(2);

            // Submit tasks for execution
            executor.submit(() -> System.out.println("Task 1 executed by thread: " + Thread.currentThread().getName()));
            executor.submit(() -> System.out.println("Task 2 executed by thread: " + Thread.currentThread().getName()));

            // Shutdown the ExecutorService
            executor.shutdown();
        }
    }
    ```

  In this example, an `ExecutorService` is created with a fixed thread pool size of 2 using the
  `Executors.newFixedThreadPool`
  method. Two tasks are then submitted for execution using the `submit` method, and the tasks are executed
  asynchronously
  by the worker threads in the thread pool. Finally, the `ExecutorService` is shut down to release the resources.
- **194 . Explain different ways of creating executor services**. \
  There are several ways to create `ExecutorService` instances in Java using the `Executors` utility class. Some of the
  common ways to create `ExecutorService` instances include:
    - **`newFixedThreadPool(int nThreads)`**: Creates a fixed-size thread pool with the specified number of threads.
    - **`newCachedThreadPool()`**: Creates a thread pool that creates new threads as needed and reuses idle threads.
    - **`newSingleThreadExecutor()`**: Creates a single-threaded executor that uses a single worker thread to execute
      tasks sequentially.
    - **`newScheduledThreadPool(int corePoolSize)`**: Creates a thread pool that can schedule tasks to run after a
      specified delay or at a fixed rate.

  These methods provide different ways to create `ExecutorService` instances with varying thread pool configurations
  based on the requirements of the application.
- **195 . How do you check whether an ExecutionService task executed successfully?** \
  The `Future` interface in the Java Concurrency API provides a way to check whether an `ExecutorService` task executed
  successfully and retrieve the result of the task. The `Future` interface represents the result of an asynchronous
  computation and provides methods for checking the status of the task, waiting for the task to complete, and retrieving
  the result of the task.

  Here is an example of using `Future` to check whether an `ExecutorService` task executed successfully:

    ```java
    import java.util.concurrent.ExecutorService;
    import java.util.concurrent.Executors;
    import java.util.concurrent.Future;

    public class Main {
        public static void main(String[] args) {
            // Create an ExecutorService with a fixed thread pool size
            ExecutorService executor = Executors.newFixedThreadPool(2);

            // Submit a task for execution
            Future<String> future = executor.submit(() -> {
                Thread.sleep(2000);
                return "Task completed successfully";
            });

            // Check if the task is done
            if (future.isDone()) {
                try {
                    // Get the result of the task
                    String result = future.get();
                    System.out.println("Task result: " + result);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }

            // Shutdown the ExecutorService
            executor.shutdown();
        }
    }
    ```

  In this example, a task is submitted for execution using the `submit` method, which returns a `Future` representing
  the
  result of the task. The `isDone` method is used to check if the task has completed, and the `get` method is used to
  retrieve the result of the task. If the task is done, the result is printed to the console. Finally, the
  `ExecutorService` is shut down to release the resources.
- **196 . What is callable? How do you execute a callable from executionservice?** \
  `Callable` is a functional interface in the Java Concurrency API that represents a task that can be executed
  asynchronously and return a result. `Callable` is similar to `Runnable`, but it can return a result or throw an
  exception. The `Callable` interface defines a single method, `call`, that takes no arguments and returns a result of
  a specified type.

  Here is an example of executing a `Callable` from an `ExecutorService`:

    ```java
    import java.util.concurrent.Callable;
    import java.util.concurrent.ExecutorService;
    import java.util.concurrent.Executors;
    import java.util.concurrent.Future;

    public class Main {
        public static void main(String[] args) {
            // Create an ExecutorService with a fixed thread pool size
            ExecutorService executor = Executors.newFixedThreadPool(2);

            // Create a Callable task
            Callable<String> callable = () -> {
                Thread.sleep(2000);
                return "Task completed successfully";
            };

            // Submit the Callable task for execution
            Future<String> future = executor.submit(callable);

            // Check if the task is done
            if (future.isDone()) {
                try {
                    // Get the result of the task
                    String result = future.get();
                    System.out.println("Task result: " + result);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }

            // Shutdown the ExecutorService
            executor.shutdown();
        }
    }
    ```

  In this example, a `Callable` task is created using a lambda expression that sleeps for 2 seconds and returns a
  result.
  The `Callable` task is then submitted for execution using the `submit` method, which returns a `Future` representing
  the result of the task. The `isDone` method is used to check if the task has completed, and the `get` method is used
  to
  retrieve the result of the task. If the task is done, the result is printed to the console. Finally, the
  `ExecutorService` is shut down to release the resources.
- **197 . What is synchronization of threads?** \
  Synchronization in Java is a mechanism that allows multiple threads to coordinate access to shared resources.
- **198 . Can you give an example of a synchronized block?** \
  Here is an example of using a synchronized block in Java to synchronize access to a shared resource:

    ```java
    public class Counter {
        private int count = 0;

        public void increment() {
            synchronized (this) {
                count++;
            }
        }

        public int getCount() {
            synchronized (this) {
                return count;
            }
        }

        public static void main(String[] args) {
            Counter counter = new Counter();

            // Create multiple threads to increment the counter
            Thread thread1 = new Thread(() -> {
                for (int i = 0; i < 1000; i++) {
                    counter.increment();
                }
            });

            Thread thread2 = new Thread(() -> {
                for (int i = 0; i < 1000; i++) {
                    counter.increment();
                }
            });

            thread1.start();
            thread2.start();

            // Wait for threads to finish
            try {
                thread1.join();
                thread2.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            // Print the final count
            System.out.println("Final count: " + counter.getCount());
        }
    }
    ```

  In this example, a `Counter` class is created with methods to increment and get the count of a shared counter. The
  `increment` and `getCount` methods are synchronized using a synchronized block with the `this` object as the monitor.
  Multiple threads are created to increment the counter concurrently, and the final count is printed after the threads
  have finished.
- **199 . Can a static method be synchronized?** \
  Yes, a static method can be synchronized in Java. When a static method is synchronized, the lock acquired is on the
  class object associated with the method's class. This means that only one thread can execute the synchronized static
  method at a time, regardless of the number of instances of the class.

  Here is an example of a synchronized static method in Java:

    ```java
    public class Counter {
        private static int count = 0;

        public static synchronized void increment() {
            count++;
        }

        public static int getCount() {
            return count;
        }

        public static void main(String[] args) {
            // Create multiple threads to increment the counter
            Thread thread1 = new Thread(() -> {
                for (int i = 0; i < 1000; i++) {
                    Counter.increment();
                }
            });

            Thread thread2 = new Thread(() -> {
                for (int i = 0; i < 1000; i++) {
                    Counter.increment();
                }
            });

            thread1.start();
            thread2.start();

            // Wait for threads to finish
            try {
                thread1.join();
                thread2.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            // Print the final count
            System.out.println("Final count: " + Counter.getCount());
        }
    }
    ```

  In this example, the `increment` method is a synchronized static method that increments a shared static counter. The
  `increment` method is synchronized to ensure that only one thread can increment the counter at a time, even when
  multiple threads are accessing the method concurrently.
- **200 . What is the use of join method in threads?** \
  The `join` method in Java is used to wait for a thread to complete its execution before continuing with the current
  thread. When the `join` method is called on a thread, the current thread will block and wait for the specified thread
  to finish before proceeding.

  Here is an example of using the `join` method in Java:

    ```java
    public class Main {
        public static void main(String[] args) {
            Thread thread = new Thread(() -> {
                System.out.println("Thread started");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread finished");
            });

            thread.start();

            // Wait for the thread to finish
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("Main thread finished");
        }
    }
    ```

  In this example, a thread is created that sleeps for 2 seconds before finishing. The `join` method is called on the
  thread to wait for it to finish before printing a message in the main thread. This ensures that the main thread waits
  for the thread to complete before continuing.
- **201 . Describe a few other important methods in threads?** \
  Some other important methods in Java threads include:
    - **`start`**: The `start` method is used to start a thread and execute its `run` method asynchronously.
    - **`sleep`**: The `sleep` method is used to pause the execution of a thread for a specified amount of time.
    - **`yield`**: The `yield` method is used to give up the current thread's turn and allow other threads to run.
    - **`interrupt`**: The `interrupt` method is used to interrupt a thread that is blocked or sleeping.
    - **`isAlive`**: The `isAlive` method is used to check if a thread is alive and running.
    - **`setName` and `getName`**: The `setName` and `getName` methods are used to set and get the name of a thread.
    - **`setPriority` and `getPriority`**: The `setPriority` and `getPriority` methods are used to set and get the
      priority of a thread.
    - **`join`**: The `join` method is used to wait for a thread to complete its execution before continuing with the
      current thread.
    - **`wait` and `notify`**: The `wait` and `notify` methods are used for inter-thread communication and
      synchronization
      in multi-threaded programs.
    - **`isInterrupted` and `interrupted`**: The `isInterrupted` and `interrupted` methods are used to check if a thread
      has been interrupted.
    - **`run`**: The `run` method is the entry point for a thread's execution and contains the code that the thread will
      run.
- **202 . What is a deadlock? How can you avoid a deadlock?** \
  A deadlock is a situation in multi-threaded programming where two or more threads are blocked forever, waiting for
  each
  other to release resources that they need to continue execution. Deadlocks can occur when multiple threads acquire
  locks on resources in a different order, leading to a circular dependency that prevents any thread from making
  progress.

  To avoid deadlocks in multi-threaded programs, you can follow some best practices:
    - **Avoid Nested Locks**: Try to avoid acquiring multiple locks in nested order, as this can lead to deadlocks.
    - **Use a Timeout**: Use a timeout when acquiring locks to prevent threads from waiting indefinitely.
    - **Avoid Circular Dependencies**: Ensure that threads acquire locks in a consistent order to avoid circular
      dependencies.
    - **Use Lock Ordering**: Establish a global lock ordering to ensure that threads acquire locks in a consistent
      order.
    - **Use Deadlock Detection**: Implement deadlock detection mechanisms to identify and resolve deadlocks when they
      occur.

  By following these best practices and designing multi-threaded programs carefully, you can reduce the likelihood of
  deadlocks and improve the reliability of your applications.
- **203 . What are the important methods in Java for inter**-thread communication? \
  Java provides several methods for inter-thread communication, including:
    - **`wait` and `notify`**: The `wait` and `notify` methods are used to coordinate the execution of threads by
      allowing
      threads to wait for a condition to be met and notify other threads when the condition is satisfied.
    - **`wait(long timeout)` and `notifyAll`**: The `wait(long timeout)` method allows a thread to wait for a specified
      amount of time before continuing, while the `notifyAll` method notifies all waiting threads to wake up and
      continue execution
- **204 . What is the use of wait method?** \
  The `wait` method in Java is used to make a thread wait until a condition is met. When a thread calls the `wait`
  method,
  it releases the lock it holds and enters a waiting state until another thread calls the `notify` or `notifyAll` method
  on the same object. The `wait` method is typically used for inter-thread communication and synchronization in
  multi-threaded programs.
- **205 . What is the use of notify method?** \
  The `notify` method in Java is used to wake up a single thread that is waiting on the same object. When a thread calls
  the `notify` method, it notifies a single waiting thread to wake up and continue execution. The `notify` method is
  typically used in conjunction with the `wait` method for inter-thread communication and synchronization in
  multi-threaded programs.
- **206 . What is the use of notifyall method?** \
  The `notifyAll` method in Java is used to wake up all threads that are waiting on the same object. When a thread calls
  the `notifyAll` method, it notifies all waiting threads to wake up and
- **207 . Can you write a synchronized program with wait and notify methods?** \
  Here is an example of a synchronized program using the `wait` and `notify` methods for inter-thread communication in
  Java:

    ```java
    public class Main {
        public static void main(String[] args) {
            Object lock = new Object();

            Thread producer = new Thread(() -> {
                synchronized (lock) {
                    System.out.println("Producer thread started");
                    try {
                        lock.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("Producer thread resumed");
                }
            });

            Thread consumer = new Thread(() -> {
                synchronized (lock) {
                    System.out.println("Consumer thread started");
                    lock.notify();
                    System.out.println("Consumer thread notified");
                }
            });

            producer.start();
            consumer.start();
        }
    }
    ```

  In this example, a producer thread and a consumer thread are created to demonstrate the use of the `wait` and `notify`
  methods for inter-thread communication. The producer thread waits for the consumer thread to notify it before
  continuing, while the consumer thread notifies the producer thread to resume

### Functional Programming - Lambda expressions and Streams

- **208 . What is functional programming? How is it different from object**-oriented programming? \
  Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions
  and avoids changing state and mutable data. Functional programming focuses on the use of pure functions, higher-order
  functions, and immutable data structures to achieve declarative and concise code. Functional programming is based on
  the principles of lambda calculus and emphasizes the use of functions as first-class citizens.

  Some key differences between functional programming and object-oriented programming include:
    - **State and Mutability**: Functional programming avoids changing state and mutable data, while object-oriented
      programming uses objects and classes to model state and behavior.
    - **Functions vs. Objects**: Functional programming focuses on functions as the primary building blocks of programs,
      while object-oriented programming uses objects to encapsulate state and behavior.
    - **Immutability**: Functional programming emphasizes the use of immutable data structures to avoid side effects and
      make programs easier to reason about.
    - **Declarative vs. Imperative**: Functional programming is more declarative, focusing on what should be done rather
      than how it should be done, while object-oriented programming is more imperative, specifying the steps to achieve
      a
      result.
    - **Concurrency**: Functional programming is well-suited for concurrent and parallel programming due to its emphasis
      on immutability and pure functions.

  Functional programming languages like Haskell, Scala, and Clojure provide built-in support for functional programming
  features, while languages like Java have introduced functional programming concepts like lambda expressions and
  streams to support functional programming paradigms.
- **209 . Can you give an example of functional programming?** \
  Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions
  and avoids changing state and mutable data. Functional programming focuses on the use of pure functions, higher-order
  functions, and immutable data structures to achieve declarative and concise code. Functional programming is based on
  the principles of lambda calculus and emphasizes the use of functions as first-class citizens.

  Here is an example of functional programming in Java using lambda expressions:

    ```java
    import java.util.Arrays;
    import java.util.List;

    public class Main {
        public static void main(String[] args) {
            List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

            // Using lambda expression to square each element
            numbers.stream()
                   .map(n -> n * n)
                   .forEach(System.out::println);
        }
    }
    ```

  In this example, a list of integers is created, and a lambda expression is used with the `map` method of the `Stream`
  interface to square each element in the list. The result is then printed to the console using the `forEach` method.
  This example demonstrates the use of functional programming concepts like lambda expressions and streams in Java.
- **210 . What is a stream?**
- **211 . Explain about streams with an example? what are intermediate operations in streams?** \
  Streams in Java provide a way to process collections of elements in a functional and declarative manner. Streams
  enable you to perform operations like filtering, mapping, sorting, and reducing on collections using a fluent and
  pipeline-based API. Streams are designed to be lazy, parallelizable, and efficient for processing large amounts of
  data.

  Here is an example of using streams in Java:

    ```java
    import java.util.Arrays;
    import java.util.List;

    public class Main {
        public static void main(String[] args) {
            List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

            // Using streams to filter and print even numbers
            numbers.stream()
                   .filter(n -> n % 2 == 0)
                   .forEach(System.out::println);
        }
    }
    ```

  In this example, a list of integers is created, and a stream is obtained using the `stream` method. The `filter`
  method is then used to filter even numbers from the stream, and the result is printed to the console using the
  `forEach` method. This example demonstrates the use of streams and intermediate operations like `filter` in Java.
- **212 . What are terminal operations in streams?** \
  Terminal operations in streams are operations that produce a result or a side effect and terminate the stream
  processing. Terminal operations are the final step in a stream pipeline and trigger the execution of intermediate
  operations on the stream elements. Some common terminal operations in streams include `forEach`, `collect`, `reduce`,
  and `count`. Terminal operations are essential for processing streams and obtaining the final result of the stream
  processing.
- **213 . What are method references? How are they used in streams?** \
  Method references in Java provide a way to refer to methods or constructors without invoking them. Method references
  are shorthand syntax for lambda expressions that call a single method or constructor. Method references can be used in
  streams to simplify the code and make it more readable by replacing lambda expressions with method references.

  Here is an example of using method references in streams in Java:

    ```java
    import java.util.Arrays;
    import java.util.List;

    public class Main {
        public static void main(String[] args) {
            List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

            // Using method reference to print each name
            names.forEach(System.out::println);
        }
    }
    ```

  In this example, a list of names is created, and a method reference `System.out::println` is used with the `forEach`
  method to print each name in the list. The method reference `System.out::println` refers to the `println` method of
  the
  `System.out` class and is equivalent to a lambda expression `(name) -> System.out.println(name)`. Method references
  provide a concise and readable way to refer to methods in streams and other functional programming constructs in Java.
- **214 . What are lambda expressions? How are they used in streams?** \
  Lambda expressions in Java provide a way to define anonymous functions or blocks of code that can be passed as
  arguments to methods or stored in variables. Lambda expressions are a concise and expressive way to represent
  functions and enable functional programming paradigms in Java. Lambda expressions are used in streams to define
  operations on stream elements in a functional and declarative manner.

  Here is an example of using lambda expressions in streams in Java:

    ```java
    import java.util.Arrays;
    import java.util.List;

    public class Main {
        public static void main(String[] args) {
            List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

            // Using lambda expression to square each element
            numbers.stream()
                   .map(n -> n * n)
                   .forEach(System.out::println);
        }
    }
    ```

  In this example, a list of integers is created, and a lambda expression `n -> n * n` is used with the `map` method of
  the `Stream` interface to square each element in the list. The result is then printed to the console using the
  `forEach` method. Lambda expressions provide a concise and expressive way to define operations on stream elements in
  Java.
- **215 . Can you give an example of lambda expression?** \
  Lambda expressions in Java provide a way to define anonymous functions or blocks of code that can be passed as
  arguments to methods or stored in variables. Lambda expressions are a concise and expressive way to represent
  functions and enable functional programming paradigms in Java.

  Here is an example of a lambda expression in Java:

    ```java
    public class Main {
        public static void main(String[] args) {
            // Lambda expression to add two numbers
            MathOperation add = (a, b) -> a + b;

            int result = add.operate(10, 20);
            System.out.println("Result: " + result);
        }

        interface MathOperation {
            int operate(int a, int b);
        }
    }
    ```

  In this example, a lambda expression `(a, b) -> a + b` is used to define a function that adds two numbers. The lambda
  expression is assigned to a functional interface `MathOperation` that defines a method `operate` to perform the
  operation. The lambda expression is then used to add two numbers and print the result to the console.
- **216 . Can you explain the relationship between lambda expression and functional interfaces?** \
  Lambda expressions in Java are closely related to functional interfaces, which are interfaces that have exactly one
  abstract method. Lambda expressions can be used to provide an implementation for the abstract method of a functional
  interface, allowing you to define anonymous functions or blocks of code that can be passed as arguments to methods or
  stored in variables.

  Here is an example of using a lambda expression with a functional interface in Java:

    ```java
    public class Main {
        public static void main(String[] args) {
            // Lambda expression to add two numbers
            MathOperation add = (a, b) -> a + b;

            int result = add.operate(10, 20);
            System.out.println("Result: " + result);
        }

        interface MathOperation {
            int operate(int a, int b);
        }
    }
    ```

  In this example, a lambda expression `(a, b) -> a + b` is used to define a function that adds two numbers. The lambda
  expression is assigned to a functional interface `MathOperation` that defines a method `operate` to perform the
  operation. The lambda expression provides an implementation for the abstract method of the functional interface,
  allowing you to define and use anonymous functions in Java.
- **217 . What is a predicate?** \
  A predicate in Java is a functional interface that represents a boolean-valued function of one argument. Predicates
  are
  commonly used in functional programming to define conditions or filters that can be applied to elements in a
  collection. Predicates can be combined using logical operators like `and`, `or`, and `negate` to create complex
  conditions for filtering elements.

  Here is an example of using a predicate in Java:

    ```java
    import java.util.Arrays;
    import java.util.List;
    import java.util.function.Predicate;

    public class Main {
        public static void main(String[] args) {
            List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

            // Define a predicate to filter even numbers
            Predicate<Integer> isEven = n -> n % 2 == 0;

            // Filter even numbers from the list
            numbers.stream()
                   .filter(isEven)
                   .forEach(System.out::println);
        }
    }
    ```

  In this example, a predicate `isEven` is defined to filter even numbers from a list of integers. The predicate is used
  with the `filter` method of the `Stream` interface to apply the condition and print the even numbers to the console.
- **218 . What is the functional interface **- function? \
  The `Function` interface in Java is a functional interface that represents a function that accepts one argument and
  produces a result. The `Function` interface is commonly used in functional programming to define transformations or
  mappings that can be applied to elements in a collection. The `Function` interface provides a method `apply` to
  perform the transformation and produce the result.

  Here is an example of using the `Function` interface in Java:

    ```java
    import java.util.function.Function;

    public class Main {
        public static void main(String[] args) {
            // Define a function to square a number
            Function<Integer, Integer> square = n -> n * n;

            // Apply the function to a number
            int result = square.apply(5);
            System.out.println("Result: " + result);
        }
    }
    ```

  In this example, a function `square` is defined to square a number. The function is assigned to a `Function` interface
  that accepts an integer and produces an integer. The function is then applied to a number using the `apply` method to
  calculate the square and print the result to the console.
- **219 . What is a consumer?** \
  A consumer in Java is a functional interface that represents an operation that accepts a single input argument and
  returns no result. Consumers are commonly used in functional programming to perform side effects or actions on
  elements
  in a collection without producing a result. Consumers provide a method `accept` to perform the operation on the input
  argument.

  Here is an example of using a consumer in Java:

    ```java
    import java.util.function.Consumer;

    public class Main {
        public static void main(String[] args) {
            // Define a consumer to print a message
            Consumer<String> printMessage = message -> System.out::println;

            // Accept the message and print it
            printMessage.accept("Hello, World!");
        }
    }
    ```

  In this example, a consumer `printMessage` is defined to print a message. The consumer is assigned to a `Consumer`
  interface that accepts a string and performs the operation to print the message. The consumer is then used to accept
  the message and print it to the console.
- **220 . Can you give examples of functional interfaces with multiple arguments?** \
  Functional interfaces in Java can have multiple arguments by defining methods with multiple parameters. You can create
  functional interfaces with multiple arguments by specifying the number of input arguments in the method signature and
  using lambda expressions to provide implementations for the method.

  Here is an example of a functional interface with multiple arguments in Java:

    ```java
    public class Main {
        public static void main(String[] args) {
            // Define a functional interface with multiple arguments
            MathOperation add = (a, b) -> a + b;

            int result = add.operate(10, 20);
            System.out.println("Result: " + result);
        }

        interface MathOperation {
            int operate(int a, int b);
        }
    }
    ```

  In this example, a functional interface `MathOperation` is defined with a method `operate` that accepts two integers
  and returns an integer. The functional interface is used with a lambda expression `(a, b) -> a + b` to define a
  function that adds two numbers. The lambda expression provides an implementation for the method of the functional
  interface, allowing you to define and use functions with multiple arguments in Java.

### New Features

- **221 . What are the new features in Java **5? \
  Java 5 introduced several new features and enhancements to the Java programming language, including:
    - **Generics**: Java 5 introduced generics to provide compile-time type safety and reduce the need for explicit
      casting of objects. Generics allow you to define classes, interfaces, and methods with type parameters that can be
      used to enforce type constraints and improve code readability.
    - **Enhanced for Loop**: Java 5 introduced the enhanced for loop, also known as the "for-each" loop, to simplify
      iterating over collections and arrays. The enhanced for loop provides a more concise syntax for iterating over
      elements in a collection without the need for explicit indexing.
    - **Autoboxing and Unboxing**: Java 5 introduced autoboxing and unboxing to automatically convert primitive types to
      their corresponding wrapper classes and vice versa. Autoboxing allows you to use primitive types and wrapper
      classes interchangeably, simplifying code and improving readability.
    - **Varargs**: Java 5 introduced varargs, which allow you to pass a variable number of arguments to a method.
      Varargs
      provide a flexible way to define methods that accept a variable number of arguments without the need to create
      overloaded methods for different argument counts.
    - **Annotations**: Java 5 introduced annotations to provide metadata about classes, methods, and fields. Annotations
      allow you to add information to your code that can be used by the compiler, tools, and frameworks to generate
      code,
      perform validation, and configure behavior.
    - **Enumerations**: Java 5 introduced enumerations to provide a type-safe way to define a set of constants.
      Enumerations
      allow you to define a fixed set of values that can be used in place of magic numbers or strings, improving code
      readability and maintainability.
    - **Static Imports**: Java 5 introduced static imports to allow static members of a class to be imported directly
      into
      another class. Static imports provide a way to use static methods and constants without qualifying them with the
      class name, making code more concise and readable.

  These new features introduced in Java 5 helped to improve the expressiveness, readability, and maintainability of Java
  code and laid the foundation for future enhancements in the Java programming language.
- **222 . What are the new features in Java **6? \
  Java 6 introduced several new features and enhancements to the Java programming language, including:
    - **Scripting Support**: Java 6 introduced scripting support through the `javax.script` package, allowing you to
      execute scripts written in languages like JavaScript, Groovy, and Ruby within Java applications. Scripting support
      provides a way to embed scripting languages in Java applications and execute scripts dynamically at runtime.
    - **Compiler API**: Java 6 introduced the `javax.tools` package, which provides an API for compiling Java source
      code
      programmatically. The compiler API allows you to compile Java source code from within a Java program, enabling
      dynamic code generation and compilation.
    - **Pluggable Annotations**: Java 6 introduced pluggable annotations, which allow you to define custom annotations
      that can be processed at compile time using annotation processors. Pluggable annotations provide a way to extend
      the Java language with custom metadata and annotations that can be used to generate code, perform validation, and
      configure behavior.
    - **JDBC 4.0**: Java 6 introduced JDBC 4.0, which included several enhancements to the JDBC API for interacting with
      databases. JDBC 4.0 introduced features like automatic driver loading, improved exception handling, and support
      for
      SQLXML data types, making it easier to work with databases in Java applications.
    - **Java Compiler API**: Java 6 introduced the `javax.tools` package, which provides an API for compiling Java
      source
      code programmatically. The Java Compiler API allows you to compile Java source code from within a Java program,
      enabling dynamic code generation and compilation.
    - **Web Services**: Java 6 included updates to the Java API for XML Web Services (JAX-WS) and the Java Architecture
      for XML Binding (JAXB) to support the latest web services standards and technologies. These updates made it easier
      to develop and consume web services in Java applications.
    - **Java DB**: Java 6 included Java DB (formerly known as Apache Derby) as a built-in database that can be used for
      developing and testing Java database applications. Java DB provides a lightweight, embeddable database that can be
      used with Java applications without requiring a separate database installation.

  These new features introduced in Java 6 helped to improve the performance, productivity, and functionality of Java
  applications and provided developers with new tools and capabilities for building robust and scalable software
  systems.
- **223 . What are the new features in Java **7? \
  Java 7 introduced several new features and enhancements to the Java programming language, including:
    - **Diamond Operator**: Java 7 introduced the diamond operator (`<>`) to simplify the use of generics by inferring
      the
      type arguments from the context. The diamond operator allows you to create instances of generic classes without
      specifying the type arguments explicitly, reducing boilerplate code and improving readability.
    - **Try-With-Resources**: Java 7 introduced the try-with-resources statement to simplify resource management and
      ensure that resources like streams, connections, and files are closed properly after use. The try-with-resources
      statement automatically closes resources at the end of the block, reducing the risk of resource leaks and
      simplifying error handling.
    - **Strings in Switch**: Java 7 introduced the ability to use strings in switch statements, allowing you to switch
      on
      string values instead of just primitive types and enums. Strings in switch statements provide a more expressive
      way
      to handle multiple cases based on string values, improving code readability and maintainability.
    - **Binary Literals and Underscores in Numeric Literals**: Java 7 introduced support for binary literals (0b or 0B
      prefix) and underscores in numeric literals to improve readability and expressiveness when working with binary and
      numeric values
    - **224 . What are the new features in Java **8? \
      Java 8 introduced several new features and enhancements to the Java programming language, including:
        - **Lambda Expressions**: Java 8 introduced lambda expressions to provide a concise and expressive way to define
          anonymous functions or blocks of code. Lambda expressions enable functional programming paradigms in Java and
          simplify the use of functional interfaces like `Predicate`, `Function`, and `Consumer`.
        - **Streams API**: Java 8 introduced the Streams API to provide a fluent and pipeline-based API for processing
          collections of elements. Streams enable you to perform operations like filtering, mapping, sorting, and
          reducing
          on collections using functional programming constructs like lambda expressions and method references.
        - **Default Methods**: Java 8 introduced default methods in interfaces to allow interfaces to have concrete
          implementations for methods. Default methods provide a way to add new methods to interfaces without breaking
          existing implementations and enable the evolution of interfaces over time.
        - **Functional Interfaces**: Java 8 introduced the `@FunctionalInterface` annotation to define functional
          interfaces
          that have exactly one abstract method. Functional interfaces can be used with lambda expressions and method
          references to provide implementations for the abstract method.
        - **Method References**: Java 8 introduced method references to provide a shorthand syntax for lambda
          expressions
          that call a single method or constructor. Method references allow you to refer to methods or constructors
          without
          invoking them directly, improving code readability and conciseness.
        - **Optional Class**: Java 8 introduced the `Optional` class to provide a way to handle null values and avoid
          NullPointerExceptions. The `Optional` class provides methods to check for the presence of a value and safely
          access
          the value if it is present.
        - **Date and Time API**: Java 8 introduced the Date and Time API to provide a modern and comprehensive API for
          handling date and time values. The Date and Time API includes classes like `LocalDate`, `LocalTime`, and
          `ZonedDateTime`
          to represent date, time, and timezone information in a type-safe and immutable way.
        - **CompletableFuture**: Java 8 introduced the `CompletableFuture` class to provide a way to work with
          asynchronous
          computations and handle asynchronous results. `CompletableFuture` enables you to perform non-blocking and
          asynchronous operations using a fluent API and callbacks.

      These new features introduced in Java 8 helped to modernize the Java programming language and provide developers
      with new tools and capabilities for building robust and scalable software systems.

- **225 . What are the new features in Java **9? \
  Java 9 introduced several new features and enhancements to the Java programming language, including:
    - **Module System (Project Jigsaw)**: Java 9 introduced the module system to provide a way to modularize and
      encapsulate
      Java code. The module system allows you to define modules with explicit dependencies and access controls,
      improving
      code maintainability and security.
    - **JShell (Interactive Shell)**: Java 9 introduced JShell, an interactive shell for evaluating Java code snippets
      and expressions. JShell provides a way to experiment with Java code interactively and quickly test ideas without
      needing to create a full Java program.
    - **Private Methods in Interfaces**: Java 9 introduced the ability to define private methods in interfaces to
      encapsulate common code and reduce duplication. Private methods in interfaces provide a way to share code between
      default methods without exposing the implementation details.
    - **Stream API Enhancements**: Java 9 introduced several enhancements to the Streams API, including new methods like
      `takeWhile`, `dropWhile`, and `ofNullable` to improve the functionality and expressiveness of stream operations.
    - **Process API Updates**: Java 9 introduced updates to the Process API to provide better
- **226 . What are the new features in Java **11? \
  Java 11 introduced several new features and enhancements to the Java programming language, including:
    - **Local-Variable Syntax for Lambda Parameters**: Java 11 introduced the ability to use `var` as the type of
      lambda parameters in lambda expressions. This feature allows you to use `var` to declare the type of lambda
      parameters when the type can be inferred from the context, reducing boilerplate code and improving readability.
    - **HTTP Client (Standard)**: Java 11 introduced a new HTTP client API as a standard feature to provide a modern
      and flexible way to send HTTP requests and handle responses. The new HTTP client API supports HTTP/1.1 and HTTP/2
      protocols and provides a fluent and asynchronous API for working with HTTP.
    - **Epsilon Garbage Collector**: Java 11 introduced the Epsilon garbage collector, a no-op garbage collector that
      does not perform any memory reclamation. The Epsilon garbage collector is designed for performance testing and
      benchmarking to provide a baseline for comparing the performance of other garbage collectors.
    - **ZGC (Experimental)**: Java 11 introduced the Z Garbage Collector (ZGC) as an experimental feature to provide
      low-latency garbage collection for large heaps. ZGC is designed to reduce pause times and improve responsiveness
      for applications that require low-latency garbage collection.
    - **Flight Recorder (JFR) and Mission Control**: Java 11 introduced Flight Recorder (JFR) and Mission Control as
      open-source features to provide advanced monitoring and profiling capabilities for Java applications. Flight
      Recorder allows you to collect detailed runtime information and events, while Mission Control provides a graphical
      interface for analyzing and visualizing the collected data.
    - **Nest-Based Access Control**: Java 11 introduced nest-based access control to provide a more flexible and secure
      way to access private members of classes within the same nest. Nest-based access control allows classes that are
      logically part of the same group to access each other's private members, improving encapsulation and security.
    - **Dynamic Class-File Constants**: Java 11 introduced dynamic class-file constants to provide a way to define
      constants in class files that are dynamically computed at runtime. Dynamic class-file constants allow you to
      define constants that depend on the class's runtime context, enabling more flexible and dynamic code generation.
- **227 . What are the new features in Java **13? \
  Java 13 introduced several new features and enhancements to the Java programming language, including:
    - **Text Blocks (Preview Feature)**: Java 13 introduced text blocks as a preview feature to provide a more readable
      and maintainable way to write multi-line strings in Java. Text blocks allow you to define multi-line strings with
      improved formatting and indentation, making it easier to write and read complex string literals.
    - **Switch Expressions (Preview Feature)**: Java 13 introduced switch expressions as a preview feature to provide a
      more concise and expressive way to write switch statements. Switch expressions allow you to use the `->` operator
      to return a value from a switch case, enabling you to use switch statements as expressions that produce a result.
    - **Reimplement the Legacy Socket API**: Java 13 reimplemented the legacy Socket API to provide a more modern and
      efficient implementation of the socket communication protocol. The new Socket API is designed to improve
      performance
      and reliability for socket-based communication in Java applications.
    - **Dynamic CDS Archives**: Java 13 introduced dynamic class data-sharing (CDS) archives to provide a way to create
      and use CDS archives at runtime. Dynamic CDS archives allow you to optimize class loading and sharing for improved
      startup time and memory footprint in Java applications.
    - **FileSystems.newFileSystem() Method**: Java 13 introduced the `FileSystems.newFileSystem()` method to provide a
      way to create new file systems dynamically at runtime. The new method allows you to create file systems from
      various sources like ZIP files, JAR files, and custom providers, enabling more flexible and dynamic file system
      operations.
    - **ZGC (Production Feature)**: Java 13 promoted the Z Garbage Collector (ZGC) to a production feature to provide
      low-latency garbage collection for large heaps. ZGC is designed to reduce pause times and improve responsiveness
      for applications that require low-latency garbage collection.
    - **Text Blocks (Second Preview)**: Java 13 introduced text blocks as a second preview feature to provide a more
      readable and maintainable way to write multi-line strings in Java. Text blocks allow you to define multi-line
      strings with improved formatting and indentation, making it easier to write and read complex string literals.
- **228 . What are the new features in Java **17? \
  Java 17 introduced several new features and enhancements to the Java programming language, including:
    - **Sealed Classes (Standard Feature)**: Java 17 introduced sealed classes as a standard feature to provide a way to
      restrict the subclasses of a class. Sealed classes allow you to define a limited set of subclasses that can extend
      a class, improving code maintainability and security.
    - **Pattern Matching for switch (Standard Feature)**: Java 17 introduced pattern matching for switch as a standard
      feature to provide a more concise and expressive way to write switch statements. Pattern matching for switch
      allows
      you to use patterns in switch cases to destructure objects and extract values, enabling more powerful and flexible
      switch statements.
    - **JEP 356: Enhanced Pseudo-Random Number Generators**: Java 17 introduced enhanced pseudo-random number generators
      to provide improved performance and security for generating random numbers. The enhanced pseudo-random number
      generators use a more efficient algorithm to generate random numbers and provide better randomness and
      unpredictability.
    - **JEP 382: New macOS Rendering Pipeline**: Java 17 introduced a new macOS rendering pipeline to provide better
      performance and compatibility for rendering graphics on macOS. The new rendering pipeline uses the Metal API to
      improve graphics rendering and reduce latency on macOS systems.
    - **JEP 391: macOS/AArch64 Port**: Java 17 introduced support for running Java applications on macOS systems with
      Apple Silicon (ARM64) processors. The macOS/AArch64 port enables Java applications to run natively on Apple
      Silicon
      hardware, providing better performance and compatibility for macOS users.
    - **JEP 411: Deprecate the Security Manager for Removal**: Java 17 deprecated the Security Manager for removal in
      future releases. The Security Manager is a legacy feature that provides security checks and restrictions for Java
      applications, but it is no longer widely used and has been replaced by other security mechanisms.
    - **JEP 412: Foreign Function & Memory API (Incubator)**: Java 17 introduced the Foreign Function & Memory API as
      an incubator feature to provide a way to interoperate with native code and memory in Java applications. The
      Foreign
      Function & Memory API allows you to call native functions and access native memory directly from Java code,
      enabling
      better integration with native libraries and systems.
    - **JEP
- **228 . What are the new features in Java **21? \
  Java 21 introduced several new features and enhancements to the Java programming language, including:
    - **JEP 406: Pattern Matching for switch (Standard Feature)**: Java 21 introduced pattern matching for switch as a
      standard feature to provide a more concise and expressive way to write switch statements. Pattern matching for
      switch
      allows you to use patterns in switch cases to destructure objects and extract values, enabling more powerful and
      flexible switch statements.
    - **JEP 413: Code Snippets in Java API Documentation**: Java 21 introduced code snippets in Java API documentation
      to
      provide more interactive and informative examples for developers. Code snippets allow you to see and run code
      examples
      directly in the API documentation, making it easier to understand and use Java APIs.
    - **JEP 414: Vector API (Second Incubator)**: Java 21 introduced the Vector API as a second incubator feature to
      provide a way to perform vectorized operations on arrays and vectors in Java applications. The Vector API allows
      you
      to use vector instructions and hardware acceleration to improve performance for numerical and scientific
      computing.
    - **JEP 415: Context-Specific Deserialization Filters**: Java 21 introduced context-specific deserialization filters
      to provide a way to filter and control the deserialization of objects based on the context. Context-specific
      deserialization filters allow you to define custom filters that can be applied to specific deserialization
      operations,
      improving security and performance for Java applications.
    - **JEP 416: Java Embedded Content API**: Java 21 introduced the Java Embedded Content API to provide a way to embed
      content like images, videos, and other media in Java applications. The Java Embedded Content API allows you to
      load,
      display, and interact with embedded content in Java applications, enabling richer and more interactive user
      interfaces.
    - **JEP 417: Vector API (Incubator)**: Java 21 introduced the Vector API as an incubator feature to provide a way to
      perform vectorized operations on arrays and vectors in Java applications. The Vector API allows you to use vector
      instructions and hardware acceleration to improve performance for numerical and scientific computing.
    - **JEP 418: Java on Windows AArch64**: Java 21 introduced support for running Java applications on Windows systems
      with ARM64 processors. Java on Windows AArch64 enables Java applications to run natively on Windows ARM64
      hardware,
    - **JEP 419: Java on Alpine Linux**: Java 21 introduced support for running Java applications on Alpine Linux, a
      lightweight and secure Linux distribution. Java on Alpine Linux provides better compatibility and performance for
      Java applications running in containerized environments and cloud-native architectures.
    - **JEP 420: Java on Docker**: Java 21 introduced support for running Java applications on Docker containers to
      provide a more seamless and integrated experience for Java developers. Java on Docker enables you to build,
      package,
      and deploy Java applications in Docker containers, improving portability and scalability for Java applications.
    - **JEP 421: Java on Kubernetes**: Java 21 introduced support for running Java applications on Kubernetes, a popular
      container orchestration platform. Java on Kubernetes provides better integration and management of Java
      applications
      in Kubernetes environments, enabling you to deploy and scale Java applications more effectively in cloud-native
      architectures.
    - **JEP 422: Java on AWS**: Java 21 introduced support for running Java applications on Amazon Web Services (AWS),
      a leading cloud computing platform. Java on AWS provides better integration and performance for Java applications
      running on AWS services, enabling you to build and deploy Java applications in the cloud more effectively.
    - **JEP 423: Java on Azure**: Java 21 introduced support for running Java applications on Microsoft Azure, a
      cloud computing platform. Java on Azure provides better integration and scalability for Java applications running
      on Azure services, enabling you to build and deploy Java applications in the cloud more effectively.
    - **JEP 424: Java on Google Cloud**: Java 21 introduced support for running Java applications on Google Cloud, a
      cloud computing platform. Java on Google Cloud provides better integration and performance for Java applications
      running on Google Cloud services, enabling you to build and deploy Java applications in the cloud more
      effectively.

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
