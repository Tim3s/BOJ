#include <iostream>

long long a, r, N, MOD;

long long mypow(long long n) {
    long long cur = r;
    long long res = 1;
    while (n > 0) {
        if (n % 2 == 1) {
            res *= cur;
            res %= MOD;
        }
        cur *= cur;
        cur %= MOD;
        n /= 2;
    }
    return res;
}

long long calc(long long n) {
    if (n == 0)
        return 1;
    if (n % 2 == 0) {
        n /= 2;
        return (1 + r * (mypow(n) + 1) % MOD * calc(n - 1)) % MOD;
    }
    n /= 2;
    return ((1 + mypow(n + 1)) * calc(n)) % MOD;
}

int main() {
    std::cin >> a >> r >> N >> MOD;
    std::cout << (a * calc(N - 1)) % MOD;
}
