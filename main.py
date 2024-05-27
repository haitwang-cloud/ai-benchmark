
import ai_benchmark
import sys


def main():
    benchmark = ai_benchmark.AIBenchmark()
    results = benchmark.run_training(precision="high")
    print(results)
    sys.exit(0)



if __name__ == "__main__":
    # execute only if run as a script
    main()
