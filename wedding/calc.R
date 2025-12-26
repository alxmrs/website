#!/usr/bin/env Rscript
# Source: https://stats.stackexchange.com/a/335132

# Compute the chance that in `n` independent rolls of a `d`-sided die,
# no side appears more than `m` times.
#
tmultinom <- function(n, m, d, count=FALSE) tmultinom.full(n, m, d, count)[n+1]
#
# Compute the chances that in 0, 1, 2, ..., `n` independent rolls of a
# `d`-sided die, no side appears more than `m` times.
#
tmultinom.full <- function(n, m, d, count=FALSE) {
  if (n < 0) return(numeric(0))
  one <- rep(1.0, n+1); names(one) <- 0:n
  if (d <= 0 || m >= n) return(one)

  if(count) log.p <- 0 else log.p <- -log(d)
  f <- function(n, m, d) {                   # The recursive solution
    if (d==1) return(one)                    # Base case
    r <- floor(d/2)
    x <- double(f(n, m, r), m)               # Combine two equal values
    if (2*r < d) x <- combine(x, one, m)     # Treat odd `d`
    return(x)
  }
  one <- c(log.p*(0:m), rep(-Inf, n-m))      # Reduction modulo x^(m+1)
  double <- function(x, m) combine(x, x, m)
  combine <- function(x, y, m) {             # The Binomial Theorem
    z <- sapply(1:length(x), function(n) {   # Need all powers 0..n
      z <- x[1:n] + lchoose(n-1, 1:n-1) + y[n:1]
      z.max <- max(z)
      log(sum(exp(z - z.max), na.rm=TRUE)) + z.max
    })
    return(z)
  }
  x <- exp(f(n, m, d)); names(x) <- 0:n
  return(x)
}

# Given that I encounter 23 random people, what are the odds
# that 3 of them have the same wedding day?
print('P(3 weddings | 23 people)')
print(tmultinom(23,2,365), digits=15)

# The birthday problem: find the number of people where the chance of
# a collision of `m+1` birthdays first exceeds `alpha`.
birthday <- function(m=1, d=365, alpha=0.50) {
  n <- 8
  while((p <- tmultinom.full(n, m, d))[n] > alpha) n <- n * 2
  return(p)
}

print('N people to have 50% chance of 3 people with the same wedding day.')
print(birthday(2, 365))