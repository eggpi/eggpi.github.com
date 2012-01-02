import operator
import itertools

def factorials():
    def delayed_output():
        for i in output:
            yield i

    result, feedback = itertools.tee(delayed_output())
    seeded = itertools.chain([1], feedback)
    output = itertools.imap(operator.mul,
                            seeded,
                            itertools.count(1))

    return result

if __name__ == "__main__":
    print list(itertools.islice(factorials(), 10))
