from statistics import mode

import arrow
import pandas
import tabulate
from numpy import mean, median
from tinyalowda import Tinyalowda


def analysis(pt, codes, sizes, times):
    df = pandas.DataFrame({"codes": codes, "sizes": sizes, "times": times})
    success_mask = df["codes"].isin([200])

    total_requests = len(df.index)
    success_count = len(df[success_mask].index)
    failure_count = len(df[~success_mask].index)

    median_size = median(df[success_mask]["sizes"].to_list())
    mean_size = mean(df[success_mask]["sizes"].to_list())
    mode_size = mode(df[success_mask]["sizes"].to_list())

    median_time = median(df[success_mask]["times"].to_list())
    mean_time = mean(df[success_mask]["times"].to_list())
    mode_time = mode(df[success_mask]["times"].to_list())

    if pt:
        print("")
        print(tabulate.tabulate(df, headers="keys", tablefmt="psql"))

    print("")
    print("Totals")
    print(f"    Request: {total_requests}")
    print(f"    Success: {success_count}")
    print(f"    Failure: {failure_count}")

    print("Successful Sizes (bytes)")
    print(f"    Median: {median_size:.2f}")
    print(f"    Mean:   {mean_size:.2f}")
    print(f"    Mode:   {mode_size:.2f}")

    print("Successful Times (milliseconds)")
    print(f"    Median: {median_time:.2f}")
    print(f"    Mean:   {mean_time:.2f}")
    print(f"    Mode:   {mode_time:.2f}")

    print("")


if __name__ == "__main__":
    # Load Test
    start = arrow.utcnow()
    load_params = {
        "clients": 10,
        "runtime": 30,
        "target": "http://localhost:8000/test-get/0",
    }
    print(f"Load Test: {load_params}")
    load_run = Tinyalowda(load_params)
    codes, sizes, times = load_run.run()
    stop = arrow.utcnow()
    print(f"Run Time: {(stop - start).total_seconds()} seconds")
    analysis(False, codes, sizes, times)

    # Stress Test
    start = arrow.utcnow()
    stress_params = {
        "clients": 10000,
        "runtime": 300,
        "target": "http://localhost:8000/test-get/0",
    }
    print(f"Stress Test: {stress_params}")
    stress_run = Tinyalowda(stress_params)
    codes, sizes, times = stress_run.run()
    stop = arrow.utcnow()
    print(f"Run Time: {(stop - start).total_seconds()} seconds")
    analysis(False, codes, sizes, times)

    # Endurance Testing
    start = arrow.utcnow()
    endurance_params = {
        "clients": 10,
        "runtime": 900,
        "target": "http://localhost:8000/test-get/0",
    }
    print(f"Endurance Test: {endurance_params}")
    endurance_run = Tinyalowda(endurance_params)
    codes, sizes, times = endurance_run.run()
    stop = arrow.utcnow()
    print(f"Run Time: {(stop - start).total_seconds()} seconds")
    analysis(False, codes, sizes, times)
