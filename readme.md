## Windows Setup

Apologies if I missed a few steps.

Here is (roughly) how I configured my Windows 10 Pro machine for python development.

### Install Python

It's recommended to use the Python.org installer, rather than installing it via Windows Store or otherwise. Apparently this makes upgrades easier?

[https://www.python.org/downloads/](https://www.python.org/downloads/)

### Install Nuitka and Compile

```bash
python -m venv venv
pip install -r requirements.txt
nuitka --standalone .\hello-scipy.py
```

### Results

- The "hello-scipy.dist" folder that contains the .exe is 171MB
- This compresses pretty well (35MB .7z, 60MB .zip)

### Notes

My Windows machine is a i5-13400F (10 cores, 16 threads) with 64GB RAM and NVMe SSD.

**First** compilation took about 15-20 minutes. The first part of it seemed to peg 2 cores @ 100%. The second portion took ??? minutes and pegged all 16 cores @ 100%. You may want to have a fire extinguisher ready.

**Second** compilation took "only" 4m46sec, seemed to use cached results from first time

According to the docs, cross-compilation is highly unfinished. Assume a Windows machine is necessary for compilation.

### Questions / Next Steps

- The [documentation](https://nuitka.net/user-documentation/user-manual.html) mentions Qt support; not sure about other GUI options.
- A wide variety of C backends are supported. By default it will use GCC.
- It would be worth exploring other backends to see if they perform better in terms of runtime or compilation performance
- Hopefully we can precompile scipy and numpy and cache those results so we don't have 20+ minute compilations every time. =)
