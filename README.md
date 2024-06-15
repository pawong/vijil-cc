# Vijil Code Challenge

Description is included in `Vijil Coding Challenege.pdf`.

There are three major categories of test for tesing a webserver.

- Load Testing
- Stress Testing
- Endurance Testing

**Load Testing** This test is the most basic. This test will ensure that the server can handle expected load. We run the code at x clients for some period of time. This means the server can handle without issues x number of users asking for request for duration of period given.

**Stress Testing** This test is useful for determining scalability. The goal of this testing will flood the server with request and see when the server starts to fail and return errors. This is usually cased by too many clients requesting pages/data at the same time.

**Endurance Testing** This test will be used to determine the longivity of the server. It can also determine failover scenarios.

## Requirements

- Python 3.11
- Poetry

## How To Use

### Build Environments

```bash
% make build
```

### Start Server

```bash
% make start-server
```

### Run Benchmarks

```bash
% make benchmarks
```

Sample output

```bash
Collecting benchmarks...
Load Test: {'clients': 10, 'tries': 2000, 'target': 'http://localhost:8000/test-get/0'}
Run Time: 9.692251 seconds

+------+---------+---------+---------+
|      |   codes |   sizes |   times |
|------+---------+---------+---------|
|    0 |     200 |    8080 |  12.551 |
|    1 |     200 |   19798 |   5.049 |
|    2 |     200 |   29626 |   6.545 |
|    3 |     200 |   25048 |   6.406 |
...
| 1997 |     200 |   30886 |   5.407 |
| 1998 |     200 |    6946 |   2.678 |
| 1999 |     200 |   18622 |   3.942 |
+------+---------+---------+---------+

Totals
    Request: 2000
    Success: 2000
    Failure: 0
Successful Sizes (bytes)
    Median: 21646.00
    Mean:   21387.07
    Mode:   646.00
Successful Times (milliseconds)
    Median: 4.75
    Mean:   4.76
    Mode:   5.02

Done.
```

### Stop Server

```bash
% make stop-server
```

## Results

Run

```bash
% make benchmarks
Collecting benchmarks...
Load Test: {'clients': 10, 'runtime': 30, 'target': 'http://localhost:8000/test-get/0'}
Run Time: 30.023395 seconds

Totals
    Request: 4981
    Success: 4981
    Failure: 0
Successful Sizes (bytes)
    Median: 21562.00
    Mean:   21282.52
    Mode:   40714.00
Successful Times (milliseconds)
    Median: 5.72
    Mean:   5.91
    Mode:   7.40

Stress Test: {'clients': 10000, 'runtime': 300, 'target': 'http://localhost:8000/test-get/0'}
Run Time: 310.555625 seconds

Totals
    Request: 54982
    Success: 54982
    Failure: 0
Successful Sizes (bytes)
    Median: 21142.00
    Mean:   21097.74
    Mode:   37690.00
Successful Times (milliseconds)
    Median: 5.77
    Mean:   6.08
    Mode:   7.51

Endurance Test: {'clients': 10, 'runtime': 900, 'target': 'http://localhost:8000/test-get/0'}
Run Time: 900.057108 seconds

Totals
    Request: 192413
    Success: 192413
    Failure: 0
Successful Sizes (bytes)
    Median: 21016.00
    Mean:   21029.26
    Mode:   37942.00
Successful Times (milliseconds)
    Median: 5.96
    Mean:   6.32
    Mode:   8.01

Done.
```

## TODO

- Add tests.

## Conclusion

This turned out to not be very affective. First and formost, I believe the code is unable to add requests to the `tasks` set fast enough. This makes it pretty ineffective for `STRESS TEST`. I wasn't seeing failures as I would have expect. Redesign would include running seperate clients each spawning their own set of requests. Also testing from the servicing machine is probably useless as well. It should also include having clients on seperate machines.

There are better tools out there, for example, [Locust](https://locust.io), [JMeter](https://jmeter.apache.org) or [Selenium](https://www.selenium.dev).
