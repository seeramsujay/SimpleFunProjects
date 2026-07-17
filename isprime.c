#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(double n)
{
    if (n != (long long)n || n < 2.0) return false;

    long long num = (long long)n;

    if (num == 2 || num == 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;

    // sqrt(n) = exp(0.5 * log(n)) — using log to avoid i*i overflow and sqrt
    long long limit = (long long)exp(0.5 * log(n));

    for (long long i = 5; i <= limit; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }

    return true;
}

void factorize(long long n)
{
    printf("%lld = ", n);

    while (n % 2 == 0) { printf("2"); n /= 2; if (n > 1) printf(" × "); }

    for (long long i = 3; i * i <= n; i += 2) {
        while (n % i == 0) { printf("%lld", i); n /= i; if (n > 1) printf(" × "); }
    }

    if (n > 1) printf("%lld", n);
    printf("\n");
}

int main(void)
{
    double n;

    printf("Enter a number: ");
    scanf("%lf", &n);

    if (is_prime(n)) {
        printf("%.0f -> prime\n", n);
    } else {
        factorize((long long)n);
    }

    return 0;
}
