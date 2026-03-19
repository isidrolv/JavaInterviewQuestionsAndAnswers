
# **Addendum: 10 coding challenge exercises**


Each exercise includes:

* **Task description**
* **Starting code sample (incomplete or incorrect)**
* **Final expected solution**

---

# 1.- Counter Component (useState)

**Task:** Create a simple counter with increment and decrement buttons.

**Starting Code:**

```jsx
import React from "react";

function Counter() {
  let count = 0;

  return (
    <div>
      <p>Count: {count}</p>
      <button>Increment</button>
      <button>Decrement</button>
    </div>
  );
}

export default Counter;
```

**Final Expected Code:**

```jsx
import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
}

export default Counter;
```

---

## 2.- Toggle Button

**Task:** Implement a button that toggles between “ON” and “OFF”.

**Starting Code:**

```jsx
function Toggle() {
  let state = "OFF";

  return (
    <button>
      {state}
    </button>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useState } from "react";

function Toggle() {
  const [isOn, setIsOn] = useState(false);

  return (
    <button onClick={() => setIsOn(!isOn)}>
      {isOn ? "ON" : "OFF"}
    </button>
  );
}

export default Toggle;
```

---

## 3.- Fetch API Data

**Task:** Fetch and display posts from JSONPlaceholder API.

**Starting Code:**

```jsx
function Posts() {
  let posts = [];

  return (
    <div>
      <h2>Posts</h2>
      {posts.map(p => <p>{p.title}</p>)}
    </div>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useEffect, useState } from "react";

function Posts() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then(res => res.json())
      .then(data => setPosts(data.slice(0, 5)));
  }, []);

  return (
    <div>
      <h2>Posts</h2>
      {posts.map(p => <p key={p.id}>{p.title}</p>)}
    </div>
  );
}

export default Posts;
```

---

## 4.- Form Input Control

**Task:** Capture and display input text in real-time.

**Starting Code:**

```jsx
function InputForm() {
  let value = "";

  return (
    <div>
      <input />
      <p>You typed: {value}</p>
    </div>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useState } from "react";

function InputForm() {
  const [value, setValue] = useState("");

  return (
    <div>
      <input value={value} onChange={e => setValue(e.target.value)} />
      <p>You typed: {value}</p>
    </div>
  );
}

export default InputForm;
```

---

## 5.- Conditional Rendering

**Task:** Show “Welcome, User!” if logged in, otherwise show “Please log in.”

**Starting Code:**

```jsx
function Greeting() {
  let loggedIn = false;

  return (
    <div>
      Welcome!
    </div>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useState } from "react";

function Greeting() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <div>
      {loggedIn ? "Welcome, User!" : "Please log in."}
      <br />
      <button onClick={() => setLoggedIn(!loggedIn)}>
        {loggedIn ? "Logout" : "Login"}
      </button>
    </div>
  );
}

export default Greeting;
```

---

## 6.- Todo List

**Task:** Build a simple todo list where users can add tasks.

**Starting Code:**

```jsx
function TodoApp() {
  let todos = [];

  return (
    <div>
      <input />
      <button>Add</button>
      {todos.map(t => <li>{t}</li>)}
    </div>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useState } from "react";

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");

  const addTodo = () => {
    if (input.trim() !== "") {
      setTodos([...todos, input]);
      setInput("");
    }
  };

  return (
    <div>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={addTodo}>Add</button>
      <ul>
        {todos.map((t, i) => <li key={i}>{t}</li>)}
      </ul>
    </div>
  );
}

export default TodoApp;
```

---

## 7.- Theme Switcher (Dark/Light Mode)

**Task:** Toggle between dark and light theme.

**Starting Code:**

```jsx
function Theme() {
  let theme = "light";

  return (
    <div className={theme}>
      <button>Switch Theme</button>
    </div>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useState } from "react";

function Theme() {
  const [theme, setTheme] = useState("light");

  return (
    <div className={theme}>
      <p>Current Theme: {theme}</p>
      <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
        Switch Theme
      </button>
    </div>
  );
}

export default Theme;
```

---

## 8.- Stopwatch (Timer)

**Task:** Build a stopwatch with start and stop buttons.

**Starting Code:**

```jsx
function Stopwatch() {
  let time = 0;

  return (
    <div>
      <p>{time}</p>
      <button>Start</button>
      <button>Stop</button>
    </div>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useState, useEffect, useRef } from "react";

function Stopwatch() {
  const [time, setTime] = useState(0);
  const [running, setRunning] = useState(false);
  const intervalRef = useRef(null);

  useEffect(() => {
    if (running) {
      intervalRef.current = setInterval(() => {
        setTime(t => t + 1);
      }, 1000);
    } else {
      clearInterval(intervalRef.current);
    }
    return () => clearInterval(intervalRef.current);
  }, [running]);

  return (
    <div>
      <p>{time} seconds</p>
      <button onClick={() => setRunning(true)}>Start</button>
      <button onClick={() => setRunning(false)}>Stop</button>
    </div>
  );
}

export default Stopwatch;
```

---

## 9.- Search Filter

**Task:** Filter a list of names as the user types.

**Starting Code:**

```jsx
function SearchList() {
  const names = ["Alice", "Bob", "Charlie"];

  return (
    <div>
      <input />
      <ul>
        {names.map(n => <li>{n}</li>)}
      </ul>
    </div>
  );
}
```

**Final Expected Code:**

```jsx
import React, { useState } from "react";

function SearchList() {
  const names = ["Alice", "Bob", "Charlie", "David", "Eve"];
  const [query, setQuery] = useState("");

  const filtered = names.filter(n =>
    n.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search..." />
      <ul>
        {filtered.map((n, i) => <li key={i}>{n}</li>)}
      </ul>
    </div>
  );
}

export default SearchList;
```

---

###10.- Custom Hook (useLocalStorage)

**Task:** Create a custom hook to persist state in localStorage.

**Starting Code:**

```jsx
function useLocalStorage(key, value) {
  return value;
}
```

**Final Expected Code:**

```jsx
import { useState, useEffect } from "react";

function useLocalStorage(key, initialValue) {
  const [stored, setStored] = useState(() => {
    const item = localStorage.getItem(key);
    return item ? JSON.parse(item) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(stored));
  }, [key, stored]);

  return [stored, setStored];
}

export default useLocalStorage;
```