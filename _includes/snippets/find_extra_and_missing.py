import math

def sum_arith_progression(n, m):
    """ Returns sum(n, n+1, n+2, ..., m) """

    return (m**2 - n**2 + n + m) / 2

def partition(l, p):
    """ Partition a list p as pivot value.
    Returns left_sum, right_sum, idx such that sum(l[s:idx+1]) == left_sum,
    sum(l[idx+1:e]) == right_sum and all elements in l[s:idx+1] are smaller
    than or equal to p, and all elements in l[idx+2:e] are greater than p.
    """

    i = 0
    j = len(l)-1

    left_sum = 0
    right_sum = 0

    while True:
        while i <= len(l)-1 and l[i] <= p:
            left_sum += l[i]
            i += 1
        while j >= 0 and l[j] > p:
            right_sum += l[j]
            j -= 1

        if i > j:
            break

        l[i], l[j] = l[j], l[i]

    return left_sum, right_sum, i-1

def find_extra_and_missing(l, s, t):
    """ Given a list of integers in the range [s, t] in which a single integer
    has been removed and another one has been added, find the missing and the
    extra integer.
    Returns a tuple (missing, extra).
    """

    while l:
        mid = (s + t) / 2

        left_sum, right_sum, p = partition(l, mid)
        expected_left = sum_arith_progression(s, mid)
        expected_right = sum_arith_progression(mid+1, t)
        expected_p = math.ceil(len(l)/2.0) - 1

        if p == expected_p: # missing and extra are on the same side
            if left_sum == expected_left:
                l = l[p+1:]
                s = mid + 1
            else:
                l = l[0:p+1]
                t = mid
        else:
            if p > expected_p: # extra on the left, missing on the right
                missing = expected_right - right_sum
                extra = left_sum - expected_left
            else: # extra on the right, missing on the left
                missing = expected_left - left_sum
                extra = right_sum - expected_right

            return missing, extra
