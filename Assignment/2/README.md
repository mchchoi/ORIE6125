ORIE6125 HW2
============

All files are stored in /webapp

* [Project Description](webapp/templates/project.html)
* [webapp/BinHeap\_Array.py](webapp/BinHeap_Array.py) -- implements binary heap in array form
* [webapp/test\_BinHeap\_Array.py](webapp/BinHeap_Array.py)-- unit test of binary heap in array form
* [webapp/BinHeap\_Ptr.py](webapp/BinHeap_Ptr.py)  -- implements binary heap in pointer
* [webapp/test\_BinHeap\_Ptr.py](webapp/test_BinHeap_Ptr.py) -- unit test of binary heap in pointer
* [webapp/heap.py](webapp/heap.py) -- Flask file to run locally
* [webapp/run.py](webapp/run.py) -- Flask file for heroku deployment

Heroku deployment
-----------------
[https://michael-orie6125.herokuapp.com/](https://michael-orie6125.herokuapp.com/)

Clone my work
-------------

For bare repository, run the following.
```
git clone --bare https://git.heroku.com/michael-orie6125.git
```


Run the webapp locally
----------------------

```
python webapp/heap.py
```

Unit test for the webapp
------------------------

We can perform the following tests either locally or via Heroku. Replace "http://127.0.0.1:5000/" by "http://michael-orie6125.herokuapp.com/" if we want to test the following on heroku!

### Test GET /project ###

```
curl -X GET http://127.0.0.1:5000/project
```

### Test GET /heap/\<name> and POST /heap/\<name> ###

```
curl -X GET http://127.0.0.1:5000/heap/2
```
```
curl -X POST http://127.0.0.1:5000/heap/2 -d values="2,9,100,6,7,1,4"
```
```
curl -X GET http://127.0.0.1:5000/heap/2
```

### Test GET /heap/\<name>/peak ###

```
curl -X GET http://127.0.0.1:5000/heap/2/peak
```

### Test GET /heap/\<name>/pop ###

```
curl -X GET http://127.0.0.1:5000/heap/2/pop
```
```
curl -X GET http://127.0.0.1:5000/heap/2 
```
```
curl -X GET http://127.0.0.1:5000/heap/2/pop
```
```
curl -X GET http://127.0.0.1:5000/heap/2
```

### Test GET /heap/time/array ###

```
curl --request GET 'http://127.0.0.1:5000/heap/time/array?length=100&seed=200'
```
```
curl --request GET 'http://127.0.0.1:5000/heap/time/array?length=a&seed=200'
```
```
curl --request GET 'http://127.0.0.1:5000/heap/time/array?length=0&seed=200'
```
```
curl --request GET 'http://127.0.0.1:5000/heap/time/array?length=100'
```

### Test GET /heap/time/pointer ###

```
curl --request GET 'http://127.0.0.1:5000/heap/time/pointer?length=100&seed=200'
```
```
curl --request GET 'http://127.0.0.1:5000/heap/time/pointer?length=a&seed=200'
```
```
curl --request GET 'http://127.0.0.1:5000/heap/time/pointer?length=0&seed=200'
```
```
curl --request GET 'http://127.0.0.1:5000/heap/time/pointer?length=100'
```

