# ๐ Multithread Sockets Python

This is the representation of a Client Server behavior using multithreading and multiprocessing in Python.

![multiprocess.gif](img/multiprocess.gif)
๐จ Example with multiprocess server

## ๐ Requirements

Python 3 and Quotes

> To use the `quotes`, a pip library quotes was downloaded, it can be downloaded globally or in a virtual environment. 

> ๐ Note: Client is the only service that uses this library.

### Install quotes globally

```shell
pip install quotes
```

### If you want to create virtual enviroment

- Create it
```shell
python3 -m venv venv
```

- Activate it

    - Unix/macOS
    ```shell
    source venv/bin/activate
    ```
    
    - Windows
    ```shell
    ./venv\Script\activate
    ```

- Install requirement

```shell
pip install quotes
```

## ๐ฅ How to use


### ๐ก Server

- ๐งต Multithread server
```shell
python3 server.py multithread

```

or

- ๐จ Multiprocess server
```shell
python3 server.py multiprocess

```

### ๐ง Clients

Start clients
```shell
python3 clients.py <number_of_clients>

```
Each client sends two messages to the server
